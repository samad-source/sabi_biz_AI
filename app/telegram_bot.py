import os
import sys
import time
import requests
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath("."))

from app.router import route_user_query
from app.search_engine import recommend_from_query, format_recommendations
from app.image_search import get_business_image
from app.business_explainer import generate_business_explanation


# -----------------------------------
# LOAD ENV
# -----------------------------------
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in environment variables")

BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = 0


# -----------------------------------
# SAFE REQUEST WRAPPER
# -----------------------------------
def safe_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, timeout=30, **kwargs)
        return response.json()
    except Exception as e:
        print(f"⚠️ Network error: {e}")
        return {}


# -----------------------------------
# SEND MESSAGE
# -----------------------------------
def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    safe_request("POST", url, json=payload)


# -----------------------------------
# SEND PHOTO
# -----------------------------------
def send_photo(chat_id, image_url, caption=""):
    url = f"{BASE_URL}/sendPhoto"

    payload = {
        "chat_id": chat_id,
        "photo": image_url,
        "caption": caption[:900]  # safer limit
    }

    safe_request("POST", url, data=payload)


# -----------------------------------
# HANDLE MESSAGE
# -----------------------------------
def handle_message(message):
    try:
        chat_id = message["chat"]["id"]
        text = message.get("text", "").strip()

        # START COMMAND
        if text == "/start":
            welcome = (
                "🧠 Welcome to SabiBiz AI\n\n"
                "Try asking:\n"
                "- African restaurant in Lagos\n"
                "- cafe in New York\n"
                "- review for KFC\n"
                "- best pizza in Tampa"
            )
            send_message(chat_id, welcome)
            return

        # ROUTER
        reply_data = route_user_query(text)
        reply_type = reply_data.get("type")
        response = reply_data.get("response")

        # REVIEW
        if reply_type == "review":
            send_message(chat_id, f"✍️ AI Review\n\n{response}")
            return

        # RECOMMENDATION
        if reply_type == "recommendation":
            results = response

            if results is None or len(results) == 0:
                send_message(chat_id, "❌ No businesses found.")
                return

            for _, row in results.iterrows():
                try:
                    name = row.get("name", "Unknown")

                    # -----------------------------------
                    # FIXED IMAGE QUERY (IMPORTANT)
                    # -----------------------------------
                    search_query = f"{name} restaurant food"
                    image_url = get_business_image(search_query)

                    # fallback image if none found
                    if not image_url:
                        image_url = "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"

                    maps_url = f"https://www.google.com/maps/search/{name} {row.get('city','')}"

                    insight = generate_business_explanation(row)

                    caption = (
                        f"🏪 {name}\n\n"
                        f"⭐ Rating: {row.get('stars','N/A')}\n"
                        f"📍 City: {row.get('city','N/A')}\n"
                        f"📝 Reviews: {row.get('review_count','N/A')}\n\n"
                        f"🏷️ {row.get('categories','')}\n\n"
                        f"🤖 AI Insight:\n{insight}\n\n"
                        f"📍 Maps:\n{maps_url}"
                    )

                    send_photo(chat_id, image_url, caption)

                except Exception as e:
                    print("⚠️ Error processing business:", e)

            return

        # FALLBACK
        results = recommend_from_query(text)
        reply = format_recommendations(results)
        send_message(chat_id, reply)

    except Exception as e:
        print("⚠️ handle_message error:", e)
        send_message(chat_id, "⚠️ Something went wrong. Try again.")


# -----------------------------------
# GET UPDATES
# -----------------------------------
def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"

    params = {
        "timeout": 20,
        "offset": offset
    }

    return safe_request("GET", url, params=params)


# -----------------------------------
# MAIN LOOP
# -----------------------------------
def run_bot():
    global last_update_id

    print("🤖 Telegram Bot Running (Stable Mode)...")

    retry_delay = 2

    while True:
        try:
            data = get_updates(last_update_id + 1)

            if data and "result" in data:
                for update in data["result"]:
                    last_update_id = update["update_id"]

                    if "message" in update:
                        handle_message(update["message"])

            retry_delay = 2

        except Exception as e:
            print("🔥 Bot loop error:", e)
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * 2, 30)

        time.sleep(1)


# -----------------------------------
# START
# -----------------------------------
if __name__ == "__main__":
    run_bot()
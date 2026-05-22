import os
import requests
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_KEY = os.getenv("UNSPLASH_ACCESS_KEY")


def clean_query(query: str):
    query = query.lower().strip()

    # keep name meaningful, only remove noise words
    remove_words = ["in", "at", "near"]

    for word in remove_words:
        query = query.replace(word, "")

    query = " ".join(query.split())

    return query if query else "restaurant food"


def get_business_image(query: str):
    if not UNSPLASH_KEY:
        print("❌ Missing UNSPLASH_ACCESS_KEY")
        return None

    query = clean_query(query)

    url = "https://api.unsplash.com/search/photos"

    headers = {
        "Authorization": f"Client-ID {UNSPLASH_KEY}"
    }

    params = {
        "query": query,
        "per_page": 3,
        "orientation": "landscape"
    }

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)

        if response.status_code != 200:
            print(f"❌ Unsplash error {response.status_code}: {response.text}")
            return None

        data = response.json()
        results = data.get("results", [])

        if not results:
            print(f"⚠️ No image found for: {query}")
            return None

        return results[0]["urls"]["regular"]

    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None
import os
import json
import pandas as pd
from groq import Groq
from dotenv import load_dotenv

from app.memory import update_user, get_user

# Load env
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Load dataset safely
try:
    df = pd.read_csv("data/reviews_small.csv")
except Exception:
    df = pd.DataFrame()


def generate_review(user_id: str, business_id: str) -> str:

    if df.empty:
        return "Dataset not available."

    user_reviews = df[df["user_id"] == user_id]

    if user_reviews.empty:
        return "No review history found for this user."

    avg_rating = round(float(user_reviews["stars"].mean()), 2)

    personality = "positive reviewer" if avg_rating >= 4 else "critical reviewer"

    # SAFE MEMORY UPDATE (prevents history crash)
    try:
        update_user(user_id, "avg_rating", avg_rating)
        update_user(user_id, "personality", personality)
    except Exception:
        pass  # never crash app because of memory

    memory = get_user(user_id)

    prompt = f"""
You are simulating a realistic Nigerian customer review system.

User profile:
- Personality: {personality}
- Average rating behavior: {avg_rating}

Stored memory:
{memory}

Task:
Generate a realistic product review.

Return ONLY valid JSON:

{{
  "rating": 1-5,
  "review": "natural customer review"
}}

Rules:
- No explanation
- Only JSON
- Nigerian English tone
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Return only JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=200
        )

        content = response.choices[0].message.content

        if not content:
            return "Unable to generate review"

        try:
            result = json.loads(content)

            rating = int(result.get("rating", 3))
            review = result.get("review", "")

            stars = "★" * rating + "☆" * (5 - rating)

            return f"Rating: {rating} ({stars})\n\nReview: {review}"

        except Exception:
            return content

    except Exception as e:
        return f"Error generating review: {str(e)}"
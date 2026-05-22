import pandas as pd
import sys
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(BASE_DIR)

from app.query_understanding import extract_query_entities
from app.business_explainer import generate_business_explanation
from app.maps import generate_google_maps_link

# -----------------------------------
# LOAD DATASET
# -----------------------------------

business_df = pd.read_csv("data/businesses.csv")

# Clean dataset properly
business_df = business_df.dropna(subset=["name", "city", "categories", "stars", "review_count"])


# -----------------------------------
# SEARCH ENGINE
# -----------------------------------

def recommend_from_query(query: str, top_n: int = 5):

    entities = extract_query_entities(query)

    city = entities.get("city")
    cuisine = entities.get("cuisine")

    filtered = business_df.copy()

    # -----------------------------------
    # Filter by city
    # -----------------------------------
    if city:
        filtered = filtered[
            filtered["city"].str.lower().str.contains(city.lower(), na=False)
        ]

    # -----------------------------------
    # Filter by cuisine/category
    # -----------------------------------
    if cuisine:
        filtered = filtered[
            filtered["categories"].str.lower().str.contains(cuisine.lower(), na=False)
        ]

    # -----------------------------------
    # No results
    # -----------------------------------
    if filtered.empty:
        return []

    # -----------------------------------
    # Ranking Logic
    # -----------------------------------
    filtered = filtered.copy()

    filtered["score"] = (
        filtered["stars"] * 0.7 +
        filtered["review_count"] * 0.3
    )

    filtered = filtered.sort_values(by="score", ascending=False)

    return filtered.head(top_n)


# -----------------------------------
# FORMAT RESULTS
# -----------------------------------

def format_recommendations(results):

    if len(results) == 0:
        return (
            "❌ No matching businesses found.\n\n"
            "Try:\n"
            "- African restaurant in Tucson\n"
            "- cafe in Philadelphia\n"
            "- pizza in Tampa"
        )

    message = "🔥 Top Recommendations\n\n"

    for idx, (_, row) in enumerate(results.iterrows(), start=1):

        # Generate explanation safely
        explanation = generate_business_explanation(row)

        # Map link
        map_link = generate_google_maps_link(
            row.get("latitude"),
            row.get("longitude")
        )

        message += (
    f"{idx}. {row['name']}\n"
    f"⭐ {row['stars']}\n"
    f"📍 {row['address']}, {row['city']}\n"
    f"🗺️ Map:\n{map_link}\n"
    f"📝 Reviews: {row['review_count']}\n"
    f"🏷️ {row['categories']}\n\n"
    f"🤖 AI Insight:\n"
    f"{explanation}\n\n"
)

    return message


# -----------------------------------
# TEST
# -----------------------------------

if __name__ == "__main__":

    query = "African restaurant in Tucson"

    results = recommend_from_query(query)

    print(format_recommendations(results))
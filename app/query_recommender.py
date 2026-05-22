from typing import List, Dict, Any, Optional
import pandas as pd

# -----------------------------------
# LOAD BUSINESS DATA
# -----------------------------------

business_df: pd.DataFrame = pd.read_json(
    "data/yelp_academic_dataset_business.json",
    lines=True
)


# -----------------------------------
# QUERY RECOMMENDER
# -----------------------------------

def recommend_from_query(
    query: str,
    top_n: int = 5
) -> List[Dict[str, Any]]:

    query = query.lower()

    # -----------------------------------
    # CATEGORY DETECTION
    # -----------------------------------

    category_keywords: List[str] = [
        "cafe",
        "coffee",
        "restaurant",
        "pizza",
        "burger",
        "shawarma",
        "hotel",
        "bar",
        "lounge",
        "bakery"
    ]

    detected_category: Optional[str] = None

    for category in category_keywords:
        if category in query:
            detected_category = category
            break

    # -----------------------------------
    # CITY DETECTION
    # -----------------------------------

    detected_city: Optional[str] = None

    unique_cities = business_df["city"].dropna().unique()

    for city in unique_cities:
        if str(city).lower() in query:
            detected_city = str(city)
            break

    # -----------------------------------
    # FILTER BUSINESSES
    # -----------------------------------

    filtered: pd.DataFrame = business_df.copy()

    if detected_category:
        filtered = filtered[
            filtered["categories"]
            .fillna("")
            .astype(str)
            .str.contains(detected_category, case=False, na=False)
        ]

    if detected_city:
        filtered = filtered[
            filtered["city"]
            .fillna("")
            .astype(str)
            .str.contains(detected_city, case=False, na=False)
        ]

    # -----------------------------------
    # SORT BY RATINGS
    # -----------------------------------

    filtered = filtered.sort_values(
        by=["stars", "review_count"],
        ascending=False
    )

    # -----------------------------------
    # BUILD RESULTS
    # -----------------------------------

    results: List[Dict[str, Any]] = []

    top_results = filtered.head(top_n)

    for _, row in top_results.iterrows():

        explanation: str = (
            f"{row['name']} is highly rated "
            f"with {row['stars']} stars "
            f"from {row['review_count']} reviews."
        )

        results.append({
            "name": str(row["name"]),
            "city": str(row["city"]),
            "categories": str(row["categories"]),
            "stars": float(row["stars"]),
            "review_count": int(row["review_count"]),
            "explanation": explanation
        })

    return results


# -----------------------------------
# TEST
# -----------------------------------

if __name__ == "__main__":

    query = "cafe in Philadelphia"

    recommendations = recommend_from_query(query)

    print("\nRecommendations:\n")

    for idx, item in enumerate(recommendations, start=1):

        print(f"{idx}. {item['name']}")
        print(f"📍 {item['city']}")
        print(f"⭐ {item['stars']}")
        print(f"📝 {item['review_count']} reviews")
        print(f"🏷️ {item['categories']}")
        print(f"💡 {item['explanation']}")
        print("-" * 50)
import os
from typing import List, Dict, Any, Optional
import pandas as pd

# -----------------------------------
# SAFE DATA LOADING (OPTION 2 FIX)
# -----------------------------------

file_path = "data/yelp_academic_dataset_business.json"

if os.path.exists(file_path):
    business_df = pd.read_json(file_path, lines=True)
else:
    print("⚠️ business dataset missing — running fallback mode")

    business_df = pd.DataFrame(columns=[
        "business_id",
        "name",
        "address",
        "city",
        "categories",
        "stars",
        "review_count",
        "latitude",
        "longitude"
    ])


# -----------------------------------
# QUERY RECOMMENDER
# -----------------------------------
def recommend_from_query(query: str, top_n: int = 5) -> List[Dict[str, Any]]:

    query = query.lower()

    category_keywords: List[str] = [
        "cafe", "coffee", "restaurant", "pizza",
        "burger", "shawarma", "hotel", "bar",
        "lounge", "bakery"
    ]

    detected_category: Optional[str] = None

    for category in category_keywords:
        if category in query:
            detected_category = category
            break

    detected_city: Optional[str] = None

    if "city" in business_df.columns and not business_df.empty:
        for city in business_df["city"].dropna().unique():
            if str(city).lower() in query:
                detected_city = str(city)
                break

    filtered = business_df.copy()

    if detected_category and "categories" in filtered.columns:
        filtered = filtered[
            filtered["categories"]
            .fillna("")
            .astype(str)
            .str.contains(detected_category, case=False, na=False)
        ]

    if detected_city and "city" in filtered.columns:
        filtered = filtered[
            filtered["city"]
            .fillna("")
            .astype(str)
            .str.contains(detected_city, case=False, na=False)
        ]

    if filtered.empty:
        return []

    filtered = filtered.sort_values(
        by=["stars", "review_count"],
        ascending=False
    )

    results: List[Dict[str, Any]] = []

    for _, row in filtered.head(top_n).iterrows():

        results.append({
            "name": str(row.get("name", "Unknown")),
            "city": str(row.get("city", "N/A")),
            "categories": str(row.get("categories", "")),
            "stars": float(row.get("stars", 0)),
            "review_count": int(row.get("review_count", 0)),
            "explanation": f"{row.get('name')} is highly rated."
        })

    return results
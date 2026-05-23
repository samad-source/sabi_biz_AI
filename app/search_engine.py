import pandas as pd
import os

from app.query_understanding import extract_query_entities


# SAFE LOAD
if os.path.exists("data/businesses_small.csv"):

    business_df = pd.read_csv(
        "data/businesses_small.csv"
    )

else:

    business_df = pd.DataFrame({
        "name":["Demo Restaurant"],
        "city":["Lagos"],
        "categories":["Restaurant"],
        "stars":[5],
        "review_count":[100]
    })


def recommend_from_query(query, top_n=5):

    entities = extract_query_entities(query)

    city = entities.get("city")

    cuisine = entities.get("cuisine")

    filtered = business_df.copy()

    if city:

        filtered = filtered[
            filtered["city"]
            .str.contains(city,
            case=False,
            na=False)
        ]

    if cuisine:

        filtered = filtered[
            filtered["categories"]
            .str.contains(cuisine,
            case=False,
            na=False)
        ]

    return filtered.head(top_n)
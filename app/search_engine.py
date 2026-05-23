import pandas as pd
import os

DATA = "data/businesses_small.csv"

if os.path.exists(DATA):
    business_df = pd.read_csv(DATA)
else:
    business_df = pd.DataFrame()

business_df = business_df.fillna("")


def recommend_from_query(query, top_n=5):

    if business_df.empty:
        return pd.DataFrame()

    query = query.lower()

    filtered = business_df[
        business_df["name"].str.lower().str.contains(query)
        |
        business_df["categories"].str.lower().str.contains(query)
        |
        business_df["city"].str.lower().str.contains(query)
    ]

    if filtered.empty:

        words = query.split()

        for word in words:

            filtered = business_df[
                business_df["name"].str.lower().str.contains(word)
                |
                business_df["categories"].str.lower().str.contains(word)
                |
                business_df["city"].str.lower().str.contains(word)
            ]

            if not filtered.empty:
                break

    filtered = filtered.sort_values(
        by=["stars","review_count"],
        ascending=False
    )

    return filtered.head(top_n)
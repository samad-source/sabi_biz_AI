import os
import pandas as pd

print("Loading business dataset...")

file_path = "data/yelp_academic_dataset_business.json"

# -----------------------------------
# SAFE LOAD (OPTION 2 FIX)
# -----------------------------------
if os.path.exists(file_path):
    business_df = pd.read_json(file_path, lines=True)
else:
    print("⚠️ Dataset not found — skipping business load")
    business_df = pd.DataFrame()

# -----------------------------------
# ONLY PROCESS IF DATA EXISTS
# -----------------------------------
if not business_df.empty:

    business_df = business_df[
        [
            "business_id",
            "name",
            "address",
            "city",
            "categories",
            "stars",
            "review_count",
            "latitude",
            "longitude"
        ]
    ].dropna()

    business_df.to_csv("data/businesses_small.csv", index=False)

    print("✅ businesses_small.csv created successfully!")

    print("\nColumns:\n", business_df.columns)

    print("\nSample Businesses:\n", business_df.head())

else:
    print("⚠️ No dataset available — skipped processing")
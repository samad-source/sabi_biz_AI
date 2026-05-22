import pandas as pd

print("Loading business dataset...")

# -----------------------------------
# LOAD YELP BUSINESS DATA
# -----------------------------------

business_df = pd.read_json(
    "data/yelp_academic_dataset_business.json",
    lines=True
)

# -----------------------------------
# KEEP IMPORTANT COLUMNS
# -----------------------------------

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
]

# -----------------------------------
# REMOVE MISSING VALUES
# -----------------------------------

business_df = business_df.dropna()

# -----------------------------------
# SAVE CLEAN DATASET
# -----------------------------------

business_df.to_csv(
    "data/businesses.csv",
    index=False
)

print("✅ businesses.csv created successfully!")

print("\nColumns:\n")

print(
    business_df.columns
)

print("\nSample Businesses:\n")

print(
    business_df.head()
)
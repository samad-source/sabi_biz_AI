import streamlit as st
import pandas as pd

from app.user_model import analyze_user
from app.review_generator import generate_review

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv(
    "data/reviews_sample.csv"
)

business_df = pd.read_csv(
    "data/businesses.csv"
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="User Model Agent",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("👤 User Modeling Agent")

st.subheader(
    "AI-Powered Personality & Review Simulation"
)

# -----------------------------------
# USER SELECTION
# -----------------------------------

users = df["user_id"].unique()

selected_user = st.selectbox(
    "Select User",
    users
)

# -----------------------------------
# BUSINESS SELECTION
# -----------------------------------

business_names = sorted(
    business_df["name"].unique()
)

selected_business_name = st.selectbox(
    "Select Business",
    business_names
)

# -----------------------------------
# GET BUSINESS INFO
# -----------------------------------

business_row = business_df[
    business_df["name"]
    == selected_business_name
].iloc[0]

selected_business = business_row[
    "business_id"
]

business_city = business_row[
    "city"
]

business_category = business_row[
    "categories"
]

business_stars = business_row[
    "stars"
]

business_reviews = business_row[
    "review_count"
]

# -----------------------------------
# BUTTON
# -----------------------------------

if st.button("Generate AI Review"):

    # -----------------------------------
    # ANALYZE USER
    # -----------------------------------

    profile = analyze_user(
        selected_user
    )

    if not profile:

        st.error(
            "User not found."
        )

    else:

        st.success(
            "User analyzed successfully."
        )

        # -----------------------------------
        # USER METRICS
        # -----------------------------------

        st.divider()

        st.subheader(
            "📊 User Personality Analysis"
        )

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Average Rating",
            round(profile["avg_rating"], 2)
        )

        col2.metric(
            "Total Reviews",
            profile["total_reviews"]
        )

        col3.metric(
            "Personality",
            profile["personality"]
        )

        # -----------------------------------
        # BUSINESS INFORMATION
        # -----------------------------------

        st.divider()

        st.subheader(
            "🏪 Business Information"
        )

        st.write(
            f"📍 City: {business_city}"
        )

        st.write(
            f"⭐ Rating: {business_stars}"
        )

        st.write(
            f"📝 Total Reviews: {business_reviews}"
        )

        st.write(
            f"🏷️ Categories: {business_category}"
        )

        # -----------------------------------
        # REAL CUSTOMER REVIEWS
        # -----------------------------------

        st.divider()

        st.subheader(
            "💬 Previous Customer Reviews"
        )

        business_reviews_df = df[
            df["business_id"]
            == selected_business
        ]

        if len(business_reviews_df) > 0:

            sample_reviews = business_reviews_df[
                "text"
            ].head(3)

            for idx, review_text in enumerate(
                sample_reviews,
                start=1
            ):

                st.write(
                    f"🗣️ Review {idx}:"
                )

                st.info(review_text)

        else:

            st.warning(
                "No previous reviews found."
            )

        # -----------------------------------
        # AI GENERATED REVIEW
        # -----------------------------------

        st.divider()

        st.subheader(
            "✍️ AI Generated Nigerian Review"
        )

        review = generate_review(
            selected_user,
            selected_business
        )

        st.success(review)

        # -----------------------------------
        # AI BEHAVIORAL ANALYSIS
        # -----------------------------------

        st.divider()

        st.subheader(
            "🧠 Behavioral Analysis"
        )

        if profile["personality"] == "positive reviewer":

            st.success(
                "This user usually gives high ratings "
                "and focuses more on positive experiences, "
                "good service, and satisfaction."
            )

        elif profile["personality"] == "critical reviewer":

            st.warning(
                "This user is highly critical and "
                "tends to notice poor service, delays, "
                "pricing issues, and product quality problems."
            )

        else:

            st.info(
                "This user has balanced reviewing behavior "
                "and gives both positive and negative feedback "
                "depending on the experience."
            )
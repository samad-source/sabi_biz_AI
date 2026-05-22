import streamlit as st
import pandas as pd
import os

from app.user_model import analyze_user
from app.review_generator import generate_review


# ---------------------------
# SAFE DATA LOADING
# ---------------------------

if os.path.exists("data/reviews_sample.csv"):
    df = pd.read_csv("data/reviews_sample.csv")
else:
    df = pd.DataFrame({
        "user_id":[1],
        "business_id":["demo"],
        "stars":[5],
        "text":["Great place"],
        "funny":[0],
        "useful":[1],
        "cool":[0]
    })

if os.path.exists("data/businesses.csv"):
    business_df = pd.read_csv("data/businesses.csv")
else:
    business_df = pd.DataFrame({
        "business_id":["demo"],
        "name":["Demo Restaurant"],
        "city":["Lagos"],
        "categories":["Restaurant"],
        "stars":[5],
        "review_count":[100]
    })


st.set_page_config(
    page_title="User Model Agent",
    layout="wide"
)

st.title("👤 User Modeling Agent")

users = df["user_id"].unique()

selected_user = st.selectbox(
    "Select User",
    users
)

business_names = business_df["name"].unique()

selected_business = st.selectbox(
    "Select Business",
    business_names
)

if st.button("Generate AI Review"):

    profile = analyze_user(selected_user)

    st.write(profile)

    review = generate_review(
        selected_user,
        selected_business
    )

    st.success(review)
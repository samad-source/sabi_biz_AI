import pandas as pd
from typing import Union, TypedDict

from app.memory import update_user

# Load sample dataset
df = pd.read_csv("data/reviews_sample.csv")


class UserProfile(TypedDict):
    total_reviews: int
    average_rating: float
    most_common_rating: int
    funny_score: int
    useful_score: int
    cool_score: int
    profile_sentiment: str
    personality: str


def build_user_profile(user_id: Union[int, str]) -> Union[UserProfile, str]:

    # Get reviews from this user
    user_reviews = df[df["user_id"] == user_id]

    if len(user_reviews) == 0:
        return "User not found."

    average_rating = round(
        float(user_reviews["stars"].mean()),
        2
    )

    profile_sentiment = "positive"

    if average_rating < 3:
        profile_sentiment = "critical"

    # Personality logic
    if average_rating >= 4:
        personality = "positive reviewer"

    elif average_rating <= 2:
        personality = "critical reviewer"

    else:
        personality = "balanced reviewer"

    profile: UserProfile = {
        "total_reviews": int(len(user_reviews)),
        "average_rating": average_rating,
        "most_common_rating": int(user_reviews["stars"].mode()[0]),
        "funny_score": int(user_reviews["funny"].sum()),
        "useful_score": int(user_reviews["useful"].sum()),
        "cool_score": int(user_reviews["cool"].sum()),
        "profile_sentiment": profile_sentiment,
        "personality": personality
    }

    return profile


# -----------------------------------
# MAIN FUNCTION FOR AGENT SYSTEM
# -----------------------------------
def analyze_user(user_id: str):

    profile = build_user_profile(user_id)

    if isinstance(profile, str):
        return None

    # Save memory
    update_user(
        user_id,
        "avg_rating",
        profile["average_rating"]
    )

    update_user(
        user_id,
        "personality",
        profile["personality"]
    )

    return {
        "total_reviews": profile["total_reviews"],
        "avg_rating": profile["average_rating"],
        "most_common_rating": profile["most_common_rating"],
        "funny_score": profile["funny_score"],
        "useful_score": profile["useful_score"],
        "cool_score": profile["cool_score"],
        "personality": profile["personality"]
    }


# -----------------------------------
# TEST RUN
# -----------------------------------
if __name__ == "__main__":

    sample_user = str(df.iloc[0]["user_id"])

    print("Sample User:", sample_user)

    result = analyze_user(sample_user)

    print(result)
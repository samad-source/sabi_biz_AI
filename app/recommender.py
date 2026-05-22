import pandas as pd
from app.memory import get_user

df = pd.read_csv("data/reviews_sample.csv")


def get_popular_businesses():
    if df.empty or "business_id" not in df.columns:
        return pd.Series(dtype=float)

    return df.groupby("business_id")["stars"].mean().sort_values(ascending=False)


def recommend_businesses(query: str, user_id: str, top_n: int = 5):

    popular = get_popular_businesses()

    if popular.empty:
        return []

    results = []

    for biz_id, score in popular.head(top_n).items():
        results.append({
            "business_id": str(biz_id),
            "score": float(score),
            "explanation": "Top rated business"
        })

    return results


def recommend_businesses_personalized(query: str, user_id: str, top_n: int = 5):

    user = get_user(user_id)

    personality = user.get("personality", "neutral")

    if df.empty:
        return []

    business_scores = {}

    for biz_id in df["business_id"].unique():
        data = df[df["business_id"] == biz_id]
        score = data["stars"].mean()

        if personality == "positive reviewer":
            score += 0.2
        elif personality == "critical reviewer":
            score -= 0.1

        business_scores[biz_id] = score

    ranked = sorted(business_scores.items(), key=lambda x: x[1], reverse=True)

    return [
        {
            "business_id": biz_id,
            "score": round(score, 2),
            "explanation": "Personalized ranking"
        }
        for biz_id, score in ranked[:top_n]
    ]
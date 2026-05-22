from app.router import route_user_query
from app.memory import update_user, get_user
from app.recommender import (
    recommend_businesses,
    recommend_businesses_personalized
)
from app.review_generator import generate_review
from app.user_model import analyze_user


class SabiBizAgent:

    def __init__(self):
        self.name = "SabiBiz Agent"

    def think(self, user_id: str, query: str):

        route = route_user_query(query)
        memory = get_user(user_id)

        return {
            "route": route,
            "memory": memory,
            "query": query
        }

    def act(self, user_id: str, context: dict):

        route = context["route"]
        intent = route.get("intent")

        # -------------------
        # RECOMMENDATION
        # -------------------
        if intent == "recommend_business":
            return recommend_businesses(route["query"], user_id)

        # -------------------
        # REVIEW GENERATION (FIXED)
        # -------------------
        if intent == "generate_review":

            # fallback if business not found
            business_id = route.get("business_id") or "unknown"

            return generate_review(user_id, business_id)

        # -------------------
        # USER ANALYSIS
        # -------------------
        if intent == "analyze_user":
            return analyze_user(user_id)

        return {"message": "I don't understand the request"}

    def reflect(self, user_id: str, query: str, result: dict):
        update_user(user_id, "last_result", result)
        return result

    def run(self, user_id: str, query: str):

        context = self.think(user_id, query)
        result = self.act(user_id, context)
        final = self.reflect(user_id, query, result)

        return final
def route_user_query(query: str) -> dict:
    query = query.lower()

    # -------------------------
    # RECOMMENDATION INTENT
    # -------------------------
    if any(word in query for word in ["restaurant", "shop", "buy", "near me", "recommend", "business"]):
        return {
            "intent": "recommend_business",
            "query": query
        }

    # -------------------------
    # REVIEW INTENT
    # -------------------------
    if "review" in query or "rate" in query:
        return {
            "intent": "generate_review",
            "query": query
        }

    # -------------------------
    # ANALYZE USER INTENT
    # -------------------------
    if "analyze" in query or "profile" in query:
        return {
            "intent": "analyze_user",
            "query": query
        }

    # -------------------------
    # DEFAULT FALLBACK
    # -------------------------
    return {
        "intent": "unknown",
        "query": query
    }
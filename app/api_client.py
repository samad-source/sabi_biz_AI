import requests

API_URL = "http://api:8000/ask"  # IMPORTANT for Docker networking


def ask_agent(user_id: str, query: str):

    try:
        response = requests.post(
            API_URL,
            params={
                "user_id": user_id,
                "query": query
            },
            timeout=10
        )

        return response.json()

    except Exception as e:
        return {
            "error": "Failed to connect to API",
            "details": str(e)
        }
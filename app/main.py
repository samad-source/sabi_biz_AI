from fastapi import FastAPI, Query
from app.agent import SabiBizAgent
import traceback

app = FastAPI(title="SabiBiz AI", version="1.0")

agent = SabiBizAgent()


@app.get("/")
def home():
    return {"message": "SabiBiz running 🚀"}


@app.post("/ask")
def ask(
    user_id: str = Query(...),
    query: str = Query(...)
):
    try:
        result = agent.run(user_id, query)
        return {
            "status": "success",
            "data": result
        }

    except Exception as e:
        print("🔥 ERROR TRACEBACK:")
        print(traceback.format_exc())

        return {
            "status": "error",
            "message": str(e)
        }
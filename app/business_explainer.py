import os
from groq import Groq

# -----------------------------------
# INIT GROQ CLIENT
# -----------------------------------

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# -----------------------------------
# BUSINESS INSIGHT GENERATOR
# -----------------------------------

def generate_business_explanation(row):

    name = row["name"]
    stars = row["stars"]
    reviews = row["review_count"]
    categories = str(row["categories"])
    city = row.get("city", "unknown location")

    # -----------------------------------
    # STRUCTURED PROMPT (IMPORTANT FIX)
    # -----------------------------------

    prompt = f"""
You are a senior business intelligence analyst.

Generate a UNIQUE, NON-REPETITIVE insight for this business.

Do NOT reuse sentence structures from previous responses.
Do NOT sound generic or templated.

BUSINESS INFORMATION:
Name: {name}
Category: {categories}
Location: {city}
Rating: {stars}
Number of Reviews: {reviews}

ANALYSIS TASK:
Write 3–5 sentences covering:

1. What this business is likely best known for
2. What its rating and review count suggest about real customer experience
3. What type of customers it attracts
4. One unique business insight or interpretation (very important)

STYLE:
- Human-like writing
- Analytical tone
- Specific to this business only
- No repetition
- No filler phrases like "this business offers"

OUTPUT:
"""

    # -----------------------------------
    # GROQ API CALL
    # -----------------------------------

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # you can switch to llama3-8b-8192 for speed
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert business analyst. "
                    "You write sharp, non-repetitive, insightful business reports."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.9,
        max_tokens=220
    )

    return response.choices[0].message.content
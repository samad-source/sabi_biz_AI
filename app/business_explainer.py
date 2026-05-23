import random

def generate_business_explanation(row):

    name = row["name"]
    stars = row["stars"]
    reviews = row["review_count"]
    categories = str(row["categories"])

    # -----------------------------------
    # CUISINE DETECTION
    # -----------------------------------

    if "African" in categories:
        cuisine = "African cuisine"
    elif "Italian" in categories:
        cuisine = "Italian food"
    elif "Pizza" in categories:
        cuisine = "pizza spots"
    elif "Coffee" in categories or "Cafe" in categories:
        cuisine = "cafes and coffee"
    else:
        cuisine = "restaurant experiences"

    # -----------------------------------
    # POPULARITY
    # -----------------------------------

    if reviews > 300:
        popularity = "very popular among customers"
    elif reviews > 100:
        popularity = "well-reviewed by many customers"
    else:
        popularity = "a hidden gem with loyal customers"

    # -----------------------------------
    # SENTIMENT
    # -----------------------------------

    if stars >= 4.5:
        sentiment = "Customers highly praise the experience."
    elif stars >= 4:
        sentiment = "Most customers leave satisfied reviews."
    else:
        sentiment = "Reviews are mixed depending on expectations."

    # -----------------------------------
    # VARIATION BANK (THIS IS THE KEY FIX)
    # -----------------------------------

    intro_variations = [
        f"{name} is known for {cuisine}.",
        f"{name} specializes in {cuisine}.",
        f"You’ll find {cuisine} at {name}.",
        f"{name} offers a strong focus on {cuisine}.",
        f"A popular choice for {cuisine}, {name} stands out locally."
    ]

    popularity_variations = [
        f"It is {popularity}.",
        f"This place is considered {popularity}.",
        f"Locals describe it as {popularity}.",
        f"Customer traffic shows it is {popularity}."
    ]

    sentiment_variations = [
        sentiment,
        f"In general, {sentiment.lower()}",
        f"Overall, {sentiment.lower()}",
        f"Feedback suggests that {sentiment.lower()}"
    ]

    insight_extra = [
        "It tends to attract repeat customers.",
        "It is often recommended by locals.",
        "It has a strong community presence.",
        "It is a go-to spot for nearby residents.",
        "It maintains consistent service quality."
    ]

    # -----------------------------------
    # BUILD FINAL OUTPUT RANDOMLY
    # -----------------------------------

    explanation = " ".join([
        random.choice(intro_variations),
        random.choice(popularity_variations),
        random.choice(sentiment_variations),
        random.choice(insight_extra)
    ])

    return explanation
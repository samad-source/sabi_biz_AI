def generate_business_explanation(row):

    import random

    name = row["name"]
    stars = row["stars"]
    reviews = row["review_count"]
    categories = str(row["categories"])

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

    if reviews > 300:
        popularity = "very popular among customers"
    elif reviews > 100:
        popularity = "well-reviewed by many customers"
    else:
        popularity = "a hidden gem with loyal customers"

    if stars >= 4.5:
        sentiment = "Customers highly praise the experience."
    elif stars >= 4:
        sentiment = "Most customers leave satisfied reviews."
    else:
        sentiment = "Reviews are mixed depending on expectations."

    intro_templates = [
        f"{name} specializes in {cuisine}.",
        f"You’ll find {cuisine} at {name}.",
        f"{name} offers a strong focus on {cuisine}."
    ]

    popularity_templates = [
        f"It is {popularity}.",
        f"This place is considered {popularity}.",
        f"Locals describe it as {popularity}."
    ]

    sentiment_templates = [
        sentiment,
        f"In general, {sentiment.lower()}",
        f"Overall, customers say that {sentiment.lower()}"
    ]

    explanation = " ".join([
        random.choice(intro_templates),
        random.choice(popularity_templates),
        random.choice(sentiment_templates)
    ])

    return explanation
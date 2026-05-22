def generate_business_explanation(row):

    name = row["name"]
    stars = row["stars"]
    reviews = row["review_count"]
    categories = str(row["categories"])

    # -----------------------------------
    # Detect dining style
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
    # Popularity analysis
    # -----------------------------------

    if reviews > 300:

        popularity = (
            "very popular among customers"
        )

    elif reviews > 100:

        popularity = (
            "well-reviewed by many customers"
        )

    else:

        popularity = (
            "a hidden gem with loyal customers"
        )

    # -----------------------------------
    # Rating sentiment
    # -----------------------------------

    if stars >= 4.5:

        sentiment = (
            "Customers highly praise the experience."
        )

    elif stars >= 4:

        sentiment = (
            "Most customers leave satisfied reviews."
        )

    else:

        sentiment = (
            "Reviews are mixed depending on expectations."
        )

    # -----------------------------------
    # Final explanation
    # -----------------------------------

    explanation = (
        f"{name} is known for {cuisine}. "
        f"It is {popularity}. "
        f"{sentiment}"
    )

    return explanation
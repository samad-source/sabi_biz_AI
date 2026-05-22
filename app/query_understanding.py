import re # pyright: ignore[reportUnusedImport]


def extract_query_entities(query: str):

    query = query.lower()

    # -----------------------------------
    # COMMON CITIES
    # -----------------------------------

    cities = [
        "tucson",
        "philadelphia",
        "tampa",
        "nashville",
        "new orleans",
        "vegas",
        "houston",
        "phoenix",
        "los angeles",
        "new york"
        "lagos"
        "nigeria"
        "ghana"
        "ethiopia"
    ]

    # -----------------------------------
    # COMMON FOOD TYPES
    # -----------------------------------

    cuisines = [
        "african",
        "nigerian",
        "ghanaian",
        "ethiopian",
        "italian",
        "pizza",
        "burger",
        "coffee",
        "cafe",
        "sushi",
        "chinese",
        "mexican"
        "indian"
        "Nightlife"
        "Cocktail Bars"
        " Halal"
        " Grocery"
    ]

    detected_city = None
    detected_cuisine = None

    # -----------------------------------
    # DETECT CITY
    # -----------------------------------

    for city in cities:

        if city in query:
            detected_city = city
            break

    # -----------------------------------
    # DETECT CUISINE
    # -----------------------------------

    for cuisine in cuisines:

        if cuisine in query:
            detected_cuisine = cuisine
            break

    return {
        "city": detected_city,
        "cuisine": detected_cuisine
    }


# -----------------------------------
# TEST
# -----------------------------------

if __name__ == "__main__":

    sample = "I need African restaurant in Tucson"

    result = extract_query_entities(sample)

    print(result)
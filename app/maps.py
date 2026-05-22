def generate_google_maps_link(
    latitude : float,
    longitude : float
):

    return (
        f"https://www.google.com/maps?q="
        f"{latitude},{longitude}"
    )
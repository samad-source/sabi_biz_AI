import streamlit as st

from app.search_engine import (
    recommend_from_query
)

from app.image_search import (
    get_business_image
)

from app.business_explainer import (
    generate_business_explanation
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Recommendation Agent",
    layout="wide"
)

# -----------------------------------
# CUSTOM STYLING
# -----------------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
    }

    .stButton > button {
        width:100%;
        border-radius:10px;
        height:3em;
        font-size:18px;
        font-weight:bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🎯 AI Recommendation Agent")

st.subheader(
    "Conversational AI Business Discovery"
)

# -----------------------------------
# SEARCH BOX
# -----------------------------------

query = st.text_input(
    "What are you looking for?",
    placeholder="African restaurant in Tucson"
)

# -----------------------------------
# BUTTON ACTION
# -----------------------------------

if st.button("🔍 Find Businesses"):

    # Empty search handling
    if query.strip() == "":

        st.warning(
            "Please enter a search query."
        )

    else:

        results = recommend_from_query(query)

        # -----------------------------------
        # NO RESULTS
        # -----------------------------------

        if results is None or len(results) == 0:

            st.error(
                "❌ No businesses found."
            )

        else:

            st.success(
                f"✅ {len(results)} recommendations found"
            )

            # -----------------------------------
            # LOOP THROUGH RESULTS
            # -----------------------------------

            for _, row in results.iterrows():

                st.divider()

                col1, col2 = st.columns([1,2])

                # ---------------------------
                # IMAGE COLUMN
                # ---------------------------

                with col1:

                    try:

                        image = get_business_image(
                            row["name"]
                        )

                        if image:

                            st.image(
                                image,
                                use_container_width=True
                            )

                    except:

                        pass

                # ---------------------------
                # INFO COLUMN
                # ---------------------------

                with col2:

                    st.subheader(
                        row["name"]
                    )

                    st.write(
                        f"⭐ Rating: {row['stars']}"
                    )

                    st.write(
                        f"📍 City: {row['city']}"
                    )

                    st.write(
                        f"📝 Reviews: {row['review_count']}"
                    )

                    st.write(
                        f"🏷️ Categories: {row['categories']}"
                    )

                    # -----------------------
                    # AI INSIGHT
                    # -----------------------

                    try:

                        insight = (
                            generate_business_explanation(
                                row
                            )
                        )

                        st.info(
                            f"🤖 AI Insight:\n\n{insight}"
                        )

                    except:

                        st.info(
                            "AI explanation unavailable."
                        )

                    # -----------------------
                    # MAP LINK
                    # -----------------------

                    maps_url = (
                        f"https://www.google.com/maps/search/"
                        f"{row['name']} {row['city']}"
                    )

                    st.markdown(
                        f"[📍 Open in Google Maps]({maps_url})"
                    )
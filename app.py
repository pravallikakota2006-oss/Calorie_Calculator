import streamlit as st

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Pravallika's Calorie Calculator",
    page_icon="🥗",
    layout="centered"
)

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */

    .stApp {
        background:
        linear-gradient(
            135deg,
            #0f2027,
            #203a43,
            #2c5364
        );
    }

    /* Main content width */

    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Button design */

    .stButton > button {
        width: 100%;
        border-radius: 15px;
        padding: 12px;
        font-size: 18px;
        font-weight: bold;

        background:
        linear-gradient(
            90deg,
            #00c6ff,
            #0072ff
        );

        color: white;
        border: none;
    }

    .stButton > button:hover {
        transform: scale(1.02);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🥗 Pravallika's Calorie Calculator")

st.write(
    "🔥 Discover your estimated daily calorie requirement!"
)

st.divider()

# --------------------------------------------------
# USER DETAILS
# --------------------------------------------------

st.header("👤 Enter Your Details")

name = st.text_input(
    "📝 Your Name"
)

age = st.number_input(
    "🎂 Age",
    min_value=1,
    max_value=100,
    value=20
)

gender = st.selectbox(
    "🚻 Gender",
    [
        "Female",
        "Male"
    ]
)

weight = st.number_input(
    "⚖️ Weight (kg)",
    min_value=1.0,
    max_value=300.0,
    value=60.0,
    step=0.5
)

height = st.number_input(
    "📏 Height (cm)",
    min_value=50.0,
    max_value=250.0,
    value=165.0,
    step=0.5
)

# --------------------------------------------------
# ACTIVITY LEVEL
# --------------------------------------------------

st.header("🏃 Activity Level")

activity = st.selectbox(
    "Choose your daily activity level",
    [
        "🛋️ Sedentary - Little or no exercise",
        "🚶 Lightly Active - Exercise 1-3 days/week",
        "🏃 Moderately Active - Exercise 3-5 days/week",
        "💪 Very Active - Exercise 6-7 days/week",
        "🔥 Extra Active - Very hard exercise or physical job"
    ]
)

# --------------------------------------------------
# CALCULATE BUTTON
# --------------------------------------------------

st.divider()

calculate = st.button(
    "🔥 CALCULATE MY CALORIES"
)

# --------------------------------------------------
# CALCULATION
# --------------------------------------------------

if calculate:

    # Check name

    if name.strip() == "":
        st.warning(
            "⚠️ Please enter your name first."
        )

    else:

        # ------------------------------------------
        # BMR CALCULATION
        # ------------------------------------------

        if gender == "Male":

            bmr = (
                10 * weight
                + 6.25 * height
                - 5 * age
                + 5
            )

        else:

            bmr = (
                10 * weight
                + 6.25 * height
                - 5 * age
                - 161
            )

        # ------------------------------------------
        # ACTIVITY MULTIPLIER
        # ------------------------------------------

        if "Sedentary" in activity:

            multiplier = 1.20

        elif "Lightly Active" in activity:

            multiplier = 1.375

        elif "Moderately Active" in activity:

            multiplier = 1.55

        elif "Very Active" in activity:

            multiplier = 1.725

        else:

            multiplier = 1.90

        # ------------------------------------------
        # DAILY CALORIE CALCULATION
        # ------------------------------------------

        daily_calories = bmr * multiplier

        # ------------------------------------------
        # RESULT
        # ------------------------------------------

        st.success(
            f"🎉 Hello {name}! Your calculation is ready."
        )

        st.divider()

        st.header("🔥 Your Calorie Result")

        st.metric(
            label="Estimated Daily Calories",
            value=f"{daily_calories:,.0f} kcal/day"
        )

        # ------------------------------------------
        # DETAILS
        # ------------------------------------------

        st.subheader("📊 Your Information")

        st.write(
            f"👤 **Name:** {name}"
        )

        st.write(
            f"🎂 **Age:** {age} years"
        )

        st.write(
            f"🚻 **Gender:** {gender}"
        )

        st.write(
            f"⚖️ **Weight:** {weight} kg"
        )

        st.write(
            f"📏 **Height:** {height} cm"
        )

        st.write(
            f"🏃 **Activity:** {activity}"
        )

        # ------------------------------------------
        # SIMPLE INTERPRETATION
        # ------------------------------------------

        st.divider()

        st.subheader("💡 Simple Interpretation")

        st.info(
            f"""
            Based on the information you entered,
            your estimated daily calorie requirement
            is approximately **{daily_calories:,.0f} kcal per day**.

            This is an estimate of the calories your body
            may need to maintain your current weight
            based on your activity level.
            """
        )

        st.caption(
            "⚠️ This calculator provides an estimate and "
            "is not medical advice."
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "🥗 Calorie Calculator | "
    "Python + Streamlit | Created by Pravallika"
)
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# =========================
# PAGE TITLE
# =========================

st.title("🏥 Public Health Resource Assistant")
st.markdown("""
Welcome to the Public Health Resource Assistant.

This tool helps students and community members identify health and wellness resources based on their needs.

Examples:
- I need mental health support
- Where can I get STI testing?
- I need a doctor
- I need diatary assistance
- I need crisis support
""")

with st.sidebar:

    st.header("About")

    st.write("""
    Built by Rebecca Cazarin

    Tools Used:
    - Python
    - Streamlit
    - Pandas
    - Data Analysis

    This application connects University of South Carolina students and staff with health resources found on campus and in the community.
    """)

    st.info(
        "This application is informational only and is not medical advice."
    )
# =========================
# LOAD RESOURCE DATA
# =========================

resources = pd.read_csv(
    "USC Health and Wellness Resources(csv).csv",
    encoding="latin1"
)

# Remove extra spaces from column names
resources.columns = resources.columns.str.strip()

# =========================
# USER QUESTION
# =========================

user_question = st.text_input(
    "How can I help you today?"
)

# =========================
# SEARCH RESOURCES
# =========================

if user_question:

    question = user_question.lower()

    matching_resources = pd.DataFrame()

    if (
        "mental" in question
        or "anxiety" in question
        or "depression" in question
        or "sad" in question
    ):

        matching_resources = resources[
            resources["Category"].str.contains(
                "Mental Health",
                case=False,
                na=False
            )
        ]

    elif (
        "crisis" in question
        or "suicide" in question
        or "emergency" in question
        or "bad problem" in question
        or "not okay" in question
        or "really bad" in question
        or "sad" in question
        or "kms" in question
        or "kill myself" in question
        or "seeing things" in question
        or "hallucinations" in question
        or "hallucinating" in question
        or "lost" in question
        or "alone" in question
        or "hearing things" in question
        or "voices" in question
        or "demons" in question
        or "demon" in question
        or "can't stop" in question
        or "worry" in question
        or "obsess" in question
        or "obsessive" in question
        or "obsessing" in question
        or "obsessed" in question
        or "racing" in question
    ):

        matching_resources = resources[
            resources["Category"].str.contains(
                "Crisis",
                case=False,
                na=False
            )
        ]

    elif (
        "sti" in question
        or "sexual" in question
        or "sex" in question
        or "gave me something" in question
        or "got something" in question
        or "burning" in question
        or "itching" in question
        or "discharge" in question
        or "itchy" in question
        or "spot" in question
        or "penis" in question
        or "vagina" in question
        or "cunt" in question
        or "pussy" in question
        or "dick" in question
        or "cock" in question
        or "vajayjay" in question
        or "lady bits" in question
        or "privates" in question
        or "twat" in question
        or "vag" in question
        or "anus" in question
        or "butthole" in question
        or "butt" in question
        or "starfish" in question
        or "ass" in question
        or "asshole" in question
        or "pubes" in question
        or "pubic hair" in question
        or "pregnant" in question
        or "pregnancy" in question
        or "baby" in question
        or "knocked up" in question
        or "late" in question
        or "period" in question
        or "pap" in question
        or "bathroom" in question
        or "sting" in question
        or "stinging" in question
        or "pain" in question
    ):

        matching_resources = resources[
            resources["Category"].str.contains(
                "Sexual Health",
                case=False,
                na=False
            )
        ]

    elif (
        "doctor" in question
        or "primary care" in question
        or "vomiting" in question
        or "nausea" in question
        or "diarrhea" in question
        or "puke" in question
        or "hurl" in question
        or "headache" in question
        or "constipation" in question
        or "ache" in question
        or "stuffy" in question
        or "fever" in question
        or "rash" in question
        or "temperature" in question
        or "temp" in question
        or "refill" in question
        or "meds" in question
        or "medication" in question
        or "cough" in question
        or "flu" in question
        or "sinus" in question
        or "allergy" in question
        or "allergies" in question
        or "pregnant" in question
        or "pregnancy" in question
        or "baby" in question
        or "knocked up" in question
        or "late" in question
        or "period" in question
        or "pap" in question
        or "bathroom" in question
    ):

        matching_resources = resources[
            resources["Category"].str.contains(
                "Primary Care",
                case=False,
                na=False
            )
        ]

    elif (
        "nutrition" in question
        or "diet" in question
        or "hungry" in question
        or "starving" in question
        or "eat" in question
        or "food" in question
        or "vitamin" in question
        or "gluten" in question
        or "vegetarian" in question
        or "vegan" in question
        or "paleo" in question
        or "protein" in question
        or "carbs" in question
        or "carbohydrates" in question
        or "sugar" in question
    ):

        matching_resources = resources[
            resources["Category"].str.contains(
                "Nutrition",
                case=False,
                na=False
            )
        ]
    # Display results

    if matching_resources.empty:

        st.info(
            "I couldn't find matching resources. Try words like mental health, STI testing, crisis, doctor, or diet."
        )

    else:

        st.subheader("Recommended Resources")

        resource_text = matching_resources.to_string(index=False)

        prompt = f"""
        You are a helpful Public Health Resource Assistant.

        The user asked:

        {user_question}

        The following resources are available:

        {resource_text}

        Respond in a warm, professional, easy-to-understand way.

        For each resource explain:
        - what the service is
        - why it may help
        - phone number
        - website

        Only use the provided resources.
        Do not provide medical advice.
        """

        try:

            response = model.generate_content(prompt)

            st.write(response.text)

            with st.expander("View Source Information"):
                st.dataframe(matching_resources)

        except Exception as e:

            st.error(
                f"Gemini Error: {e}"
            )
# =========================
# DISCLAIMER
# =========================

st.warning(
    "⚠️ This tool is for informational purposes only and is not medical advice. If you are experiencing an emergency, call 911 or 988."
)

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
- I need nutrition assistance
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
            "I couldn't find matching resources. Try words like mental health, STI testing, crisis, doctor, or nutrition."
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
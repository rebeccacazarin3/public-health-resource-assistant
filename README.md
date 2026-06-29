Public Health Resource Assistant - University of South Carolina Students and Staff Resources

## Overview

The Public Health Resource Assistant is an AI-powered web application designed to connect users with health and wellness resources through natural language interactions.
Built using Python, Streamlit, and Google's Gemini API, the application allows users to ask questions in plain language (e.g., "I need mental health support" or "Where can I get STI testing?") and receive relevant health resource recommendations.
This project was developed to explore how generative AI can improve access to public health information and support individuals in locating community resources more efficiently.
---

## Motivation

Accessing health resources can be challenging, particularly when individuals are uncertain about what services they need or where to begin searching.

The goal of this project is to demonstrate how conversational AI can:

* Improve access to health and wellness resources.
* Simplify navigation of community services.
* Provide users with information in a user-friendly format.
* Support public health and social-impact initiatives through technology.

This project also demonstrates the responsible use of generative AI by incorporating crisis detection and safety messaging.
---

## Features

### Current Features

* Natural language user input.
* Resource matching based on health-related keywords.
* AI-generated explanations using Gemini.
* Crisis keyword detection with emergency guidance.
* Interactive web interface built with Streamlit.
* Expandable source information table displaying matched resources.
* User-friendly recommendations presented in conversational language.

### Example User Questions

* "I need mental health support."
* "Where can I get STI testing?"
* "I need crisis support."
* "I need a doctor."
* "I need nutrition help."
---

## Technology Stack

### Languages

* Python

### Libraries and Frameworks

* Streamlit
* Pandas
* Google Generative AI SDK
* python-dotenv

### AI Model

* Google Gemini

### Development Tools

* Visual Studio Code
* Git
* GitHub
---

## Application Workflow

1. A user enters a health-related question.
2. The application converts the input to lowercase and searches for keywords.
3. Relevant resources are identified from the resource dataset.
4. Matching resources are converted into structured text.
5. The Gemini model generates a conversational response using only the provided resources.
6. The application displays:

   * AI-generated recommendations
   * Resource details
   * Source information
7. If crisis-related language is detected, the application displays emergency support guidance.
---

## Responsible AI Considerations

This project incorporates several responsible AI practices:

* The AI model is instructed to use only information contained within the resource dataset.
* The application does not provide medical advice.
* Crisis-related keywords trigger emergency support messaging directing users to 911 or 988.
* Users are informed that the tool is for informational purposes only.
---

## Project Structure

```text
public-health-resource-assistant/
│
├── app.py
├── resources.csv
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

### File Descriptions

| File             | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| app.py           | Main Streamlit application                                  |
| resources.csv    | Dataset containing health and wellness resources            |
| requirements.txt | Python package dependencies                                 |
| .gitignore       | Prevents sensitive or unnecessary files from being uploaded |
| README.md        | Project documentation                                       |
---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/public-health-resource-assistant.git
```

### Navigate to the Project Folder

```bash
cd public-health-resource-assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root and add:

```text
GEMINI_API_KEY=your_api_key_here
```

Obtain a Gemini API key from Google AI Studio.

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will typically be available at:

```text
http://localhost:8501
```

## Future Enhancements

Potential improvements include:

* Semantic search using embeddings.
* Support for multiple resource categories simultaneously.
* Geographic filtering based on user location.
* Conversation history and memory.
* Resource recommendation ranking.
* User feedback collection.
* Additional responsible AI safeguards.
* Expanded public health datasets.
---

## Skills Demonstrated

This project demonstrates experience with:

* Generative AI application development
* Large Language Model integration
* Prompt engineering
* Streamlit application development
* Data processing with Pandas
* Responsible AI practices
* End-to-end project development
* Debugging and troubleshooting
* User-centered design
* Technical documentation
---

## Disclaimer

This application is intended for informational purposes only and does not provide medical advice, diagnosis, or treatment.
If you are experiencing a medical emergency or thoughts of self-harm, call 911 or 988 immediately.
---

## Author

Rebecca Cazarin

LinkedIn: https://www.linkedin.com/in/rebecca-cazarin/    
GitHub: https://github.com/rebeccacazarin3

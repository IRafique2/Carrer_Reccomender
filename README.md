# AI Career Recommendation Tool

Welcome to the **AI Career Recommendation Tool**. This tool, hosted on [Hugging Face Spaces](https://huggingface.co/spaces/iRafique/Carrer_Recommendation), provides tailored career, educational recommendations, and personalized feedback based on your undergraduate course, specialization, interests, skills, and certifications. It leverages the power of Anthropic's Claude language model to offer insightful suggestions.

## Features

- **Career Recommendations**: Based on your academic background, interests, and skills.
- **Educational Recommendations**: Provides suggestions for further education and skill development.
- **Personalized Feedback**: Offers individualized feedback to guide your career path.

## How to Use

1. **Visit the Tool**: Open the application at [this link](https://huggingface.co/spaces/iRafique/Carrer_Recommendation).
2. **Input Your Details**: 
   - Select your **Undergraduate Course** from the dropdown menu.
   - Choose your **UG Specialization (Major Subject)**.
   - Select your **Interests** and **Skills** from the available options.
   - Enter any **Certifications** you have obtained.
3. **Generate Recommendations**: Click the "Generate Career Recommendation" button in the sidebar.
4. **Receive Results**: The tool will display tailored career and educational recommendations, along with personalized feedback.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **Anthropic Claude API**: For generating personalized career recommendations using AI.
- **Python**: Used for scripting the logic and API integration.
- **Hugging Face Spaces**: For hosting the web app.


## Getting Started

1. Clone the repository or download the code files from the Hugging Face Space.
2. Ensure that you have Python installed and the necessary dependencies (`streamlit`, `requests`).
3. Run the application locally by executing the following command:
   ```bash
   streamlit run app.py
   ```
4. Set your **Anthropic Claude API Key** in the `api_key` field within the application.

## Dependencies

To install the required Python packages, use the following command:

```bash
pip install streamlit requests
```

## API Integration

This tool uses **Anthropic Claude's API** for natural language processing. Ensure you have an API key from Anthropic to make requests.


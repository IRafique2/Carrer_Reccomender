import streamlit as st
import requests

# Function to get career recommendations from Claude
def get_career_recommendations(api_key, undergraduate_course, ug_specialization, interests, skills, certifications):
    url = "https://api.anthropic.com/v1/complete"
    prompt = f"""
Human: I am providing the following details about myself:
- Undergraduate Course: {undergraduate_course}
- UG Specialization: {ug_specialization}
- Interests: {interests}
- Skills: {skills}
- Certifications: {certifications}

Please provide:
1. Career Recommendations
2. Educational Recommendations
3. Personalized Feedback

Assistant:"""
    data = {
        "prompt": prompt,
        "model": "claude-v1",
        "max_tokens_to_sample": 300,
        "stop_sequences": ["\n\nHuman:"],
    }
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json",
        "anthropic-version": "2023-01-01"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        response_data = response.json()
        completion = response_data.get("completion", "")
        return completion
    else:
        return f"Error: {response.status_code} - {response.text}"

st.title("AI Career Recommendation")
st.write("""
Welcome to the AI Career Recommendation Tool. This tool provides tailored career and educational recommendations. Provide your details below to receive guidance.
""")

st.sidebar.title("Input Your Details")
# Example lists for dropdown and multiselect options
courses = ["B.Sc", "B.S", "B.E", "BA", "MBA", "B.Tech", "MCA", "B.Com", "BCA.LLB", "B.Pharm", "Others"]
specializations = ["Computer Applications", "Computer Science Engineering", "Psychology", "Commerce", "Instrumentation Engineering", "Business Administration", "Information Technology", "Electrical Engineering", "Mechanical Engineering", "Economics", "Physics", "Chemistry", "Biological science", "Sociology", "Others"]
interest_list = ["Cloud computing", "Technology", "Understand human behaviour", "Sales/Marketing; Trading", "Data analytics", "Financial Analysis; Research", "Web development", "Teaching", "Entrepreneurship", "Social Justice", "Design", "Digital marketing", "Game industry", "Blockchain", "Social causes", "Urban Planning", "Sports Industry", "Content Writing", "Research", "Others"]
skills_list = ["Python; Data Science; Java", "Critical Thinking", "Analytic Thinking", "SQL", "Programming", "People management", "Communication skills", "Accounting Skills", "Critical Thinking", "Data Visualization skills (Power Bi/ Tableau)", "Editing", "Project Management", "Problem Solving skills", "Analytical Skills", "AI", "Java", "SQL", "C++", "R", "Linux", "Others"]

# Dropdown menus
undergraduate_course = st.sidebar.selectbox("Undergraduate Course", courses)
ug_specialization = st.sidebar.selectbox("UG Specialization (Major Subject)", specializations)
# Multiselects
interests = st.sidebar.multiselect("Interests", interest_list)
skills = st.sidebar.multiselect("Skills", skills_list)
# Text input
certifications = st.sidebar.text_input("Certifications")

api_key = "#your key"
if st.sidebar.button("Generate Career Recommendation"):
    recommendations = get_career_recommendations(
        api_key,
        undergraduate_course,
        ug_specialization,
        interests,
        skills,
        certifications
    )
    if recommendations:
        recommendations = recommendations.replace("Career Recommendations:", "Career Recommendations:").replace("Educational Recommendations:", "Educational Recommendations:").replace("Personalized Feedback:", "Personalized Feedback:")
        st.write("### **Career Recommendations:**")
        st.write(recommendations.split("Educational Recommendations:")[0].strip())
        st.write("### **Educational Recommendations:**")
        st.write(recommendations.split("Educational Recommendations:")[1].split("Personalized Feedback:")[0].strip())
        st.write("### **Personalized Feedback:**")
        st.write(recommendations.split("Personalized Feedback:")[1].strip())
    else:
        st.write(f"An error occurred: {recommendations}")

# Additional styling
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 5px;
    }
    .stTextInput>label, .stSelectbox>label, .stMultiselect>label {
        font-size: 16px;
        font-weight: bold;
    }
    .stSidebar>div:first-child {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    h3 {
        color: #2E86C1;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

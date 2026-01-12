import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from content_generator import ContentGenerator
from example_generator import ExampleGenerator
from quiz_generator import QuizGenerator

st.set_page_config(
    page_title="AI Study Material Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


@st.cache_resource
def load_generators():
    return {
        "content": ContentGenerator(),
        "example": ExampleGenerator(),
        "quiz": QuizGenerator()
    }


generators = load_generators()

st.title("AI Study Material Generator")
st.write("Structured explanation • Difficulty-specific content • Real-world examples • Quiz")

topic = st.text_input("Topic", placeholder="e.g., Machine Learning, Photosynthesis")
level = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

col_generate, col_examples, col_quiz = st.columns([2, 1, 1])

with col_generate:
    generate_button = st.button("Generate Study Material")

with col_examples:
    show_examples = st.checkbox("Include Examples", value=True)

with col_quiz:
    show_quiz = st.checkbox("Include Quiz", value=True)

if generate_button:
    if not topic.strip():
        st.error("Please enter a topic.")
    else:
        content = generators["content"].generate_content(topic, level)
        examples = generators["example"].generate_examples(topic, level) if show_examples else ""
        quiz_data = generators["quiz"].generate_quiz(topic, level) if show_quiz else []

        st.session_state.study_material = {
            "topic": topic,
            "level": level,
            "content": content,
            "examples": examples,
            "quiz": quiz_data,
        }

if "study_material" in st.session_state:
    data = st.session_state.study_material

    st.subheader(f"{data['topic']} ({data['level']})")

    st.markdown("### 📝 Structured Explanation")
    st.write(data["content"])

    st.markdown("### 💡 Real-World Examples")
    if data["examples"]:
        st.info(data["examples"])
    else:
        st.info("Examples not generated. Enable them above.")

    st.markdown("### ❓ Quiz")
    if data["quiz"]:
        for i, q in enumerate(data["quiz"], 1):
            st.markdown(f"**Question {i}:** {q['question']}")

            user_answer = st.radio(
                f"Select your answer for Q{i}",
                options=q["options"],
                key=f"q_{i}"
            )

            if st.button(f"Check Q{i}", key=f"check_{i}"):
                if q["options"].index(user_answer) == q["correct"]:
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. Correct answer: {q['options'][q['correct']]}")

                if "explanation" in q:
                    st.info(q["explanation"])

            st.divider()
    else:
        st.info("Quiz not generated. Enable it above.")
else:
    st.info("Enter a topic, choose difficulty, and click 'Generate Study Material'.")

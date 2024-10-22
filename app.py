# Install necessary libraries
!pip install streamlit -q
!pip install pyngrok -q

import streamlit as st
from pyngrok import ngrok

# Important Physics MCQs data
physics_mcqs = [
    {
        "question": "What is the SI unit of force?",
        "choices": ["Joule", "Newton", "Pascal", "Watt"],
        "answer": "Newton"
    },
    {
        "question": "Who proposed the law of universal gravitation?",
        "choices": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "James Clerk Maxwell"],
        "answer": "Isaac Newton"
    },
    {
        "question": "What is the speed of light in vacuum?",
        "choices": ["3 × 10^8 m/s", "3 × 10^6 m/s", "3 × 10^4 m/s", "3 × 10^2 m/s"],
        "answer": "3 × 10^8 m/s"
    },
    {
        "question": "Which law explains the relation between current and potential difference?",
        "choices": ["Faraday's Law", "Ohm's Law", "Hooke's Law", "Ampere's Law"],
        "answer": "Ohm's Law"
    },
    {
        "question": "Which particle has a negative charge?",
        "choices": ["Proton", "Neutron", "Electron", "Positron"],
        "answer": "Electron"
    }
]

# Function to display MCQs and provide solutions
def display_mcqs():
    score = 0
    for i, mcq in enumerate(physics_mcqs):
        st.write(f"Q{i+1}: {mcq['question']}")
        answer = st.radio("Choose your answer:", mcq["choices"], key=i)
        if st.button(f"Submit Answer {i+1}"):
            if answer == mcq['answer']:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Incorrect. The correct answer is {mcq['answer']}")
        st.write("---")
    
    if st.button("Show Final Score"):
        st.write(f"Your Score: {score}/{len(physics_mcqs)}")

# Streamlit App
st.title("Physics MCQs App")
st.subheader("Created by Majid Ali")
st.write("Test your Physics knowledge with these important MCQs and solutions!")

display_mcqs()

# Launch ngrok to make app accessible externally
public_url = ngrok.connect(port='8501')
st.write(f"App is live at {public_url}")


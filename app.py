import streamlit as st

# Define important MCQs and their solutions
mcqs = [
    {
        "question": "What is the SI unit of force?",
        "choices": ["Joule", "Newton", "Pascal", "Watt"],
        "answer": "Newton"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    }
]

# Function to display MCQs and check answers
def display_mcqs():
    score = 0
    for i, mcq in enumerate(mcqs):
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
        st.write(f"Your Score: {score}/{len(mcqs)}")

# Streamlit app setup
st.title("Physics MCQs App by Majid Ali")
st.write("Test your knowledge with important MCQs and see the solutions!")

display_mcqs()

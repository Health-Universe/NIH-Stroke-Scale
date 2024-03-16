import streamlit as st

def calculate_nihss_score(answers):
    # Simple function to calculate the total NIHSS score based on user inputs
    return sum(answers)

def main():
    st.title('NIH Stroke Scale/Score (NIHSS) Calculator')

    st.markdown("""
    This app is designed for healthcare professionals to quickly calculate the NIH Stroke Scale/Score (NIHSS) for their patients. The NIHSS is a measure used to quantify the impairment caused by a stroke.
    """)

    # Example categories - extend this with all NIHSS items for a complete tool
    q1 = st.selectbox('1a. Level of Consciousness:', (0, 1, 2, 3), format_func=lambda x: f"{x} - {'Normal' if x == 0 else 'Abnormal'}")
    q2 = st.selectbox('1b. Level of Consciousness Questions:', (0, 1, 2), format_func=lambda x: f"{x} - {'Answers both correctly' if x == 0 else 'Answers one correctly or none'}")
    q3 = st.selectbox('1c. Level of Consciousness Commands:', (0, 1, 2), format_func=lambda x: f"{x} - {'Performs both tasks correctly' if x == 0 else 'Performs one correctly or none'}")
    # Add more questions here...

    # Collect answers in a list
    answers = [q1, q2, q3]  # Extend this list with all your questions' variables

    if st.button('Calculate NIHSS Score'):
        score = calculate_nihss_score(answers)
        st.subheader(f'Total NIHSS Score: {score}')
        st.markdown("""
        **Score Interpretation:**
        - 0: No stroke symptoms
        - 1-4: Minor stroke
        - 5-15: Moderate stroke
        - 16-20: Moderate to severe stroke
        - 21-42: Severe stroke
        """)

if __name__ == "__main__":
    main()

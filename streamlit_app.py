import streamlit as st
import random

def generate_question(limit_to_100_percent):
    while True:
        numerator = random.randint(1, 11)
        denominator = random.randint(1, 11)
        if not limit_to_100_percent or (numerator / denominator) * 100 <= 100:
            return numerator, denominator

def main():
    st.title('Division Table Game')

    limit_to_100_percent = st.checkbox('Limit to 100%')

    numerator, denominator = generate_question(limit_to_100_percent)

    st.markdown(f'**{numerator}** / **{denominator}**')

    answer = st.text_input('Enter the result:')
    if st.button('Check'):
        try:
            user_answer = float(answer)
            correct_answer = (numerator / denominator) * 100
            if user_answer == round(correct_answer, 1):
                st.success('Correct!')
            else:
                st.error(f'Incorrect. The correct answer is {correct_answer:.1f}%.')

            numerator, denominator = generate_question(limit_to_100_percent)
            st.markdown(f'**{numerator}** / **{denominator}**')
            answer = ''  # Clear the answer text field
        except ValueError:
            st.error('Please enter a valid number.')

if __name__ == "__main__":
    main()

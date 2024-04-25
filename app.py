import streamlit as st
from openai import OpenAI

##key
OPENAI_KEY = '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'
client = OpenAI(api_key=OPENAI_KEY)


st.header("AI CODE REVIWER!!!")
st.subheader("This AI is trained to review PYTHON Code.")
user_prompt = st.text_area("[Enter your Python code: ]")
system_prompt ='''
    verify the given code and if it is incorrect, show the errors with the correct code
'''
if st.button("Code Review"):
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=1,
        max_tokens=3800,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    st.write(response.choices[0].message.content)
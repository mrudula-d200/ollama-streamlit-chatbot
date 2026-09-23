import streamlit as st
st.write("Hello, Streamlit!")
while True:
    user_input = st.text_input("you")
    if user_input=="exit":
        st.write("goodbye")
        break
    else:
        response=ollama.chat(
        model='llama3.2:3b',
        messages=[
            {"role":"user",
            "content":user_input}
    ]
    )
    st.write(response["message"]['content'])
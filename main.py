import streamlit as st
import langchain_helper

st.title("Restaurant Name Generator")
st.caption("_Note_ : The site uses Google's FLAN LLM for generations which isn't the best model available right now. One can expect better results with OpenAI's GPT models.")
st.divider()
with st.sidebar:
    api_key = st.text_input("Input your HuggingFace Hub API key here", key='api_key', placeholder="Enter here", type="password")
    cuisine = st.selectbox("Pick a Cuisine", ("American", "Indian", "Mexican", "Arabic", "Italian"), index=None, placeholder="Choose an option")

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine=cuisine, api_key=api_key)
    st.header(f"Restaurant Name: {response['restaurant_name']}")
    menu_items = response["menu_items"].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item)




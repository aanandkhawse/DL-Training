import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello, Streamlit")
st.write("This is my first Streamlit app")
st.text("Let's get started")

name = st.text_input("Enter your name:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.line_chart(df)
st.bar_chart(df)

upload_file = st.file_uploader("Upload a CSV", type="csv")
if upload_file is not None:
    uploaded_df = pd.read_csv(upload_file)
    st.dataframe(uploaded_df)

st.title("Text and Markdown Demo")
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, `code`, [link](https://streamlit.io)")
st.code("for i in range(5):\n    print(i)", language="python")

st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show details"):
    st.info("Here are your details")

option = st.radio("Choose view", ["Show chart", "Show table"])
if option == "Show chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")
    if submitted:
        st.success(f"Welcome, {username}!")

st.image(
    "https://picjumbo.com/wp-content/uploads/beautiful-nature-wallpaper-spring-flowers-mountain-sunset-free-image.jpg",
    caption="Sample image",
    use_container_width=True,
)
st.video("https://www.youtube.com/watch?v=wGOn7hDb3gk")

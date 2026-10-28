"""A beginner-friendly Streamlit demo covering common UI components and data display."""

import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Streamlit Learning Demo", page_icon="📊", layout="wide")

st.title("Streamlit Learning Demo")
st.caption("A hands-on collection of beginner examples for interactive Python apps.")

with st.sidebar:
    st.header("Demo navigation")
    st.write("Explore the examples below: inputs, charts, CSV upload, and forms.")

st.header("1. Greeting")
name = st.text_input("What's your name?", placeholder="Enter your name")
if st.button("Greet me", type="primary"):
    if name.strip():
        st.success(f"Hello, {name.strip()}!")
    else:
        st.warning("Enter your name first.")

st.header("2. Sample charts")
rng = np.random.default_rng(42)
chart_data = pd.DataFrame(rng.normal(size=(10, 2)), columns=["Series A", "Series B"])
left, right = st.columns(2)
with left:
    st.subheader("Line chart")
    st.line_chart(chart_data)
with right:
    st.subheader("Bar chart")
    st.bar_chart(chart_data)

st.header("3. Upload and preview a CSV")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
if uploaded_file is not None:
    try:
        uploaded_data = pd.read_csv(uploaded_file)
        st.success(f"Loaded {len(uploaded_data):,} rows and {len(uploaded_data.columns):,} columns.")
        st.dataframe(uploaded_data, use_container_width=True)
    except (pd.errors.ParserError, UnicodeDecodeError, ValueError) as error:
        st.error(f"Could not read this CSV file: {error}")

st.header("4. Common input widgets")
col1, col2 = st.columns(2)
with col1:
    st.text_area("Write a note", placeholder="Type something here...")
    st.number_input("Choose a number", min_value=0, max_value=100, value=25)
    st.slider("Choose a range", min_value=0, max_value=100, value=(20, 80))
with col2:
    st.selectbox("Choose a fruit", ["Apple", "Banana", "Mango"])
    st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
    st.radio("Choose a view", ["Chart", "Table"], horizontal=True)
    if st.checkbox("Show extra details"):
        st.info("This message appears when the checkbox is selected.")

st.header("5. Form example")
with st.form("profile_form"):
    username = st.text_input("Username")
    submitted = st.form_submit_button("Submit")
    if submitted:
        if username.strip():
            st.success(f"Welcome, {username.strip()}!")
        else:
            st.warning("Please enter a username.")

st.header("6. Markdown and code")
st.markdown("Use **bold text**, *italic text*, and links such as [Streamlit](https://streamlit.io).")
st.code("for number in range(5):\n    print(number)", language="python")

st.header("7. Video example")
st.video("https://www.youtube.com/watch?v=wGOn7hDb3gk")

st.divider()
st.caption("Learning demo • Built with Python, Streamlit, Pandas, and NumPy")

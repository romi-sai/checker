import os
import streamlit as st

st.set_page_config(page_title="Checker Home", page_icon="⭐️")

st.title('Dead Link Checker Website.')
st.sidebar.success('Please choose an option from the navigation bar above.')

st.subheader('About Us... ')
st.write('This website aims to find all of the deadlinks from a url provided by the user.')
st.write('It uses a recursive method to find the deadlinks, diving deep into the website from the provided depth value by the user.')

st.write('NEXT STOP: Please go to the Instructions option below to know how the Deadlink Checker works!')

# Get a list of all Python files in the 'pages' directory
page_files = [f for f in os.listdir("checker/pages") if f.endswith(".py")]

# Run each page file
for page_file in page_files:
    # Import the page module dynamically
    page_module = __import__(f"deadlinkchecker.pages.{page_file[:-3]}", fromlist=["*"])
    # Run the page module's main function if it exists
    if hasattr(page_module, "main"):
        page_module.main()

import streamlit as st
from auto_script_writer import main

st.title("Automated YouTube Script Generator")

if st.button("Generate Scripts"):
    st.write("Generating scripts... Please wait.")
    main()
    st.success("✅ Scripts generated and saved in Google Docs!")

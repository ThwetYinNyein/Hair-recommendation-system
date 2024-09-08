# sidebar_style.py

import streamlit as st

def apply_sidebar_style():
    sidebar_style = """
    <style>
    .sidebar .sidebar-content {
        padding-top: 0;
    }
    .sidebar .sidebar-content h1 {
        font-size: 32px;
        margin-bottom: 20px;
    }
    </style>
    """
    st.markdown(sidebar_style, unsafe_allow_html=True)

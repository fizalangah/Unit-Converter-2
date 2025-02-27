import streamlit as st;
from pint import UnitRegistry;

ureg =  UnitRegistry()

st.markdown(
    """
    <style>
    /* Change the background color of the entire app */
    .stApp {
        background-color: lightblue;
        color: black; /* Text color */
        font-family: 'Georgia', serif; /* Change font to serif */
    }

    /* Style the input field */
    .stNumberInput input {
        background-color: white !important;
        color: black !important;
        font-family: 'Arial', sans-serif; /* Change font for input field */
    }

    /* Style the dropdown menus */
    .stSelectbox select {
        background-color: white !important;
        color: black !important;
        font-family: 'Arial', sans-serif; /* Change font for dropdowns */
    }

    /* Style the success and error messages */
    .stSuccess {
        font-family: 'Georgia', serif;
    }
    .stError {
        font-family: 'Georgia', serif;
    }

    /* Center-align the title */
    h1 {
        text-align: center;
    }
    </style>

    """,
    unsafe_allow_html=True,
)

st.title("Unit-Converter")

value = st.number_input("enter input value " ,value = 1.0)

unit_Input = st.selectbox("enter Input unit", ["meter","kilometer","inch","feet","cm"])
unit_Output = st.selectbox("enter Output unit", ["meter","kilometer","inch","feet","cm"])

try:

    input_quantity = value * ureg(unit_Input)
    output_quantity = input_quantity.to(unit_Output)

    st.success(f"{value} {unit_Input} = {output_quantity.magnitude:.2f} {unit_Output}")
except Exception as e:
    st.error('error :{e}')
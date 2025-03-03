import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

UNIT_SYSTEM = {
    'Length': [
        'meter', 'kilometer', 'centimeter', 'millimeter',
        'micrometer', 'nanometer', 'mile', 'yard', 'foot', 'inch', 'light_year'
    ],
    'Temperature': ['kelvin', 'celsius', 'fahrenheit'],
    'Area': ['meter**2', 'kilometer**2', 'mile**2', 'acre', 'hectare'],
    'Volume': ['liter', 'milliliter', 'gallon', 'cubic_meter'],
    'Weight': ['gram', 'kilogram', 'milligram', 'pound', 'ounce'],
    'Time': ['second', 'minute', 'hour', 'day', 'week', 'year']
}

# Remove sidebar
st.set_page_config(layout="wide")

# CSS styling for tabs
st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 12px 25px;
        background: #f0f2f6;
        border-radius: 4px;
        transition: 0.3s;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background:hsl(0, 17.20%, 5.70%) !important;
        color: white !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📐 Unit Converter Express")

# Create tabs for categories
tabs = st.tabs(list(UNIT_SYSTEM.keys()))

# Conversion UI
tab_names = list(UNIT_SYSTEM.keys())
for i, tab in enumerate(tabs):
    with tab:
        value = st.number_input(f"Enter Value ({tab_names[i]})", value=1.0, step=0.1, key=f"value_{i}")
        from_unit = st.selectbox(f"From Unit ({tab_names[i]})", UNIT_SYSTEM[tab_names[i]], key=f"from_unit_{i}")
        to_unit = st.selectbox(f"To Unit ({tab_names[i]})", UNIT_SYSTEM[tab_names[i]], key=f"to_unit_{i}")
        
        if st.button("Convert Now", key=f"convert_btn_{i}"):
            try:
                if tab_names[i] == "Temperature":
                    input_q = ureg.Quantity(value, ureg(from_unit))
                    output_q = input_q.to(ureg(to_unit))
                else:
                    input_q = value * ureg(from_unit)
                    output_q = input_q.to(to_unit)
                
                st.success(f"Result: {output_q.magnitude:.2f} {to_unit}")
            except Exception as e:
                st.error(f"Error: {str(e)}")

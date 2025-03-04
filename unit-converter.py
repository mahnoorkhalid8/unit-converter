import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

length_units = {
    "meters": 1,
    "kilometers": 1000,
    "centimeters": 0.01,
    "millimeters": 0.001,
    "micrometers": 1e-6,
    "nanometers": 1e-9,
    "inches": 0.0254,
    "foot": 0.3048,
    "yards": 0.9144,
    "miles": 1609.34,
    "nautical_miles": 1852,
}

weight_units = {
    "kilograms": 1,
    "grams": 0.001,
    "milligrams": 1e-6,
    "pounds": 0.453592,
    "ounces": 0.0283495,
}

st.title("Unit Converter")
category = st.selectbox("Select Category", ["Length", "Weight"])

if category == "Length":
    units = length_units
else:
    units = weight_units

def convert(value, from_unit, to_unit):
    return value * units[to_unit] / units[from_unit]

col1, col2 = st.columns([2, 2])

with col1:
    from_unit = st.selectbox("From unit", list(units.keys()))
    length = st.number_input("Value", min_value=0.0, value=1.0)

with col2:
    to_unit = st.selectbox("To unit", units.keys())
    result = convert(length, from_unit, to_unit)
    st.metric(label= "Converted Value", value=f"{result:.6f}")

# st.info(f"Formula: Multiply by {length_units[to_unit] / length_units[from_unit]:.6f}")


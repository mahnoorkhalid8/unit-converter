import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

length_units = {
    "meters": 1000,
    "kilometers": 1,
    "centimeters": 100000,
    "millimeters": 1e+6,
    "micrometers": 1e+9,
    "nanometers": 1e+12,
    "inches": 39370.1,
    "foot": 3280.84,
    "yards": 1093.61,
    "miles": 0.621371,
    "nautical_miles": 0.539957,
}

weight_units = {
    "kilograms": 1,
    "grams": 1000,
    "milligrams": 1e+6,
    "pounds": 2.20462,
    "ounces": 35.274,
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
    st.metric(label= "Converted Value", value=f"{result:.2f}")

st.info(f"Formula: Multiply by {length_units[to_unit] / length_units[from_unit]:.6f}")


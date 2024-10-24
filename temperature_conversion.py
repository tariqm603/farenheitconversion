import streamlit as st

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

# Streamlit interface
st.title("Temperature Converter")

# Input for Fahrenheit to Celsius conversion
st.header("Convert Fahrenheit to Celsius")
fahrenheit_input = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
if st.button("Convert to Celsius"):
    converted_celsius = fahrenheit_to_celsius(fahrenheit_input)
    st.success(f"{fahrenheit_input}°F is equal to {converted_celsius:.2f}°C")

# Input for Celsius to Fahrenheit conversion
st.header("Convert Celsius to Fahrenheit")
celsius_input = st.number_input("Enter temperature in Celsius:", format="%.2f")
if st.button("Convert to Fahrenheit"):
    converted_fahrenheit = celsius_to_fahrenheit(celsius_input)
    st.success(f"{celsius_input}°C is equal to {converted_fahrenheit:.2f}°F")

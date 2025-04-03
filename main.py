import streamlit as st

#making unit converter with python

def convert_units(value, unit_from, unit_to):

    #now making dictionary 
    convertion = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "garams_kilograms": 0.001,
        "kilograms_grams": 1000
    }

    #now making formula for above key define
    key= f"{unit_from}_{unit_to}" #generate key for conversion

    #check if key exist in dictionary
    if key in convertion:

        #storing key value of meters_kilometer,kilometers_meter, garam_kilogram in storing_key_value
        storing_key_value = convertion[key]

        return value * storing_key_value  #here value is the value enter by user

    
    else:
        return("value not found ")
    
st.title("Unit Converter")

    #now to store value of user input we have to store in value
value = st.number_input("Please enter value to convert")

unit_from = st.selectbox("Select unit to convert from", ["meters" , "kilometers" , "garams" , "kilograms"])
unit_to = st.selectbox("Select unit to convert to", ["meters" , "kilometers" , "garams" , "kilograms"])

    #now we have to make button to convert
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted Value: {result}")





 
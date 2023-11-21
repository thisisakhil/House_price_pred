import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('model.pkl')

# Define the Streamlit app title and header
st.title('House Price Prediction')
st.write(
    "Welcome! Input the details below to predict the sale price of a house."
)

# Create separate sections for input fields and prediction result
st.sidebar.title('Enter House Details')

# Add input fields for features in separate sections
with st.sidebar.expander("House Features"):
    overall_qual = st.slider('Overall Quality (1-10)', 1, 10, 5)
    grliv_area = st.number_input('Above Ground Living Area (sqft)', min_value=0, value=1500)
    year_built = st.number_input('Year Built', min_value=1800, value=2000)
    total_bsmt_sf = st.number_input('Total Basement Area (sqft)', min_value=0, value=1000)
    full_bath = st.number_input('Number of Full Bathrooms Above Ground', min_value=0, value=2)
    half_bath = st.number_input('Number of Half Bathrooms Above Ground', min_value=0, value=1)
    garage_cars = st.number_input('Garage Size (in Car Capacity)', min_value=0, value=2)
    garage_area = st.number_input('Garage Area (sqft)', min_value=0, value=500)
    price_for_sft = 270963/grliv_area #270963 is the average price for square feet


# Make predictions and display result
if st.button('Predict'):
    input_data = pd.DataFrame({
        'OverallQual': [overall_qual],
        'GrLivArea': [grliv_area],
        'YearBuilt': [year_built],
        'TotalBsmtSF': [total_bsmt_sf],
        'FullBath': [full_bath],
        'HalfBath': [half_bath],
        'GarageCars': [garage_cars],
        'GarageArea': [garage_area],
        'price_for_sft':[price_for_sft]
    })
    
    prediction = model.predict(input_data)
    st.subheader('Prediction Result')
    st.write(f'Predicted Sale Price: ${prediction[0]:,.2f}')

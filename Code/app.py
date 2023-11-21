import streamlit as st
import joblib
import pandas as pd

# Load the trained model
# model = joblib.load('../Model/model.pkl')
model = joblib.load('/app/Model/model.pkl')

# Define the Streamlit app
st.title('House Price Prediction')

# Add input fields for features
overall_qual = st.sidebar.number_input('OverallQual', value=0)
grliv_area = st.sidebar.number_input('GrLivArea', value=0)
year_built = st.sidebar.number_input('YearBuilt', value=0)
total_bsmt_sf = st.sidebar.number_input('TotalBsmtSF', value=0)
full_bath = st.sidebar.number_input('FullBath', value=0)
half_bath = st.sidebar.number_input('HalfBath', value=0)
garage_cars = st.sidebar.number_input('GarageCars', value=0)
garage_area = st.sidebar.number_input('GarageArea', value=0)

# Create a DataFrame with user input
input_data = pd.DataFrame({
    'OverallQual': [overall_qual],
    'GrLivArea': [grliv_area],
    'YearBuilt': [year_built],
    'TotalBsmtSF': [total_bsmt_sf],
    'FullBath': [full_bath],
    'HalfBath': [half_bath],
    'GarageCars': [garage_cars],
    'GarageArea': [garage_area]
})

# Make predictions and display result
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Sale Price: ${prediction[0]:,.2f}')

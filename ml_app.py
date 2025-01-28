# import ml package
import joblib
import os

import streamlit as st
import numpy as np
import pandas as pd

from scipy.special import boxcox1p
        
def load_scaler(scaler_file):
    loaded_scaler = joblib.load(open(os.path.join(scaler_file), 'rb'))
    return loaded_scaler
        
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), 'rb'))
    return loaded_model

def run_ml_app():
    st.markdown("<h2 style = 'text-align: center;'> Input the Transaction Data </h2>", unsafe_allow_html=True)

    amount = st.number_input('Transaction Amount (USD)', 0.00, 999999.99, value=300.00)
    age = st.slider("Customer Age", 0, 100, 18)
    occupation = st.selectbox("Customer Occupation", ['Student', 'Doctor', 'Engineer', 'Retired'])
    duration = st.slider("Transaction Duration (Seconds)", 0, 600, 100)
    attempt = st.slider("Login Attempts", 1, 10, 1)
    balance = st.number_input('Account Balance (USD)', 0.00, 999999.99, value=5000.00)

    st.markdown("<h2 style = 'text-align: center;'>The Transaction Data </h2>", unsafe_allow_html=True)

    df = pd.DataFrame(
        {
            'Transaction Amount (USD)': [amount],
            'Customer Age': [age],
            'Customer Occupation': [occupation],
            'Transaction Duration (Seconds)': [duration],
            'Login Attempts': [attempt],
            'Account Balance (USD)': [balance]
        }
    )

    df[['Transaction Amount (USD)', 'Account Balance (USD)']] = df[['Transaction Amount (USD)', 'Account Balance (USD)']].applymap(lambda x: f"{x:,.2f}")

    st.dataframe(df)

    st.markdown("<h2 style = 'text-align: center;'> The Prediction Result </h2>", unsafe_allow_html=True)

    result = {
            'amount': float(boxcox1p(amount, 0.20)),
            'age': age,
            'duration': duration,
            'attempt': float(boxcox1p(attempt, 0.20)),
            'balance': float(balance),
            'occupation': occupation
    }

    # Map geography to one-hot encoding
    occupation_dict = {'Doctor'  : [1, 0, 0, 0], 
                       'Engineer': [0, 1, 0, 0], 
                       'Retired' : [0, 0, 1, 0],
                       'Student' : [0, 0, 0, 1],
                      }
    
    encoded_result = []

    for i in result.values():
        if type(i) == int:
            encoded_result.append(i)
        elif type(i) == float:
            encoded_result.append(i)
        elif i in ['Student', 'Doctor', 'Engineer', 'Retired']:
            encoded_result.extend(occupation_dict[i])

    single_array = np.array(encoded_result).reshape(1, -1)

    scaling = load_scaler("scaler.pkl")    
    scaling_array = scaling.transform(single_array)

    model = load_model("model_rf.pkl")  
    prediction = model.predict(scaling_array)

    if prediction == 'Fraud':
        st.warning("Beware! This transaction has the potential for fraud")
    else:
        st.success('This transaction is safe')\
    
    st.markdown('''<p style='text-align: justify;'> <br> <strong>Disclaimer:</strong> This tool is only to help detect fraud transactions. Perform further analysis to minimize prediction errors.</p>''', unsafe_allow_html=True)
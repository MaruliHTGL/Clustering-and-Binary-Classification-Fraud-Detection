import streamlit as st

from ml_app import run_ml_app

def main():
    menu = ['Home', 'Fraud Detection']
    choice = st.sidebar.radio("Menu", menu)

    if choice == 'Home':
            st.markdown(
            '''
            <h1 style='text-align: center;'> Defend Your Bank, Defeat Fraud </h1>
            <br>
            <h4 style='text-align: justify;'>Advanced Fraud Detection for a Safer Banking Experience</h4>
            <p style='text-align: justify;'>Protect every transaction with our intelligent fraud detection solution, designed to secure your bank and build customer trust. Leverage cutting-edge AI technology to identify and prevent suspicious activities, safeguarding your financial ecosystem. </p>
            <br>
            <h4 style='text-align: justify;'>Why Does Fraud Detection Matter?</h4>
            <p style='text-align: justify;'>Fraud is a growing threat in the banking sector, costing financial institutions billions of dollars each year. Common types of bank fraud include:</p>
                <ul style='text-align: justify;'>
                    <li><strong>Identity Theft:</strong> Fraudsters use stolen personal information to access accounts.</li>
                    <li><strong>Phishing Scams:</strong > Fake emails or websites trick customers into revealing sensitive data.</li>
                    <li><strong>Transaction Fraud:</strong> Unauthorized manipulation of payments for illicit gains.</li>
                </ul>
            </p>
            <br>
            <p style='text-align: justify;'>In addition to financial losses, fraud undermines customer trust and can lead to severe regulatory penalties. Take the first step towards fraud-free banking. Demo now and keep the transaction safe.</p>
            <br>
            <p style='text-align: center;'><strong>Building trust, one secure transaction at a time</strong></p>
            ''',
            unsafe_allow_html=True
        )
    elif choice == 'Fraud Detection':
        run_ml_app()


if __name__ == '__main__':
    main()

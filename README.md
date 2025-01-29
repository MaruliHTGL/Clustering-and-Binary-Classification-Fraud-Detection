# Clustering and Binary Classification: Fraud Detection

<p style='text-align: justify;'>
A tool to detect fraud in bank transactions by clustering transactions into 4 clusters first using the K-Means model, then data with the farthest distance from the centroid (exceeding the threshold) will be considered as fraud. Clusters will be determined based on the number of transactions, customer age, customer occupation, transaction duration, number of attempts, account balance.
</p>

<br>

- Using datasets from [kaggle](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)
- For the complete code please check [this file](https://github.com/MaruliHTGL/Clustering-and-Binary-Classification-Fraud-Detection/blob/b654cfa986aa55e942013d616d9575f3a30fc626/Fraud.ipynb)
- To test the model please visit [this link](https://frauddetector.streamlit.app/)
- Use this data to test the model:
    - Transaction Amount (USD): 500.00
    - Customer Age: 65
    - Customer Occupation: Retired
    - Transaction Duration (Seconds): 240
    - Login Attempts: 2
    - Account Balance (USD): 10000,00
 
<br>

**Disclaimer** : This tool is only to help detect fraud transactions. Perform further analysis to minimize prediction errors.

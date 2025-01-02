# import necessary libraries
import pandas as pd
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

def run_loading():
    #load cleaned datasets
    products = pd.read_csv('/home/ahly9667/airflow/zipco_food_dag/products.csv')
    customers = pd.read_csv('/home/ahly9667/airflow/zipco_food_dag/customers.csv')
    staff = pd.read_csv('/home/ahly9667/airflow/zipco_food_dag/staff.csv')
    transactions = pd.read_csv('/home/ahly9667/airflow/zipco_food_dag/transactions.csv')

    # create BlobServiceClient object
    load_dotenv()

    connect_str = os.getenv('AZURE_CONNECTION_STRING_VALUE')
    container_name = os.getenv('CONTAINER_NAME')

    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(container_name)

    # Load data to Azure Blob Storage
    files = [
        (products , 'cleaneddata/products.csv'),
        (customers , 'cleaneddata/customers.csv'),
        (staff , 'cleaneddata/staff.csv'),
        (transactions , 'cleaneddata/transactions.csv')
    ]

    for file , blob_name in files :
        blob_client = container_client.get_blob_client(blob_name)
        output = file.to_csv(index=False)
        blob_client.upload_blob(output , overwrite = True)
        print(f'{blob_name} loaded into Azure Blob Storage Successfully')
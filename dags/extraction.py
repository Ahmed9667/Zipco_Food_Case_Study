import pandas as pd

#data extraction
def run_extraction():
    try:
        df = pd.read_csv(r'D:\10alytics Data Engineering\week 11\Zipco_Food_Case_Study\zipco_transaction.csv')
        print('data extracted successfully')
    except Exception as e :
        print(f'an error occured {e}')    

import pandas as pd
def run_transformation():
    df = pd.read_csv('/home/ahly9667/airflow/zipco_food_dag/zipco_transaction.csv')

    #drop duplicates
    df = df.drop_duplicates()

    #drop null values
    for i in df.columns:

        if df[i].dtypes == 'object':
    
            df[i] = df[i].fillna('unknown')  #columns with string values
        else:

            df[i] = df[i].fillna(df[i].mean())    #columns with numeric values


     #create table products
    products = df[['ProductName','UnitPrice']].copy().drop_duplicates().reset_index()
    products['product_id'] = range(1,len(products)+1)
    products = products[['product_id','ProductName','UnitPrice']]

     #create table customers
    customers = df[['CustomerName', 'CustomerAddress', 'Customer_PhoneNumber','CustomerEmail']].copy().drop_duplicates().reset_index()
    customers['customer_id'] = range(1,len(customers)+1)
    customers = customers[['customer_id','CustomerName', 'CustomerAddress', 'Customer_PhoneNumber','CustomerEmail']]  

    #create table staff
    staff = df[['Staff_Name', 'Staff_Email']].copy().drop_duplicates().reset_index()
    staff['staff_id'] = range(1,len(staff)+1)
    staff = staff[['staff_id','Staff_Name', 'Staff_Email']]

    #create table transactions
    transactions = df.merge(products,on=['ProductName','UnitPrice'],how='left')\
                    .merge(customers,on=['CustomerName', 'CustomerAddress', 'Customer_PhoneNumber','CustomerEmail'],how='left')\
                    .merge(staff,on=['Staff_Name', 'Staff_Email'],how='left')
    transactions['transaction_id'] = range(1,len(transactions)+1)
    transactions = transactions.reset_index()\
                [['transaction_id','product_id','customer_id','staff_id','Quantity',
                'StoreLocation','PaymentType', 'PromotionApplied', 'Weather', 'Temperature',
                    'StaffPerformanceRating', 'CustomerFeedback', 'DeliveryTime_min','OrderType',
                    'DayOfWeek','TotalSales','Date']]
    
    #convert date column to date type
    transactions['Date'] = pd.to_datetime(transactions['Date'])
    transactions['Date'].dtypes

    #save data
    products.to_csv('/home/ahly9667/airflow/zipco_food_dag/products.csv',index=False)
    customers.to_csv('/home/ahly9667/airflow/zipco_food_dag/customers.csv',index=False)
    staff.to_csv('/home/ahly9667/airflow/zipco_food_dag/staff.csv',index=False)
    transactions.to_csv('/home/ahly9667/airflow/zipco_food_dag/transactions.csv',index=False)
    print('Data cleaned and saved successfully')
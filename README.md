# Zipco_Food_Case_Study
## Summary:
Zipco Foods is a vibrant and growing business that specializes in the
sales of pizzas and cakes. As a key player in the fast-casual dining
industry, Zipco Foods operates numerous outlets across the country,
serving a wide variety of pizzas and cakes that cater to local tastes and
preferences.
## Business Problem Statement:
The primary challenge is the disparate nature of data
collection and storage, with critical sales and inventory information
scattered across multiple CSV files without a unified system for
aggregation and analysis.
## Objectives & Benefits:
### `Objectives:`
● Implement a streamlined ETL (Extract, Transform, Load) pipeline to automate data processing and
ensure data consistency.
● Design a database schema that supports efficient data retrieval and scalability while adhering to
2NF/3NF normalization standards.
● Develop a system for real-time data analytics to aid in decision-making processes.
● Ensure robust data governance and compliance through effective version control and data
orchestration.
### `Benefits:`
● Enhanced decision-making capabilities through real-time, accurate data analytics.
● Improved operational efficiency and reduced manual labor by automating data processes.
● Greater scalability and flexibility in data management, accommodating future business growth.
● Strengthened data integrity and reliability, ensuring high-quality information for strategic
planning.

## Tech Stack:
● `Python:` Utilized for scripting the ETL processes, data cleaning, transformation,
and analysis tasks due to its powerful libraries like pandas and NumPy.

● `Azure Blob Storage:` Chosen for its scalability and reliability, serving as the
centralized data repository for storing processed data.

● `Github:` Used for version control, allowing for collaborative development and
maintenance of the ETL scripts and other project documents.

● `Apache Airflow:` Orchestrates the ETL processes, scheduling jobs efficiently and
monitoring the workflow of data through various stages of the pipeline.

![image](https://github.com/user-attachments/assets/0d31bf3e-537a-4dc6-8951-e7990bdfc3d9)

## Project Scope:
#### ● Data Extraction:
Extract data from various CSV files into a Pandas DataFrame. This step
involves reading large datasets efficiently, handling different data formats, and
managing incomplete or corrupt data files.

#### Data Transformation:
○ Clean the extracted data to remove inconsistencies, duplicates, and handle
missing values.
○ Transform the data to fit into a designed schema that adheres to the principles
of 2NF and 3NF. This involves decomposing tables to reduce redundancy,
ensuring referential integrity, and optimizing the schema for query performance.

![schema](https://github.com/user-attachments/assets/e436262a-75c1-4db0-9c51-03d4bdea3bca)


#### Data Loading:
○ Load the cleaned and transformed data into Azure Blob Storage, which serves as the
centralized repository for all analytical data.
○ Implement version control using GitHub to maintain revisions of the data transformation
scripts and other configurations.
○ Use Apache Airflow to orchestrate the entire ETL process. Define DAGs (Directed Acyclic
Graphs) to manage the workflow of tasks including dependencies and sequence of
operations, ensuring that the data flows smoothly from extraction through to loading, with
logging and error handling to manage failures or retries effectively.
○ This case study outlines the strategic approach for utilizing advanced data engineering
techniques to drive operational improvements and business growth for Zipco Foods.

![airflow](https://github.com/user-attachments/assets/7532982b-4508-417f-a689-67697a40bd2b)





 

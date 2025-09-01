# Real-Estate-ETL-Pipeline
This project involves collecting real estate data from the **SAROUTY** website using Selenium via an Amazon Web Services (AWS) EC2 instance. The collected data is then stored in an S3 bucket for further processing.

Next, the data is cleaned, transformed, and ingested using AWS Glue. Data cleaning and transformation involve removing duplicates, filling in missing values, eliminating irrelevant data, and performing data transformations to better prepare it for machine learning.

**Overall, this project aims to provide an efficient method for collecting and processing real estate data at scale, delivering accurate Data and valuable insights for real estate analysts, investors, and professionals.**

<h2> 🚀 Tech Stack </h2>

**AWS EC2** → Running Selenium-based scraper

**Selenium & Python** → Web scraping

**AWS S3** → Raw and processed data storage

**AWS Glue** → Data cleaning, transformation & schema management

**Amazon Redshift** → Data warehousing for analytics & BI

**Apache Airflow** → Pipeline orchestration & automation

**boto3** → AWS SDK for Python

<h2> 🚀 Key Features </h2>
- Automated data extraction from SAROUTY using Selenium on EC2.
- Data lake storage with S3 (raw & processed zones).
- ETL with AWS Glue: removing duplicates, handling missing values, and preparing features.
- Data warehouse integration with Redshift for fast SQL queries and reporting.
- End-to-end orchestration with Airflow (scheduled, monitored, and automated).
- Scalable architecture ready for high-volume real estate datasets.

<h2> Architecture du projet </h2>

EC2 instance runs a Python script using Selenium to extract data from SAROUTY.

**Data storage in an S3 bucket:**
The collected data is transferred from the EC2 instance to an AWS S3 bucket using the Python library boto3.

**Data cleaning with AWS Glue:**
The data stored in the S3 bucket is processed by AWS Glue, which can be used to perform data cleaning and feature engineering steps.
AWS Glue is a fully managed data processing service that can handle data stored in S3, remove duplicates, fill missing values, and apply data transformations.
The cleaned and transformed data is then stored in another S3 bucket.

**Loading data into Amazon Redshift:**
After cleaning and transformation, the processed data is loaded into Amazon Redshift, a fully managed data warehouse service. This allows for fast SQL-based querying and analytics on the real estate data, enabling further insights and reporting.

**Process Automation with Airflow:**
A DAG file is created using Apache Airflow to automate the scraping and data cleaning process.
The DAG can be scheduled to run at a specific frequency (e.g., daily) to keep the data up to date.
Airflow can also send email notifications to inform users of the success or failure of the scraping and data cleaning process.

<a href="https://www.imgur.com"><img src="https://i.imgur.com/6pOlMcR.jpg" alt="Alt Text" title="Click to enlarge" width="800" height="400" /></a>

<h2>Steps for realizing the project</h2>
<h3> Start by scraping data in EC2 instance </h3> 
<img width="854" height="188" alt="SSH Connection 1 " src="https://github.com/user-attachments/assets/8bc002ef-3190-48b9-8b6c-0fb5f03816d0" />

SSH Connection EC2 Instance 

<img width="940" height="331" alt="scp protocol 2" src="https://github.com/user-attachments/assets/af300656-8d08-40c2-a76b-862e2a206231" />
<img width="937" height="311" alt="scp 2" src="https://github.com/user-attachments/assets/82c6acc2-3be2-4f4e-b49b-e2998c969b49" />

<img width="928" height="238" alt="scraping-execution 4" src="https://github.com/user-attachments/assets/901369f9-5d4b-4811-bc63-65be29083470" />
<img width="853" height="233" alt="scraping execution 5" src="https://github.com/user-attachments/assets/912aa7b8-6d4d-4e18-8d47-4a626c30d1a4" />

<h5>Execute Script of Data Scrapping </h5> 

<h3> Data ingestion into S3 Bucket </h3>
<h5>Creation of S3 Bucket</h5> 

<img width="956" height="448" alt="S3 Creation 1" src="https://github.com/user-attachments/assets/31d2dfcb-0539-4cae-a5ce-d40fba839745" />

<h5>Ingestion of Raw Data </h5>

<img width="953" height="446" alt="Ingestion Raw Data " src="https://github.com/user-attachments/assets/c474bf5e-337e-421c-8010-08879a97682a" />

<a href="https://www.imgur.com"><img src="https://i.imgur.com/6S7xdNe.jpg" alt="Alt Text" title="Click to enlarge" width="800" height="400" /></a>

<h3> Data preprocessing in AWS Glue </h3>
<h5>Creation of AWS Crawler </h5>

<img width="953" height="446" alt="AWS GLUE CRAWLER " src="https://github.com/user-attachments/assets/593f4c90-858d-40cb-a84b-f25883515267" />
<h5>Running AWS Crawler </h5>
<img width="959" height="446" alt="Crawler Runned " src="https://github.com/user-attachments/assets/d62e273c-1168-4185-81db-f139990bd97e" />

<h5>Glue Access Policy </h5>
<img width="959" height="484" alt="Glue Access IAM Policy" src="https://github.com/user-attachments/assets/c51fda88-676a-4eda-aa28-73dd2495a27c" />

<h5>Data After Processing and Partition Data in S3 Bucket </h5>
<img width="947" height="365" alt="Data After Processing" src="https://github.com/user-attachments/assets/fa17c587-4011-4b76-b550-011a1adcc9f9" />
<img width="953" height="299" alt="Partionned Data " src="https://github.com/user-attachments/assets/3d990efb-3b78-4f2c-9bbc-db7fba9e321e" />

<h3> Data Warehousing using AWS Redhsift </h3>
<img width="953" height="475" alt="Create Tables Using AWS Redshift Query Editor" src="https://github.com/user-attachments/assets/66ac4b64-73fd-491c-ab07-41ae2afb4815" />

<h3> Pipeline Orchestration using Apache Airflow </h3>

<img width="953" height="254" alt="ETL With Airflow" src="https://github.com/user-attachments/assets/a538beab-e230-4a39-a567-ccc735ca7778" />

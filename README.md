# Catch project presentation
Inventory Analysis: https://youtu.be/7kgBPWAAAzE  
Description: Assists organizations handle their inventory and manage their supply chain costs. 1

# Inventory Analysis
<img src="https://drive.google.com/uc?export=view&id=1ebEtsd8OazZg5JEadEf8Cc6ys-A6bUxK" alt="Project Logo" width="200" height="200">

## Table of Contents
1. Project Overview
2. Folder Structure
3. Technologies Used
4. Setup Instructions
5. Files Overview
6. How to Run
7. Power-BI Dashboard Images

## Project Overview
The Inventory Analysis Project is designed to analyze and manage inventory data for a business, offering insights into purchase prices, sales, and stock levels. This project utilizes Google Drive API to fetch files, processes the data using Python, and loads it into a MySQL database for storage and analysis. The final goal is to create dashboards and visualizations in Power BI.

## Folder Structure
``` bash
Inventory Analysis/
├── data/
│   ├── raw/                # Original data files downloaded from Google Drive
│   ├── cleaned/            # Cleaned data files for analysis
├── notebooks/              # Jupyter notebooks for data cleaning and EDA
├── scripts/                # Python scripts for Google Drive API, data processing, and loading data to SQL
│   ├── google_drive_api.py # Code for Google Drive API authentication and data downloading
│   ├── data_cleaning.ipynb # Jupyter notebook for data cleaning and exploratory data analysis
│   └── load_to_sql.py      # Script to load cleaned data into MySQL
├── .venv/                  # Virtual environment
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation
```

## Technologies Used
- Python: For data processing, manipulation, and integration with Google Drive and MySQL.
- Pandas: To handle and clean data within Python.
- Google Drive API: Used to fetch data files from Google Drive.
- MySQL: For database storage and data analysis.
- Jupyter Notebook: Used for data cleaning and exploratory data analysis (EDA).
- Power BI: For visualization and dashboard creation.

## Setup Instructions
### 1. Clone the Repository
``` bash
git clone <repo-url>
cd Inventory Analysis
```


### 2. Create a Virtual Environment
``` bash
python -m venv .venv
source .venv/bin/activate  # For Unix/MacOS
.venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies Install all necessary libraries from the requirements.txt file:
``` bash
pip install -r requirements.txt
```

### 4. Set Up Google Drive API:
- Place your Google Drive client_secret.json file in the credentials/ folder.
- Run the google_drive_api.py script to generate a token.json file, which will authenticate your Google Drive session.

### 5.Database Setup
- Ensure MySQL server is installed and running.
- Create a new database called inventory_analysis in MySQL.
- Update the load_to_sql.py file with your MySQL username and password to connect to the database.

### 6. Files Overview
- **credentials/client_secret.json:** Credentials file for authenticating with Google Drive API.
- **data/cleaned:** Contains cleaned data files for direct loading into SQL.
- **scripts/google_drive_api.py:** This script connects to Google Drive, downloads data files, and saves them locally. Make sure to run it first to obtain the required data.
- **scripts/data_cleaning.ipynb:** Jupyter Notebook for data cleaning and exploratory data analysis (EDA). Run this notebook to prepare the raw data and save it in the data/cleaned folder.
- **scripts/load_to_sql.py:** Script for loading the cleaned CSV files into the MySQL database.

## How to Run
### 1. Activate Google Drive Authentication
- Run the Google Drive API script to authenticate and fetch data files:
``` bash
python scripts/google_drive_api.py
Perform Data Cleaning and EDA
```

### 2. Open data_cleaning.ipynb in Jupyter Notebook and run the cells to clean and prepare the data for analysis.
- Save the cleaned files in the data/cleaned folder for database loading.

### 3. Load Data Into SQL Database
- Run the load_to_sql.py script to load all cleaned data files into MySQL tables:
``` bash
python scripts/load_to_sql.py
```
This will create and populate the necessary tables in the inventory_analysis database.

### 4. Analyze Data in Power BI
- Connect Power BI to your MySQL database to analyze the data and create visualizations and dashboards.

## Power-BI Dashboard Screenshots

### Home Page
![Home Page](https://drive.google.com/uc?export=view&id=1KAwZMy35SyGd8E_AjZhrwHqiV1S2V1YF)

### Overview
![Overview](https://drive.google.com/uc?export=view&id=1HS4ZymHPNCQQ-9yO8T7qwNaZQvTwkQxO)

### Dashboard
![Dashboard](https://drive.google.com/uc?export=view&id=1FQrfKm00gSqHSFdG-7lLQSi_4ERG2c26)

<div align="center">

# 📊 Financial Performance Analyser

### End to End Financial Data Analysis with Python, SQL, pandas and Matplotlib

A complete financial analytics project that cleans, validates, stores, analyses and visualises simulated banking data to evaluate profitability, efficiency, returns and stock performance.

<br>

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-orange)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-181717?logo=github&logoColor=white)

<br>

[View Repository](https://github.com/abdurraffayshah/financial-performance-analyser)

</div>

<br>

## 📌 Project Overview

The **Financial Performance Analyser** is an end to end data analytics project built to investigate the financial performance of a fictional bank across 2022 and 2023.

The project begins with raw financial data containing deliberately introduced data quality issues. The data is cleaned and validated using Python and pandas before being stored in an SQLite database.

SQL is then used to perform financial queries and identify key periods of performance. pandas is used for further statistical and comparative analysis, while Matplotlib is used to create visualisations that communicate the trends found in the data.

The final analysis focuses on four main areas:

1. **Profitability**
2. **Financial efficiency**
3. **Returns generated from assets and equity**
4. **The relationship between financial performance and stock price**

<br>

## 🎯 Project Objectives

The project aims to answer the following questions:

1. How did the bank's profitability change over time?

2. Which periods recorded the highest net income?

3. When was net interest margin strongest?

4. How did return on assets and return on equity change?

5. Did the bank's operating efficiency improve or deteriorate?

6. Which periods recorded the lowest cost to income ratio?

7. How did the bank's stock price change over time?

8. Is there a relationship between stock price and financial performance?

9. How did key financial metrics change between 2022 and 2023?

<br>

## 🔄 Project Workflow

```text
Raw Financial Dataset
        │
        ▼
Data Inspection
        │
        ▼
Data Cleaning
        │
        ▼
Validation
        │
        ▼
Financial Metric Creation
        │
        ▼
Processed CSV
        │
        ▼
SQLite Database
        │
        ▼
SQL Analysis
        │
        ▼
pandas Analysis
        │
        ▼
Matplotlib Visualisations
        │
        ▼
Financial Findings Report
```

<br>

## 📂 Dataset

The project uses a **simulated financial dataset for a fictional bank** covering observations across 2022 and 2023.

The original dataset contains the following financial variables:

| Financial Variable | Description |
| --- | --- |
| Interest Income | Income generated from interest earning activities |
| Interest Expense | Cost of interest bearing liabilities |
| Average Earning Assets | Assets used to generate interest income |
| Net Income | Profit generated during the period |
| Total Assets | Total value of the bank's assets |
| Shareholder Equity | Equity attributable to shareholders |
| Operating Expenses | Costs associated with operating the bank |
| Operating Income | Income generated through operations |
| Market Share | Estimated share of the market |
| Stock Price | Simulated share price |

The dataset also contains deliberately introduced data quality issues including missing values, duplicate records and potential outliers.

<br>

## 🧹 Data Cleaning

The raw dataset is processed through a custom cleaning pipeline before any financial analysis takes place.

The cleaning stage performs:

1. Column name standardisation

2. Duplicate record removal

3. Missing value inspection

4. Missing date handling

5. Removal of heavily incomplete records

6. Data type conversion

7. Invalid negative value detection

8. Market share validation

9. Outlier identification using the IQR method

10. Final data validation

Potential outliers are identified rather than automatically deleted because unusual financial observations may contain useful analytical information.

<br>

## 🧮 Financial Metrics

Several financial metrics are calculated from the original dataset.

### Net Interest Income

```text
Net Interest Income = Interest Income - Interest Expense
```

Net interest income measures the difference between interest earned and interest paid.

<br>

### Net Interest Margin

```text
Net Interest Margin =
(Net Interest Income / Average Earning Assets) × 100
```

Net interest margin measures how effectively the bank generates interest income from its earning assets.

<br>

### Return on Assets

```text
ROA =
(Net Income / Total Assets) × 100
```

Return on assets measures how effectively the bank uses its assets to generate profit.

<br>

### Return on Equity

```text
ROE =
(Net Income / Shareholder Equity) × 100
```

Return on equity measures the return generated from shareholder capital.

<br>

### Cost to Income Ratio

```text
Cost to Income Ratio =
(Operating Expenses / Operating Income) × 100
```

The cost to income ratio is used as an indicator of operational efficiency.

A lower value generally suggests that a smaller proportion of operating income is being consumed by operating costs.

<br>

## 🗄️ SQLite Database

After the cleaning and validation stage, the processed data is stored inside an SQLite database.

The database stage includes:

1. Creating a connection to the SQLite database

2. Creating the `financial_data` table

3. Importing the processed CSV data

4. Converting empty values into SQL `NULL` values

5. Preventing duplicate date records

6. Verifying that the database has been populated correctly

Using SQLite allows the project to demonstrate both traditional relational database analysis and pandas based analysis within the same workflow.

<br>

## 🔎 SQL Analysis

SQL is used to analyse the cleaned financial data directly from the database.

The SQL analysis includes:

1. Top five net income periods

2. Top five net interest margin periods

3. Average return on assets

4. Average return on equity

5. Identification of negative net income periods

6. Yearly average net income

7. Yearly average net interest margin

8. Lowest cost to income periods

9. Highest stock price periods

10. Yearly average stock price

The SQL stage demonstrates the use of:

```sql
SELECT
WHERE
AVG
GROUP BY
ORDER BY
ASC
DESC
LIMIT
strftime()
```

<br>

## 🐼 pandas Analysis

After the SQL analysis, the financial data is loaded directly from SQLite into a pandas DataFrame.

The pandas stage includes:

1. Loading SQL data into pandas

2. Converting dates into pandas datetime objects

3. Extracting the year from each observation

4. Creating yearly performance summaries

5. Calculating Pearson correlations

6. Calculating percentage changes between 2022 and 2023

<br>

### Yearly Performance Summary

The following metrics are compared on a yearly basis:

1. Net income

2. Net interest margin

3. Return on assets

4. Return on equity

5. Cost to income ratio

6. Stock price

This provides a high level comparison of how the bank's financial performance changed between 2022 and 2023.

<br>

### Stock Price Correlation Analysis

Pearson correlation is used to investigate the relationship between stock price and:

1. Net income

2. Net interest margin

3. Return on assets

4. Return on equity

5. Cost to income ratio

The analysis is designed to identify possible linear relationships between financial performance and stock price.

Correlation is not interpreted as evidence of causation.

<br>

### Performance Change Analysis

The percentage change between 2022 and 2023 is calculated using:

```text
Percentage Change =
((New Value - Old Value) / Old Value) × 100
```

This allows improvements and declines in financial performance to be quantified rather than assessed visually alone.

<br>

## 📈 Visualisations

Matplotlib is used to create visualisations that make the underlying financial trends easier to interpret.

### Monthly Average Net Income

Shows how profitability changed over the two year period.

<br>

### Monthly Average Net Interest Margin

Shows how the bank's core interest profitability changed over time.

<br>

### Monthly Average ROA and ROE

Compares the returns generated from assets and shareholder equity.

<br>

### Monthly Average Cost to Income Ratio

Shows how the bank's operational efficiency changed over time.

<br>

### Monthly Stock Price vs Net Income

Uses two y axes to compare changes in stock price with changes in profitability.

This visual comparison is supported by the Pearson correlation analysis performed in pandas.

<br>

## 🧠 Why Monthly Averages?

The original dataset contains a large number of individual observations.

Plotting every observation directly produced highly volatile charts that made underlying trends difficult to interpret.

The visualisation stage therefore groups observations into monthly averages.

This creates clearer time series while still preserving the original observations for SQL and pandas analysis.

<br>

## 🛠️ Technologies Used

| Technology | Purpose |
| --- | --- |
| Python | Core programming language |
| pandas | Data cleaning, manipulation and analysis |
| NumPy | Numerical operations and missing value handling |
| SQLite | Relational data storage |
| SQL | Querying and financial aggregation |
| Matplotlib | Financial visualisation |
| Git | Version control |
| GitHub | Repository hosting and project documentation |
| VS Code | Development environment |

<br>

## 🗂️ Project Structure

```text
financial-performance-analyser
│
├── data
│   │
│   ├── raw
│   │   └── myusabank.csv
│   │
│   └── processed
│       └── cleaned_data.csv
│
├── database
│   └── financial_performance.db
│
├── src
│   │
│   ├── data_cleaning.py
│   ├── database.py
│   ├── sql_analysis.py
│   ├── pandas_analysis.py
│   ├── visualisations.py
│   └── main.py
│
├── outputs
│   └── charts
│
├── README.md
│
└── requirements.txt
```

<br>

## 🧩 Project Architecture

The project is separated into modules so that each file has a clear responsibility.

### `data_cleaning.py`

Responsible for loading, inspecting, cleaning, validating and preparing the raw financial dataset.

### `database.py`

Responsible for creating the SQLite database, creating the financial table and inserting processed data.

### `sql_analysis.py`

Contains SQL based financial analysis functions.

### `pandas_analysis.py`

Contains pandas based statistical and comparative analysis.

### `visualisations.py`

Contains all Matplotlib visualisation functions.

### `main.py`

Acts as the main controller for the project and combines the database, SQL analysis, pandas analysis and visualisation stages.

<br>

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/abdurraffayshah/financial-performance-analyser.git
```

### 2. Enter the project directory

```bash
cd financial-performance-analyser
```

### 3. Create a virtual environment

#### Windows

```bash
python -m venv .venv
```

Activate the environment:

```bash
.\.venv\Scripts\Activate.ps1
```

#### macOS or Linux

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

```bash
python src/main.py
```

The program will:

1. Connect to the SQLite database

2. Load the financial data

3. Perform SQL analysis

4. Perform pandas analysis

5. Calculate year on year changes

6. Calculate stock price correlations

7. Generate all financial visualisations

8. Close the database connection

<br>

## 📊 Financial Analysis Report

A separate professional financial analysis report accompanies the project.

[View the full Financial Performance Analysis Report](./Financial_Performance_Analysis_Report.pdf)

The report will convert the technical analysis into a concise business focused interpretation of the bank's performance.

It will include:

1. Executive Summary

2. Dataset and Methodology

3. Profitability Analysis

4. Net Interest Margin Analysis

5. Return on Assets and Return on Equity

6. Operational Efficiency

7. Stock Price Analysis

8. Correlation Analysis

9. Key Financial Findings

10. Limitations

11. Conclusion


<br>

## ⚠️ Limitations

The analysis has several important limitations.

### Simulated Dataset

The data represents a fictional bank and should not be interpreted as the financial performance of a real financial institution.

### ROA Calculation

Return on assets is calculated using total assets at each observation rather than average assets across a reporting period.

### ROE Calculation

Return on equity is calculated using shareholder equity at each observation rather than average equity across a reporting period.

### Correlation

Pearson correlation measures linear association but does not prove that one variable causes another.

### Time Period

The dataset covers approximately two years, which limits the ability to draw longer term conclusions.

### Monthly Aggregation

Monthly averages improve chart readability but reduce the visibility of individual extreme observations.

The original observations remain available within the database for detailed analysis.

<br>

## 💡 Skills Demonstrated

Through this project I developed and demonstrated practical experience with:

1. Python programming

2. Data cleaning

3. Data validation

4. pandas

5. NumPy

6. SQLite

7. SQL

8. Database design

9. Financial metric calculation

10. Financial analysis

11. Time series analysis

12. Pearson correlation analysis

13. Data visualisation

14. Data interpretation

15. Modular Python development

16. Git version control

17. GitHub project management

<br>

## 🚀 Future Improvements

Possible extensions to the project include:

1. Adding additional years of financial data

2. Building an interactive Streamlit dashboard

3. Adding quarterly financial analysis

4. Expanding the stock price analysis

5. Adding automated report generation

6. Introducing additional banking performance metrics

7. Comparing multiple financial institutions

These extensions are outside the current project scope but could be implemented in future versions.

<br>

## 📄 Disclaimer

This project uses simulated financial data for educational and portfolio purposes.

The analysis should not be interpreted as investment advice or as an assessment of any real financial institution.

<br>

<div align="center">

## 👤 Author

### Abdur Raffay

Aspiring Data Analyst focused on using data, programming and financial analysis to solve real world problems.

<br>

[![GitHub](https://img.shields.io/badge/GitHub-abdurraffayshah-181717?logo=github&logoColor=white)](https://github.com/abdurraffayshah)

</div>

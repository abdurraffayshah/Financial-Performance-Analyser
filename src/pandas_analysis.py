import pandas as pd
from database import create_connection

# Load database connection
connection = create_connection("database/financial_performance.db")

def load_sql_data(conn):
    """Load financial data from database into a DataFrame."""
    
    # Query all rows from financial_data table
    df = pd.read_sql_query("SELECT * from financial_data", conn)
    return df

# Load data from database
dataframe = load_sql_data(connection)

def add_year_column(df):
    """Convert date to datetime and add year column."""
    
    # Parse date column and extract year
    df["date"] = pd.to_datetime(df["date"])
    years = df["date"].dt.year
    
    # Insert year column at position 1
    df.insert(1, "year", years)
    return df

# Add year column to dataframe
dataframe = add_year_column(dataframe)

def yearly_performance_summary(df):
    """Calculate yearly average of key financial metrics."""
    
    # Group by year
    df = df.groupby("year")
    
    # Calculate mean for each metric
    results = df[["net_income", "net_interest_margin", "return_on_assets", "return_on_equity", "cost_to_income_ratio", "stock_price"]].mean()
    
    # Round to 2 decimal places
    results = results.round(2)
    
    return results

def stock_price_correlation(df):
    """Calculate and display Pearson correlation between stock price and financial metrics."""
    
    # Define columns to analyze for correlation with stock price
    columns = ["stock_price", "net_income", "net_interest_margin", "return_on_assets", "return_on_equity", "cost_to_income_ratio"]
    
    # Calculate correlation matrix using Pearson method
    correlations = df[columns].corr(method="pearson")
    
    # Extract stock price correlations
    results = correlations["stock_price"]
    
    # Print correlation values rounded to 2 decimal places
    for column in columns:
        print(f"{column}: {round(results[column], 2)}")
    

def performance_change(df):
    """Calculate percentage change in financial metrics from 2022 to 2023."""
    
    # Group dataframe by year and calculate mean values
    df = df.groupby("year").mean()
    
    # Define financial metric columns to analyze
    columns = ["net_income", "net_interest_margin", "return_on_assets", "return_on_equity", "cost_to_income_ratio", "stock_price"]
    
    # Select only the specified columns
    df = df[columns]
    
    # Initialize list to store percentage change results
    percentage_change = []
    
    # Calculate percentage change for each metric
    for column in columns:
        # Get 2022 and 2023 values
        figure2022 = df[column].loc[2022]
        figure2023 = df[column].loc[2023]
        
        # Calculate percentage change and round to 2 decimal places
        p_change = round((float((figure2023 - figure2022) / figure2022) * 100), 2)
        
        # Append column name and percentage change to results
        percentage_change.append([column, p_change])
        
    return percentage_change

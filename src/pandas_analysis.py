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

# Print yearly performance summary
print(yearly_performance_summary(dataframe))
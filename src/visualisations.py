import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter


def plot_net_income(df):
    """Plot monthly average net income trend over time."""
    
    # Resample data by month end and calculate mean net income
    monthly_data = df.set_index("date").resample("ME")["net_income"].mean()
    
    # Plot the monthly trend line
    plt.plot(monthly_data.index, monthly_data.values)
    
    # Set x-axis to show every 3 months
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    
    # Format x-axis dates as "Month Year"
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.xticks(rotation = 45)
    
    # Format y-axis as currency in millions of pounds
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"£{x / 1_000_000:.2f}m")
    )
    
    plt.tight_layout()
    plt.xlabel("Date")
    plt.ylabel("Average Net Income")
    plt.title("Monthly Average Net Income")
    plt.show()
    


def plot_nim_trend(df):
    """Plot monthly average net interest margin trend over time."""
    
    # Resample data by month end and calculate mean net interest margin
    monthly_data = df.set_index("date").resample("ME")["net_interest_margin"].mean()
    
    # Plot the monthly trend line
    plt.plot(monthly_data.index, monthly_data.values)
    
    # Set x-axis to show every 3 months
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    
    # Format x-axis dates as "Month Year"
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.xticks(rotation = 45)
    
    # Format y-axis as percentage with 2 decimal places
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"{x:.2f}%")
    )
    
    plt.tight_layout()
    plt.xlabel("Date")
    plt.ylabel("Average Net Interest Margin")
    plt.title("Monthly Average Net Interest Margin")
    plt.show()


def plot_profitability_ratios(df):
    """Plot monthly average ROA and ROE trends for comparison."""
    
    # Resample data by month end and calculate mean return on assets
    monthly_data_roa = df.set_index("date").resample("ME")["return_on_assets"].mean()
    
    # Resample data by month end and calculate mean return on equity
    monthly_data_roe = df.set_index("date").resample("ME")["return_on_equity"].mean()
    
    # Plot ROA trend line
    plt.plot(monthly_data_roa.index, monthly_data_roa.values, label = "Return On Assets")
    
    # Plot ROE trend line
    plt.plot(monthly_data_roe.index, monthly_data_roe.values, label = "Return On Equity")
    
    # Display legend to differentiate lines
    plt.legend()
    
    # Set x-axis to show every 3 months
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3))
    
    # Format x-axis dates as "Month Year"
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    
    # Format y-axis as %
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"{x:.2f}%")
    )
    
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.xlabel("Date")
    plt.ylabel("Average Return (%)")
    plt.title("Monthly Average ROA and ROE")
    plt.show()



def plot_cost_to_income(df):
    """Plot monthly average cost to income ratio trend over time."""
    
    # Resample data by month end and calculate mean cost to income ratio
    monthly_data = df.set_index("date").resample("ME")["cost_to_income_ratio"].mean()
    
    # Plot the monthly trend line
    plt.plot(monthly_data.index, monthly_data.values)
    
    # Set x-axis to show every 3 months
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval = 3))
    
    # Format x-axis dates as "Month Year"
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    
    # Format y-axis as percentage with 1 decimal place
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"{x:.1f}%")
    )
    
    plt.xticks(rotation = 45)
    plt.xlabel("Date")
    plt.ylabel("Average Cost to Income Ratio (%)")
    plt.title("Monthly Average Cost to Income Ratio")
    plt.tight_layout()
    plt.show()
    

def plot_stock_price_vs_performance(df):
    """Plot stock price and net income on dual y-axes for comparison."""
    
    # Resample data by month end and calculate mean stock price
    monthly_data_sp = df.set_index("date").resample("ME")["stock_price"].mean()
    
    # Resample data by month end and calculate mean net income
    monthly_data_ni = df.set_index("date").resample("ME")["net_income"].mean()
    
    # Create figure with primary y-axis
    fig, ax1 = plt.subplots()
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Average Stock Price")
    
    # Plot stock price on primary y-axis
    ax1.plot(monthly_data_sp.index, monthly_data_sp.values, label = "Stock Price")
    
    # Create secondary y-axis for net income
    ax2 = ax1.twinx()
    colour = 'tab:red'
    ax2.set_ylabel("Average Net Income", color = colour)
    
    # Plot net income on secondary y-axis in red
    ax2.plot(monthly_data_ni.index, monthly_data_ni.values, label = "Net Income", color = colour)
    
    # Display legend for both axes
    fig.legend()
    
    # Set x-axis to show every 3 months
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    
    # Format x-axis dates as "Month Year"
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax1.tick_params(axis="x", rotation=45)
    
    # Format primary y-axis (stock price) as currency
    ax1.yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"${x:.2f}")
    )
    
    # Format secondary y-axis (net income) as currency in millions
    ax2.yaxis.set_major_formatter(
        FuncFormatter(lambda x, pos: f"${x / 1_000_000:.2f}m")
    )
    
    plt.title("Monthly Stock Price vs Net Income")
    fig.tight_layout()
    plt.show()

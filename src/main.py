# Import database connection utilities
from database import create_connection, close_connection

# Import pandas-based analysis functions
from pandas_analysis import (
    load_sql_data,
    add_year_column,
    yearly_performance_summary,
    stock_price_correlation,
    performance_change
)

# Import SQL analysis functions
from sql_analysis import (
    top_net_income,
    top_net_interest_margin,
    average_roa,
    average_roe,
    negative_net_income_periods,
    yearly_average_net_income,
    yearly_average_nim,
    lowest_cost_to_income,
    highest_stock_price,
    yearly_average_stock_price
)

# Import visualization functions
from visualisations import (
    plot_net_income,
    plot_nim_trend,
    plot_profitability_ratios,
    plot_cost_to_income,
    plot_stock_price_vs_performance
)

# Path to financial database
path = "database/financial_performance.db"

def main():
    # Establish connection to financial database
    connection = create_connection(path)

    # Load financial data from database and prepare it
    dataframe = load_sql_data(connection)
    dataframe = add_year_column(dataframe)

    # === SQL ANALYSIS SECTION ===
    print("\n--- SQL ANALYSIS ---")

    # Display top performing periods by net income
    print("\nTop 5 Net Income Periods:")
    print(top_net_income(connection))

    # Display top performing periods by net interest margin
    print("\nTop 5 Net Interest Margin Periods:")
    print(top_net_interest_margin(connection))

    # Display average return on assets
    print("\nAverage ROA:")
    print(average_roa(connection))

    # Display average return on equity
    print("\nAverage ROE:")
    print(average_roe(connection))

    # Display periods with negative net income
    print("\nNegative Net Income Periods:")
    print(negative_net_income_periods(connection))

    # Display yearly average net income trends
    print("\nYearly Average Net Income:")
    yearly_average_net_income(connection)

    # Display yearly average net interest margin trends
    print("\nYearly Average Net Interest Margin:")
    yearly_average_nim(connection)

    # Display periods with lowest cost-to-income ratios (most efficient)
    print("\nLowest Cost-to-Income Periods:")
    print(lowest_cost_to_income(connection))

    # Display periods with highest stock prices
    print("\nHighest Stock Price Periods:")
    print(highest_stock_price(connection))

    # Display yearly average stock price trends
    print("\nYearly Average Stock Price:")
    yearly_average_stock_price(connection)

    # === PANDAS ANALYSIS SECTION ===
    print("\n--- PANDAS ANALYSIS ---")

    # Calculate and display yearly performance summary statistics
    print("\nYearly Performance Summary:")
    print(yearly_performance_summary(dataframe))

    # Calculate and display correlations between stock price and financial metrics
    print("\nStock Price Correlations:")
    stock_price_correlation(dataframe)

    # Calculate percentage change in metrics between 2022 and 2023
    print("\nPerformance Change:")
    changes = performance_change(dataframe)

    # Display percentage changes for each metric
    for metric, change in changes:
        print(f"{metric}: {change}%")

    # === VISUALIZATION SECTION ===
    # Generate visualization charts
    plot_net_income(dataframe)
    plot_nim_trend(dataframe)
    plot_profitability_ratios(dataframe)
    plot_cost_to_income(dataframe)
    plot_stock_price_vs_performance(dataframe)

    # Close database connection
    close_connection(connection)

if __name__ == "__main__":
    main()
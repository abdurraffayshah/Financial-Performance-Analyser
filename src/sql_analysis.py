from database import create_connection

path = "database/financial_performance.db"

connection = create_connection(path)

def top_net_income(conn):
    """Return the five periods with the highest net income."""
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT date, net_income FROM financial_data ORDER BY net_income DESC LIMIT 5
                   ''')
    return cursor.fetchall()

def top_net_interest_margin(conn):
    """Return the five periods with the highest net interest margin."""
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT date, net_interest_margin FROM financial_data ORDER BY net_interest_margin DESC LIMIT 5
                   ''')
    return cursor.fetchall()

def average_roa(conn):
    """Return the average return on assets rounded to two decimal places."""
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT AVG(return_on_assets) FROM financial_data
                   ''')
    return round(cursor.fetchone()[0], 2)

def average_roe(conn):
    """Return the average return on equity rounded to two decimal places."""
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT AVG(return_on_equity) FROM financial_data
                   ''')
    return round(cursor.fetchone()[0], 2)


def negative_net_income_periods(conn):
    """Return all periods where net income was negative."""
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT date, net_income FROM financial_data WHERE net_income < 0
                   ''')
    
    return cursor.fetchall()


def yearly_average_net_income(conn):
    """Print the average net income for each year, rounded to two decimals."""
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT strftime("%Y", date), AVG(net_income) FROM financial_data GROUP BY strftime("%Y", date)
                   ''')
    results = cursor.fetchall()
    rounded_results = []

    # Round each yearly average after fetching the query results.
    for year, avg in results:
        rounded_results.append((year, round(avg, 2)))
    
    for output_year, output_average in rounded_results:
        print(f"{output_year}: {output_average}")



def yearly_average_nim(conn):
    """Print yearly average net interest margin (rounded)."""
    cursor = conn.cursor()

    # Query: average net_interest_margin grouped by year
    cursor.execute('''
                    SELECT strftime("%Y", date), AVG(net_interest_margin)
                    FROM financial_data
                    GROUP BY strftime("%Y", date)
                    ''')
    results = cursor.fetchall()
    rounded_results = []

    #rounding the results and adding them to the rounded_list list
    for year, avg in results:
        rounded_results.append((year, round(avg, 2)))

    #outputting the results
    for output_year, output_result in rounded_results:
        print(f"{output_year}: {output_result}")


def lowest_cost_to_income(conn):
    """Lowest 5 cost-to-income ratio periods."""
    cursor = conn.cursor()
    # Query: lowest cost_to_income_ratio values
    cursor.execute('''
                    SELECT date, cost_to_income_ratio
                    FROM financial_data
                    ORDER BY cost_to_income_ratio ASC LIMIT 5
                    ''')
    return cursor.fetchall()


def highest_stock_price(conn):
    """Top 5 stock price periods."""
    cursor = conn.cursor()
    # Query: top stock_price values
    cursor.execute('''
                    SELECT date, stock_price
                    FROM financial_data
                    ORDER BY stock_price DESC LIMIT 5
                    ''')
    return cursor.fetchall()


def yearly_average_stock_price(conn):
    """Print yearly average stock price (rounded)."""
    cursor = conn.cursor()
    # Query: average stock_price grouped by year
    cursor.execute('''
                    SELECT
                        strftime("%Y", date) as year,
                        AVG(stock_price)
                    FROM financial_data
                    GROUP BY year
                    ORDER BY year
                    ''')
    results = cursor.fetchall()
    rounded_results = []

    #rounding the results and adding them to the rounded_list list
    for year, result in results:
        rounded_results.append((year, round(result, 2)))

    #outputting the results
    for output_y, output_r in rounded_results:
        print(f"{output_y}: {output_r}")



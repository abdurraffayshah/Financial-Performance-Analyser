import sqlite3 as sq
from database import create_connection, close_connection, insert_data

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


yearly_average_net_income(connection)
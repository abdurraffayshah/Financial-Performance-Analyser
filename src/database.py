import sqlite3 as sq

path = "database/financial_performance.db"

def create_connection(db_file):
    '''
    Create a database connection to the SQLite database specified by db_file.
    '''
    return sq.connect(db_file)

def close_connection(conn):
    '''
    Close the database connection.
    '''
    if conn:
        conn.close()



def create_table(conn):
    '''
    Create the financial_data table in the database if it doesn't already exist.
    '''
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS financial_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL UNIQUE,
        interest_income REAL,
        interest_expense REAL,
        average_earning_assets REAL,
        net_income REAL,
        total_assets REAL,
        shareholder_equity REAL,
        operating_expenses REAL,
        operating_income REAL,
        market_share REAL,
        stock_price REAL,
        net_interest_income REAL,
        net_interest_margin REAL,
        return_on_assets REAL,
        return_on_equity REAL,
        cost_to_income_ratio REAL
    )
''')
    


def insert_data(conn, data):
    '''
    Insert data from a CSV file into the financial_data table.
    '''
    cursor = conn.cursor()

    # Read the CSV file and insert data into the table
    with open(data, 'r') as file:
        for line in file:
            if line.startswith('date'):
                continue
            line = line.strip().split(',')
            for i in range(len(line)):
                if line[i] == '':
                    line[i] = None
            cursor.execute('''
            INSERT OR IGNORE INTO financial_data (date, interest_income, interest_expense, average_earning_assets, net_income, total_assets, shareholder_equity, operating_expenses, operating_income, market_share, stock_price, net_interest_income, net_interest_margin, return_on_assets, return_on_equity, cost_to_income_ratio) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', line)
        conn.commit()



def verify_data(conn):
    '''
    Verify that the data has been inserted correctly by fetching and printing a few rows from the financial_data table.
    '''
    cursor = conn.cursor()

    # Fetch and print the first 7 rows from the financial_data table
    cursor.execute('SELECT * FROM financial_data LIMIT 7')
    for row in cursor.fetchall():
        print(row)

import pandas as pd
import numpy as np

path = 'data/raw/myusabank.csv'

def load_data(file_path):
    '''
    Load data from a CSV file and return a pandas DataFrame.
    '''
    df = pd.read_csv(file_path)
    return df

# Load the data from the CSV file
dataFrame = load_data(path)

def inspect_data(df):
    '''
    Inspect the DataFrame and print information about each column, including data type, number of null values, number of duplicates, and statistics.
    '''

    # Get the list of columns in the DataFrame
    list_of_columns = df.columns.tolist()

    # Initialize lists to store information about each column
    numberOfNullValues = []

    # Initialize lists to store information about each column
    numberOfDuplicates = []

    # Initialize lists to store statistics for each column
    statistics = []

    # Get the data types of each column in the DataFrame
    dataTypes = df.dtypes.tolist()

    # Get the numeric columns in the DataFrame
    numeric_columns = df.select_dtypes(include="number").columns

    # Loop through each column in the DataFrame and gather information about null values, duplicates, and statistics
    for i in list_of_columns:
        nullValue = int(pd.isnull(df[i]).sum())
        numberOfNullValues.append((nullValue))
        duplicates = df[i].duplicated().sum()
        numberOfDuplicates.append((int(duplicates)))
        stats = df[i].describe()
        if i in numeric_columns:
            stats = stats.round(2)
        stats_list = stats.values.tolist()
        statistics.append(stats_list)

    # Print the gathered information for each column
    for count in range(len(list_of_columns)):
        print(f"Column: {list_of_columns[count]}")
        print(f"Data Type: {dataTypes[count]}")
        print(f"Number of Null Values: {numberOfNullValues[count]}")
        print(f"Number of Duplicates: {numberOfDuplicates[count]}")
        if list_of_columns[count] in df.select_dtypes(include="number").columns:
            print("Statistics:")
            print(
                f"Count: {statistics[count][0]}"
                f"\nMean: {statistics[count][1]}"
                f"\nStd: {statistics[count][2]}"
                f"\nMin: {statistics[count][3]}"
                f"\n25%: {statistics[count][4]}"
                f"\n50%: {statistics[count][5]}"
                f"\n75%: {statistics[count][6]}"
                f"\nMax: {statistics[count][7]}"
                "\n"
            )
        else:
            print("Statistics:")
            print(
                f"Count: {statistics[count][0]}"
                f"\nUnique: {statistics[count][1]}"
                f"\nTop: {statistics[count][2]}"
                f"\nFreq: {statistics[count][3]}"
                "\n"
            )

        
def clean_columns_name(df):
    '''
    Clean the column names of the DataFrame by stripping whitespace, converting to lowercase, and replacing spaces with underscores.
    '''

    # Get the list of columns in the DataFrame
    list_of_columns = df.columns.tolist()

    # Initialize a list to store the cleaned column names
    clean_columns = []

    # Loop through each column name, clean it and add it to the list of cleaned column names
    for column in list_of_columns:
        column = column.strip().lower()
        column = column.replace(' ', '_')
        clean_columns.append(column)
    
    # Set the cleaned column names back to the DataFrame and return the cleaned DataFrame
    df.columns = clean_columns
    return df

# Clean the column names of the DataFrame
dataFrame = clean_columns_name(dataFrame)

def remove_duplicates(df):
    '''
    Remove duplicate rows from the DataFrame.
    '''
    df = df.drop_duplicates()
    return df

# Remove duplicate rows from the DataFrame
dataFrame = remove_duplicates(dataFrame)

def handle_missing_values(df):
    '''
    Handle missing values in the DataFrame by dropping rows with null values in the 'date' column and dropping rows with 7 or more null values in other columns.
    '''

    # Loop through each row in the DataFrame and check for missing values
    for i, rows in df.iterrows():
        count=0
        # Check if the 'date' column is null and drop the row if it is
        if pd.isnull(rows['date']):
                df.drop(i, inplace=True)
                continue
        # Count the number of null values in the row and drop the row if there are 7 or more null values
        for column, values in rows.items():
            if pd.isnull(values):
                count += 1
        if count>=7:
            df.drop(i, inplace=True)  
    return df

# Handle missing values in the DataFrame
dataFrame = handle_missing_values(dataFrame)

def fix_data_types(df):
    '''
    Fix the data types of the columns in the DataFrame by converting the 'date' column to datetime and downcasting numeric columns to float.
    '''

    # Convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Downcast numeric columns to float to save memory
    list_of_columns = df.columns.tolist()
    for name in list_of_columns:
        if name != 'date':
            df[name] = pd.to_numeric(df[name], downcast='float')
    return df

# Fix the data types of the columns in the DataFrame
dataFrame = fix_data_types(dataFrame)

def handle_invalid_values(df):
    '''
    Handle invalid values in the DataFrame by replacing negative values with NaN for all columns except 'date', 'net_income', 'operating_income', 'shareholder_equity' and 'market_share'. For the 'market_share' column, replace values less than 0 or greater than 100 with NaN.
    '''

    # Get the list of columns in the DataFrame
    list_of_columns = df.columns.tolist()

    # Loop through each column and replace invalid values with NaN
    for name in list_of_columns:
        if name != 'date' and name != 'net_income' and name != 'operating_income' and name != 'shareholder_equity' and name != 'market_share':
            df.loc[df[name] < 0, name] = np.nan
        elif name == 'market_share':
            df.loc[(df[name] < 0) | (df[name] > 100), name] = np.nan
    return df
                
# Handle invalid values in the DataFrame and then handle missing values again to remove any rows that may have been affected by the invalid value handling
dataFrame = handle_invalid_values(dataFrame)
dataFrame = handle_missing_values(dataFrame)

def check_outliers(df):
    '''
    Check for outliers in the DataFrame using the Interquartile Range (IQR) method for all columns except 'date' and 'market_share'. For the 'market_share' column, check for values less than 0 or greater than 100. Print a report of any outliers found.
    '''

    # Get the list of columns in the DataFrame
    list_of_columns = df.columns.tolist()

    # Initialize a list to store the outlier report
    report = []

    # Loop through each column and check for outliers using the IQR method or the specified bounds for 'market_share'
    for name in list_of_columns:
        if name != 'date' and name != 'market_share':
            l_quartile = df[name].quantile(0.25)
            u_quartile = df[name].quantile(0.75)
            iqr = u_quartile - l_quartile
            l_bound = l_quartile - (1.5 * iqr)
            u_bound = u_quartile + (1.5 * iqr)
            outliers = df.loc[(df[name] < l_bound) | (df[name] > u_bound), name]
            if not outliers.empty:
                report.append([name, l_bound, u_bound, outliers.count(), outliers.tolist()])

        elif name == 'market_share':
            l_bound = 0
            u_bound = 100
            outliers = df.loc[(df['market_share'] < l_bound) | (df['market_share'] > u_bound), 'market_share']
            if not outliers.empty:
                report.append([name, l_bound, u_bound, outliers.count(), outliers.tolist()])

    # Print the outlier report
    for index in range(len(report)):
        print (
            f"Column: {report[index][0]}"
            f"\nLower Bound: {report[index][1]}"
            f"\nUpper Bound: {report[index][2]}"
            f"\nNumber of Outliers: {report[index][3]}"
            f"\nOutliers: {report[index][4]}"
            "\n"
        )

# Call the function to check for outliers in the DataFrame
#check_outliers(dataFrame)

def create_financial_metrics(df):
    '''
    Create financial metrics in the DataFrame, including net interest income, net interest margin, return on assets, return on equity, and cost to income ratio.
    '''

    # Calculate net interest income and insert it into the DataFrame
    net_interest_income = df['interest_income'] - df['interest_expense']
    df.insert(len(df.columns), 'net_interest_income', net_interest_income.round(2))

    # Calculate net interest margin and insert it into the DataFrame
    net_interest_margin =  (net_interest_income / df['average_earning_assets']) * 100
    df.insert(len(df.columns), 'net_interest_margin', net_interest_margin.round(2))

    # Calculate return on assets and insert it into the DataFrame
    return_on_assets = (df['net_income'] / df['total_assets']) * 100
    df.insert(len(df.columns), 'return_on_assets', return_on_assets.round(2))

    # Calculate return on equity and insert it into the DataFrame
    return_on_equity = (df['net_income'] / df['shareholder_equity']) * 100
    df.insert(len(df.columns), 'return_on_equity', return_on_equity.round(2))

    # Calculate cost to income ratio and insert it into the DataFrame
    cost_to_income_ratio = (df['operating_expenses'] / df['operating_income']) * 100
    df.insert(len(df.columns), 'cost_to_income_ratio', cost_to_income_ratio.round(2))

    # Return the DataFrame with the new financial metrics
    return df

dataFrame = create_financial_metrics(dataFrame)

def validate_data(df):
    '''
    Validate the DataFrame by checking for duplicates, missing dates, valid data types, invalid values, market share bounds, existence of financial metrics, and whether the DataFrame is empty. Print a validation report.
    '''

    #Initiate Validation Dictionary
    validate = {
        "duplicates": None,
        "missing_dates": None,
        "valid_datatypes": None, 
        "Invalid_values": None,
        "market_share": None, 
        "Financial_metrics": None, 
        "dataframe_empty": None
    }

    # Check for duplicates
    duplicates = df[df.duplicated()]

    if not duplicates.empty:
        validate["duplicates"] = False
    else:
        validate["duplicates"] = True


    # Check for missing dates
    if df['date'].isnull().any():
        validate["missing_dates"] = False
    else:
        validate["missing_dates"] = True

    # Check data types
    validate["valid_datatypes"] = True

    for name in df.columns:
        if name != 'date':
            if not pd.api.types.is_numeric_dtype(df[name]):
                validate["valid_datatypes"] = False
        elif name == 'date':
            if df[name].dtype != 'datetime64[ns]':
                validate["valid_datatypes"] = False

    # Check for invalid negative values
    validate["Invalid_values"] = True

    for name in df.columns:
        if (
            name != 'date'
            and name != 'net_income'
            and name != 'operating_income'
            and name != 'shareholder_equity'
            and name != 'market_share'
            and name != 'net_interest_income'
            and name != 'net_interest_margin'
            and name != 'return_on_assets'
            and name != 'return_on_equity'
            and name != 'cost_to_income_ratio'
        ):
            if (df[name] < 0).any():
                validate["Invalid_values"] = False


    # Check market share
    if ((df['market_share'] < 0) | (df['market_share'] > 100)).any():
        validate["market_share"] = False
    else:
        validate["market_share"] = True


    # Check financial metric columns exist
    financial_metrics = [
        'net_interest_income',
        'net_interest_margin',
        'return_on_assets',
        'return_on_equity',
        'cost_to_income_ratio'
    ]
    validate["Financial_metrics"] = True
    for metric in financial_metrics:
        if metric not in df.columns:
            validate["Financial_metrics"] = False


    # Check DataFrame is not empty
    if df.empty:
        validate["dataframe_empty"] = False
    else:
        validate["dataframe_empty"] = True


    # Print validation report
    for key, value in validate.items():
        if value == True:
            print(f"{key} validation passed.")
        else:
            print(f"{key} validation failed.")

validate_data(dataFrame)

path = "data/processed"

def save_date(df, path):
    '''
    Save the DataFrame to a CSV file in the specified path.
    '''
    df.to_csv(f"{path}/cleaned_data.csv", index=False)

save_date(dataFrame, path)
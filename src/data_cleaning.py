import pandas as pd
import numpy as np

path = '/Users/raffay/Desktop/Financial Performance Analyser/data/raw/myusabank.csv'

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

dataFrame = load_data(path)

def inspect_data(df):
    list_of_columns = df.columns.tolist()
    numberOfNullValues = []
    numberOfDuplicates = []
    statistics = []
    dataTypes = df.dtypes.tolist()
    numeric_columns = df.select_dtypes(include="number").columns
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
    list_of_columns = df.columns.tolist()
    clean_columns = []
    for column in list_of_columns:
        column = column.strip().lower()
        column = column.replace(' ', '_')
        clean_columns.append(column)
    df.columns = clean_columns
    return df

dataFrame = clean_columns_name(dataFrame)

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

dataFrame = remove_duplicates(dataFrame)

def handle_missing_values(df):
    for i, rows in df.iterrows():
        count=0
        if pd.isnull(rows['date']):
                df.drop(i, inplace=True)
                continue
        for column, values in rows.items():
            if pd.isnull(values):
                count += 1
        if count>=7:
            df.drop(i, inplace=True)  
    return df

dataFrame = handle_missing_values(dataFrame)

def fix_data_types(df):
    df['date'] = pd.to_datetime(df['date'])
    list_of_columns = df.columns.tolist()
    for name in list_of_columns:
        if name != 'date':
            df[name] = pd.to_numeric(df[name], downcast='float')
    return df

dataFrame = fix_data_types(dataFrame)

def handle_invalid_values(df):
    list_of_columns = df.columns.tolist()
    for name in list_of_columns:
        if name != 'date' and name != 'net_income' and name != 'operating_income' and name != 'shareholder_equity' and name != 'market_share':
            df.loc[df[name] < 0, name] = np.nan
        elif name == 'market_share':
            df.loc[(df[name] < 0) | (df[name] > 100), name] = np.nan
    return df
                

dataFrame = handle_invalid_values(dataFrame)
dataFrame = handle_missing_values(dataFrame)

def check_outliers(df):
    list_of_columns = df.columns.tolist()
    report = []
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

    for index in range(len(report)):
        print (
            f"Column: {report[index][0]}"
            f"\nLower Bound: {report[index][1]}"
            f"\nUpper Bound: {report[index][2]}"
            f"\nNumber of Outliers: {report[index][3]}"
            f"\nOutliers: {report[index][4]}"
            "\n"
        )

check_outliers(dataFrame)
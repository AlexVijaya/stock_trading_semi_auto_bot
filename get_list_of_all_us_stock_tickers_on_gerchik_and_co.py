import os
import pandas as pd

# Get current directory
current_directory = os.getcwd()

# File path
def get_list_of_us_stock_tickers_from_gerchik_and_co():
    file_path = os.path.join(current_directory,
                             'datasets',
                             'Asset_specification',
                             'Спецификация_инструментов_на_gerchik_and_co.xlsx')

    # Load xlsx file
    df = pd.read_excel(file_path, sheet_name='cfds_on_us_stocks', index_col=0)
    df = df.reset_index()



    # Get the 'Символ' column
    symbol_column = df['Символ']

    # Remove '.us' from each element
    symbol_column = symbol_column.str.replace('.us','',regex=False)
    df['ticker'] = symbol_column
    df = df.rename(columns=lambda x: x.replace(' ', '_'))
    print('df')
    print(df.to_string())


    # Convert the column to a list
    symbol_list = symbol_column.tolist()

    print(symbol_list)
    return df,symbol_list

if __name__=="__main__":
    get_list_of_us_stock_tickers_from_gerchik_and_co()


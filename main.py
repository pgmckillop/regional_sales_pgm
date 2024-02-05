import pandas as pd
from matplotlib import pyplot as plt

# Import the data into a DataFrame
sales = pd.read_csv('regional_sales.csv')


# Modularised main menu
def main_menu():
    print("\t\t**** Welcome to the Dashboard ****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('9) Exit the program')

    choice = int(input("\n  Enter a menu number: "))
    return choice


# Return all data in the regional_sales DataFrame
def all_data():
    print(sales)


# Regional data analysis
def average_regional_sales(region_selected, start_date_selected, end_date_selected):
    # Split - Apply
    sales_filters = sales.loc[:, 'Id':'Region']
    # TODO: Debug check
    print(sales_filters)
    # Split - Apply
    sales_range = sales.loc[:, start_date_selected:end_date_selected]
    # Combine into the data filtered by region and dates
    result = pd.concat([sales_filters, sales_range], axis=1, join='inner')
    result = result.where(sales_filters["Region"] == region_selected)
    # Cast as a DataFrame
    result = pd.DataFrame(result)
    # Munge empty cells as good practice
    result.dropna(inplace=True)
    # Show the data in the terminal
    # TODO: Debug check
    print(result)

    # PLOTTING
    average_sales = sales_range.mean()
    plt.style.use('ggplot')
    average_sales.plot(kind='bar', title='average regional sales')
    plt.show()
    return result







































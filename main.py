# ********************************
# Application:      Regional Sales prototype
# Date:             February 2024
# Purpose:          Proof of concept for video training
# Author            Paul McKillop
# ********************************

# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
# import datetime
# import numpy as np

# Import the data into a DataFrame
sales = pd.read_csv('regional_sales.csv')
sales2 = pd.read_csv('regional_sales_2.csv')

# Modularised main menu
def main_menu():
    print()
    print("\t\t**** Welcome to the Dashboard ****")
    print("\t\t*** ENTER A MENU CHOICE NUMBER ***")
    print()
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Perform enhanced search')
    print('4) Highest Team sales over time')
    print('5) Total  Period Sales')
    print('6) Single Team sales over time')
    print('7) Teams sales over time')
    print('8) Rank Team sales over time')
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
    # Apply-Combine
    # The use of apply is where the region filter is set from the arguments given
    # Combine into the data filtered by region and dates
    result = pd.concat([sales_filters, sales_range], axis=1, join='inner')
    result = result.where(sales_filters["Region"] == region_selected)
    # Cast as a DataFrame
    result = pd.DataFrame(result)
    # Munge empty cells as good practice
    result.dropna(inplace=True)
    # Show the data in the terminal

    # PLOTTING
    average_sales = sales_range.mean()
    plt.style.use('ggplot')
    average_sales.plot(kind='bar', title='average regional sales')
    plt.show()
    return result


# *****************************************************************
# MENU OPTION 3: ENHANCED SEARCH
# *****************************************************************
# For the enhanced search feature I am going to modularise the code
# to the Highest practical extent given the time allowed in line with the planning
# documentation
# I will do this to make the code more secure, robust and maintainable.
# If I have time I will Modularise, perhaps not exactly in this order:
#   1.  Provision to print a list of valid region names to improve the UX when filtering
#           and reduce user errors.
#   2.  Ditto for product types
#   3.  Ditto for the Sales Teams
#   4.  Function to return a validated region name
#   5.  Function to return a validated product type name
#   6.  Function to return a validated Sales Team
#   7.  Functions to return validated start and end dates
#   8.  Class to hold the validated data needed for the enhanced search:
#           Region, Type of product, Sales Team.
#   9.  Function to populate the Class object instance with validated data harvested
#   10. Function to carry out the search and show the outcome
#
# In a perfect world, I would then refactor the code for Menu option 2 to use these features.
# I would also would modularise features into separate files and folders. I won't have time to do that, I think.


# 1. List of regions
def print_valid_regions():
    # Get the column values.
    regions = sales2["Region"].values
    # Use set() to return the unique options
    unique_regions = list(set(regions))
    # Tell the user what the unique value options are to reduce errors and improve UX
    print('The available regions are: ')
    # Loop and return each unique value
    for r in unique_regions:
        print(f"\t{r}")


# 2. List of product types
# Same strategy so no comments required
def print_valid_product_types():
    types = sales2["Type"].values
    unique_types = list(set(types))
    print("The available product types are: ")
    for t in unique_types:
        print(f"\t{t}")

#   3.  list of Sales Teams
def print_valid_sales_teams():
    teams = sales2['Sales_Team'].values
    unique_teams = list(set(teams))
    print("The available Sales Teams are: ")
    for t in unique_teams:
        print(f"\t{t}")

# Display menu when application launches
x = main_menu()

# Control loop to allow menu display
while x == 1 or x == 2 or x == 3 or x == 4 or x ==5 or x == 6 or x == 7 or x == 8 or x == 9 :
    if x == 1:
        all_data()
    elif x == 2:
        # print a spacer line
        print()
        # Get the region wanted
        region = input("Please enter the name of the region you would like to check: ")
        # Allow for casing differences
        region = region.lower()
        # Check valid region
        if region in sales["Region"].str.lower().values:
            # Get the dates
            while True:
                start_date = input("PLEASE ENTER A START DATE AS 01-Mmm: ")
                # Check valid start date
                if start_date not in sales.columns:
                    print("ERROR: Start date not found")
                else:
                    while True:
                        end_date = input("PLEASE ENTER AN END DATE AS 01-Mmm: ")
                        # check valid end date
                        if end_date not in sales.columns:
                            print("ERROR: End date not found")
                        else:
                            # Use the modularised analysis method
                            average_regional_sales(region, start_date, end_date)
                            break
                    break
            break
        else:
            print("region not in the data set")
    elif x == 3:
        # Enhanced search
        print()
        print("Enhanced search selected")
    elif x == 4:
        # Team performance
        print()
        print("Team performance selected")
    elif x == 5:
        # Region performance
        print()
        print("Region performance selected")
    elif x == 6:
        # Plot team sales over time
        print()
        print("Single Team sales analysis selected")
    elif x == 7:
        # all teams sales analysis
        print()
        print("All teams sales analysis selected")
    # Handle the exit choice
    elif x == 8:
        # Rank the sales for teams by date
        print()
        print("Rank Team sales selected")
    elif x == 9:
        print("Exit option selected. Leaving the application")
        break
    x = main_menu()

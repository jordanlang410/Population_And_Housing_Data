"""
Load in PopChange and Housing csv.
Display options for the user to select specific columns to analyze.
Display the Count, Mean, Standard Deviation, Min, Max, and Histogram
for the selected column/file
"""

import pandas as pd
import matplotlib.pyplot as plt

print("***************** Welcome to the Python Data Analysis App *****************")


def main_menu():
    """Function to print out the user menu"""
    print("\nPlease select the file you want to analyze:")
    print("1: Population Data")
    print("2: Housing Data")
    print("3: Exit the Program")


def population_menu():
    "Function to print out PopChange csv options menu"
    print("Please select the Column you want to analyze:")
    print("1: Pop Apr 1")
    print("2: Pop Jul 1")
    print("3: Change Pop")
    print("4: Exit Column")


def housing_menu():
    "Function to print out Housing csv options menu"
    print("Please select the Column you want to analyze:")
    print("1: AGE ")
    print("2: BEDRMS")
    print("3: BUILT")
    print("4: ROOMS")
    print("5: UTILITY")
    print("6: Exit Column")


def column_data(selection):
    "Function to print out Count, Mean, Standard Deviation, Min, and Max"

    pd.set_option('display.float_format', lambda x: '%.3f' % x)
    column_select = df[selection]
    print("The statistics for this column are: ")
    print(column_select.describe(exclude=['75%']))


def histogram_show(selection):
    "Function to print out histogram for Pop Jul and April 1"

    # add individual code for other histograms to all for custom axis
    df[selection].plot.hist(bins=2000).set_xlim((0, 250000))
    plt.title(selection + " Histogram")
    plt.show()  # Plot histogram


while True:
    main_menu()
    choice = input(">>> ")

    if choice == "1":
        df = pd.read_csv('PopChange.csv')  # load the PopChange csv file in
        print("\nYou have entered Population Data.")
        while True:
            population_menu()
            choice = input(">>> ")

            if choice == "1":
                COLUMN = "Pop Apr 1"
                column_data(COLUMN)
                histogram_show(COLUMN)

            elif choice == "2":
                COLUMN = "Pop Jul 1"
                column_data(COLUMN)
                histogram_show(COLUMN)

            elif choice == "3":
                COLUMN = "Change Pop"
                column_data(COLUMN)

                df[COLUMN].plot.hist(bins=2000).set_xlim((-15000, 25000))
                plt.title(COLUMN + " Histogram")
                plt.show()  # Plot histogram

            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.\n")


    elif choice == "2":
        df = pd.read_csv('Housing.csv')  # load the Housing csv file in
        print("\nYou have entered Housing Data.")
        while True:
            housing_menu()
            choice = input(">>> ")

            if choice == "1":
                COLUMN = "AGE"
                column_data(COLUMN)

                df[COLUMN].plot.hist(bins=50).set_xlim((-20, 100))
                plt.title(COLUMN + " Histogram")
                plt.show()  # Plot histogram

            elif choice == "2":
                COLUMN = "BEDRMS"
                column_data(COLUMN)

                df[COLUMN].plot.hist(bins=8).set_xlim((0, 8))
                plt.title(COLUMN + " Histogram")
                plt.show()  # Plot histogram

            elif choice == "3":
                COLUMN = "BUILT"
                column_data(COLUMN)

                df[COLUMN].plot.hist(bins=10).set_xlim((1900, 2150))
                plt.title(COLUMN + " Histogram")
                plt.show()  # Plot histogram

            elif choice == "4":
                COLUMN = "ROOMS"
                column_data(COLUMN)

                df[COLUMN].plot.hist(bins=10).set_xlim((0, 20))
                plt.title(COLUMN + " Histogram")
                plt.show()  # Plot histogram

            elif choice == "5":
                COLUMN = "UTILITY"
                column_data(COLUMN)

                df[COLUMN].plot.hist(bins=50).set_xlim((-10, 1125))
                plt.title(COLUMN + " Histogram")
                plt.show()  # Plot histogram

            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.\n")


    elif choice == "3":
        print("Thank you for using the program.")
        break

    else:
        print("Invalid choice. Please try again.\n")

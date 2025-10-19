# Automation Pandas
import pandas as pd
import os
from colorama import init, Fore, Style
import time
import sys


# Initialize colorama for Windows support
init(autoreset=True)

# === Animation Functions ===
def type_effect(text, delay=0.002):
    """Prints text with a typing animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
# === Banner Function (Tez Gati Ke Liye) ===
def show_banner():
    """Displays the interactive menu banner instantly."""
    
    # Check if a DataFrame is loaded (to avoid errors if file loading failed)
    # Note: 'df' and 'file_path' must be defined in the global scope 
    # before this function is called inside the main loop.
    if 'df' in globals():
        df_status = f"{Fore.CYAN}Data Loaded: {Fore.GREEN}{file_path} {Fore.YELLOW}{df.shape[0]} rows, {df.shape[1]} cols"
    else:
        df_status = f"{Fore.CYAN}Data Status: {Fore.RED}No file loaded."

    ascii_banner = f"""{Fore.BLUE}{Style.BRIGHT}
================= PANDAS AUTOMATION TOOL =================
{df_status}
----------------------------------------------------------
{Fore.GREEN}  1-8. FILE RECONIZE (Inspect Data)
1. head()   | 2. tail() | 3. describe() | 4. info()
5. shape    | 6. columns| 7. index      | 8. T (Transpose)

9-13. AGGREGATION & STATS (Requires Numeric Column)
9. idxmax() | 10. idxmin() | 11. mean()  | 12. sum()
13. std()

14-17. DATA CLEANING & SORTING
14. isnull() | 15. fillna | 16. dropna | 17. sort_values

18-20. SAVE FILE
18. Save CSV | 19. Save JSON | 20. Save Excel

{Fore.RED}  0. EXIT
==========================================================
"""
    print(ascii_banner)


# --- Main Program ---
while True:
    try:
        file_path = input(f'{Fore.YELLOW}Enter your CSV file name (e.g., data.csv): ')
        df = pd.read_csv(file_path)
        print(f"\n{Fore.GREEN}Successfully loaded '{file_path}'.")
        break # Exit loop once file is loaded
    except FileNotFoundError:
        print(f"{Fore.RED}Error: The file '{file_path}' was not found. Please check the name and location.")
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}")
        exit()

foldername = input(f"{Fore.YELLOW}Enter Your Folder Name to save output: ")
os.makedirs(foldername, exist_ok=True)
# filename variable is now redundant and will be prompted in save options (18-20)


def is_numeric_column(df, column):
    """Checks if a column is numeric and suitable for calculations."""
    return pd.api.types.is_numeric_dtype(df[column])
while True:
    os.system("clear" if os.name != 'nt' else "cls") # Clear screen
    show_banner()

    try:
        choice = input(f"{Fore.CYAN}{Style.BRIGHT}Enter Your Choice (0 to Exit): ")
        if choice == '0':
             print(f"{Fore.RED}Exiting the program. Goodbye! 👋")
             break
        choice = int(choice)
        print("\n" + "="*30)
    except ValueError:
        print(f"{Fore.RED}Invalid input. Please enter a number from the menu.")
        time.sleep(1.5)
        continue

    # Helper function for stat calculation and error handling
    def calculate_stat(operation_name, pandas_func):
        column = input(f"Enter column name to calculate the {operation_name}: ")
        if column not in df.columns:
            print(f"{Fore.RED}Error: Column '{column}' not found.")
        elif not is_numeric_column(df, column):
            print(f"{Fore.RED}Error: Column '{column}' is not numeric and cannot be used for {operation_name}.")
        else:
            try:
                result = pandas_func(df[column])
                if 'idxmax' in operation_name or 'idxmin' in operation_name:
                    print(f"Row with {operation_name} in '{column}':\n", df.loc[result])
                else:
                    print(f"The {operation_name} of '{column}' is: {result}")
            except Exception as e:
                print(f"{Fore.RED}Calculation failed: {e}")

    if choice == 1:
        try:
            range_val = int(input("Enter Your Head Range (e.g., 5): "))
            print(df.head(range_val))
        except ValueError:
            print(f"{Fore.RED}Invalid range. Please enter an integer.")

    elif choice == 2:
        try:
            range_val = int(input("Enter Your Tail Range (e.g., 5): "))
            print(df.tail(range_val))
        except ValueError:
            print(f"{Fore.RED}Invalid range. Please enter an integer.")

    elif choice == 3:
        print(df.describe())

    elif choice == 4:
        print(df.info())
        
    elif choice == 5:
        print(f"Shape: {df.shape}")
    
    elif choice == 6:
        print(f"Columns: {df.columns.tolist()}")

    elif choice == 7:
        print(f"Index: {df.index}")

    elif choice == 8:  
        print(df.T)
        
    # --- Statistics ---
    elif choice == 9:
        calculate_stat("idxmax (max value row index)", pd.Series.idxmax)

    elif choice == 10:
        calculate_stat("idxmin (min value row index)", pd.Series.idxmin)

    elif choice == 11:
        calculate_stat("mean", pd.Series.mean)
    
    elif choice == 12:
        calculate_stat("sum", pd.Series.sum)
    
    elif choice == 13:
        calculate_stat("standard deviation (std)", pd.Series.std)

    # --- Data Cleaning ---
    elif choice == 14:
        print("Null values per column:")
        print(df.isnull().sum())

    elif choice == 15:
        fill_value_input = input("Enter the value to fill missing data with (e.g., 0, 'N/A'): ")
        
        # Determine data type of fill value (try to cast to float)
        try:
            fill_value = float(fill_value_input)
        except ValueError:
            fill_value = fill_value_input
            
        inplace_choice = input("Apply in place (modifies the dataframe)? (True / False): ").lower() == 'true'
        
        # Use a copy if not in place, to provide visual feedback
        if inplace_choice:
            df.fillna(fill_value, inplace=True)
            print(f"{Fore.GREEN}Missing values have been filled in-place with: {fill_value}.")
        else:
            temp_df = df.fillna(fill_value, inplace=False)
            print(f"{Fore.YELLOW}Displaying result (DataFrame not modified):")
            print(temp_df.head())
            print(f"\n{Fore.YELLOW}To permanently apply, choose 'True' for 'Apply in place'.")

    elif choice == 16:
        column = input("Enter column to check for dropping rows (leave blank to drop based on any column): ")
        subset = [column] if column else None
        
        # Add confirmation for dropping data
        confirm = input(f"Are you sure you want to permanently drop rows with missing values {'in ' + column if column else ''}? (yes/no): ").lower()
        
        if confirm == 'yes':
            rows_before = len(df)
            df.dropna(subset=subset, inplace=True)
            rows_after = len(df)
            print(f"{Fore.GREEN}Dropped {rows_before - rows_after} rows. New shape: {df.shape}")
        else:
            print(f"{Fore.YELLOW}Operation cancelled.")
            
    elif choice == 17:
        column = input("Enter column to sort by: ")
        if column in df.columns:
            ascending_choice = input("Sort ascending? (True / False): ").lower() == 'true'
            print(df.sort_values(by=column, ascending=ascending_choice).head())
            print(f"\n{Fore.YELLOW}Displaying top 5 rows of sorted data.")
        else:
            print(f"{Fore.RED}Error: Column '{column}' not found.")
            
    # --- Saving ---
    elif choice in [18, 19, 20]:
        filename = input(f"{Fore.YELLOW}Enter file name (without extension): ")
        
        if choice == 18:
            path = f"{foldername}/{filename}.csv"
            df.to_csv(path, index=False)
            print(f"{Fore.GREEN}File saved successfully to {path}")
        
        elif choice == 19:
            path = f"{foldername}/{filename}.json"
            df.to_json(path, indent=4, orient='records')
            print(f"{Fore.GREEN}File saved successfully to {path}")

        elif choice == 20:
            try:
                path = f"{foldername}/{filename}.xlsx"
                df.to_excel(path, index=False)
                print(f"{Fore.GREEN}File saved successfully to {path}")
            except ImportError:
                print(f"\n{Fore.RED}Error: To save as .xlsx, you need to install 'openpyxl'.")
                print(f"{Fore.YELLOW}Please run: pip install openpyxl")
    else:
        print(f"{Fore.RED}Invalid choice. Please select a valid option from the menu.")

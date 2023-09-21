#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
def generate_random_timeseries_data(proportion_to_delete=0.2):
    # Create a date range for the year 2020,  + 20 business days 
    date_range = pd.date_range(start='2020-01-01', end='2021-01-20', freq='B')  # 'B' for business day frequency

    # Generate random data for each business day
    random_data = np.random.rand(len(date_range)) # generates values from (0,1)

    # Create a DataFrame with the date and the generated random data
    timeseries_data = pd.DataFrame({'Date': date_range, 'Value': random_data})

    # Randomly delete some observations based on the given proportion
    num_observations_to_delete = int(proportion_to_delete * len(timeseries_data))
    indices_to_delete = np.random.choice(timeseries_data.index, num_observations_to_delete, replace=False)
    timeseries_data.drop(indices_to_delete, inplace=True)

    return timeseries_data


# In[3]:


df = generate_random_timeseries_data()


# In[ ]:


df.head()


# In[ ]:


date_range = pd.Index(timeseries_data['Date'])


# In[5]:


import pandas as pd
import numpy as np

def find_nearest_10_business_days_candidate(date, date_range):
    # Find the index of the date in the date_range
    date_index = date_range.get_loc(date)

    # Find the index of the nearest date that is at least 10 business days ahead
    candidate_index = date_index
    while candidate_index < len(date_range) and (date_range[candidate_index] - date_range[date_index]).days < 10:
        candidate_index += 1

    # If the nearest candidate is more than 10 business days ahead or out of bounds, take the previous date
    if candidate_index >= len(date_range) or (date_range[candidate_index] - date_range[date_index]).days >= 10:
        candidate_index -= 1

    return candidate_index


def calculate_10_business_days_returns(timeseries_data):
    # Sort the timeseries_data by Date to ensure it is in ascending order
    timeseries_data.sort_values(by='Date', inplace=True)
    timeseries_data.reset_index(drop=True, inplace=True)

    # Create a date_range using the 'Date' column of the DataFrame
    date_range = pd.Index(timeseries_data['Date'])

    # Initialize a dictionary to store the 10-business-days returns for each unique date
    returns_dict = {}

    # Iterate through the DataFrame to calculate the returns
    for i in range(len(timeseries_data)):
        date = timeseries_data.loc[i, 'Date']
        value_t = timeseries_data.loc[i, 'Value']

        # Find the nearest to 10 business days candidate
        candidate_index = find_nearest_10_business_days_candidate(date, date_range)
        if candidate_index != i:
            value_t_plus_10 = timeseries_data.loc[candidate_index, 'Value']

            # Calculate the return using the provided formula
            D_tnm = date_range[candidate_index]
            D_t = date
            business_days_diff = (D_tnm - D_t).days
            ret = np.log(value_t_plus_10 / value_t) * np.sqrt(10 / business_days_diff)

            # Store the result in the dictionary with the unique date as key
            returns_dict[date] = ret

    # Convert the dictionary to a DataFrame
    results_df = pd.DataFrame(list(returns_dict.items()), columns=['Date', 'Return_10bd'])

    return results_df

# Example usage:
if __name__ == "__main__":
    proportion_to_delete = 0.2
    timeseries_data = generate_random_timeseries_data(proportion_to_delete)
    returns_df = calculate_10_business_days_returns(timeseries_data)
    print(returns_df)


# In[14]:


#Question 2 
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):  # Loop from 2 to number
        if number % i == 0:     # Use modulus operator to check divisibility
            return False
    return True

def find_prime_numbers(start, end):
    prime_numbers = []
    for num in range(start, end):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Test the function
start_range = 1
end_range = 50
expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
result = find_prime_numbers(start_range, end_range)

print(f"Start Range: {start_range}")
print(f"End Range: {end_range}")
print(f"Expected Prime Numbers: {expected_primes}")
print(f"Result: {result}")

if result == expected_primes:
    print("Congratulations! The function is correct.")
else:
    print("Too bad! There's a bug in the function.")


# Stock Portfolio Management
# You have been tasked with developing a stock portfolio management system. The system should allow users to add stocks to their portfolio, buy and sell stocks, calculate the portfolio's value, and perform other related operations.
# 
# Tasks:
# 1.	Create a dictionary to represent the stock portfolio. The keys should be the stock symbols (e.g., 'AAPL', 'GOOG'), and the values should be dictionaries containing information about each stock, such as the number of shares and the purchase price.
# 
# 2.	Implement a function buy_stock() that allows users to buy stocks. The function should take the stock symbol, number of shares, and purchase price as input and add the stock to the portfolio.
# 
# 3.	Implement a function sell_stock() that allows users to sell stocks. The function should take the stock symbol and the number of shares to sell as input and update the portfolio accordingly.
# 
# 4.	Implement a function calculate_portfolio_value() that calculates the current value of the entire stock portfolio based on the current stock prices. Assume current price for any stock is current price = purchase price + [*random number between -20 and 20] % of purchase price.    
# *  e.g., 4.11%, 0%, -7.0%,20.0%, -13.5%, -20.0% etc
# 
# 5.	Implement a function portfolio_performance() that calculates the overall performance of the portfolio. The performance can be measured as the percentage change in the portfolio value from the initial investment value.
# 
# 6.	[Optional] Create a menu-driven program to allow users to interact with the stock portfolio management system. The program should provide options to buy, sell, view portfolio, calculate portfolio value, and check portfolio performance.
# 

# In[ ]:


#Question one 
# Task 1: Create a dictionary to represent the stock portfolio
stock_portfolio = {}
# Task 2: Implement a function buy_stock()
def buy_stock(stock_symbol, num_shares, purchase_price):
    if stock_symbol in stock_portfolio:
        stock_info = stock_portfolio[stock_symbol]
        stock_info['num_shares'] += num_shares
        stock_info['purchase_price'] = purchase_price
    else:
        stock_portfolio[stock_symbol] = {'num_shares': num_shares, 'purchase_price': purchase_price}
# Task 3: Implement a function sell_stock()
def sell_stock(stock_symbol, num_shares_to_sell):
    if stock_symbol in stock_portfolio:
        stock_info = stock_portfolio[stock_symbol]
        num_shares = stock_info['num_shares']
        if num_shares_to_sell <= num_shares:
            stock_info['num_shares'] -= num_shares_to_sell
            if stock_info['num_shares'] == 0:
                del stock_portfolio[stock_symbol]
            return True
        else:
            return False
    else:
        return False
# Task 4: Implement a function calculate_portfolio_value()
import random

def calculate_portfolio_value():
    total_value = 0
    for stock_symbol, stock_info in stock_portfolio.items():
        purchase_price = stock_info['purchase_price']
        current_price = purchase_price + (random.uniform(-20, 20) / 100) * purchase_price
        total_value += current_price * stock_info['num_shares']
    return total_value
# Task 5: Implement a function portfolio_performance()
def portfolio_performance(initial_investment):
    current_value = calculate_portfolio_value()
    performance = ((current_value - initial_investment) / initial_investment) * 100
    return performance
# Task 6: [Optional] Create a menu-driven program
def main():
    while True:
        print("1. Buy Stock")
        print("2. Sell Stock")
        print("3. View Portfolio")
        print("4. Calculate Portfolio Value")
        print("5. Check Portfolio Performance")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            stock_symbol = input("Enter stock symbol: ")
            num_shares = int(input("Enter the number of shares: "))
            purchase_price = float(input("Enter the purchase price: "))
            buy_stock(stock_symbol, num_shares, purchase_price)

        elif choice == 2:
            stock_symbol = input("Enter stock symbol: ")
            num_shares_to_sell = int(input("Enter the number of shares to sell: "))
            if sell_stock(stock_symbol, num_shares_to_sell):
                print("Stock sold successfully.")
            else:
                print("Failed to sell stock. Insufficient shares.")

        elif choice == 3:
            print("Stock Portfolio:")
            for stock_symbol, stock_info in stock_portfolio.items():
                print(f"{stock_symbol}: {stock_info['num_shares']} shares, Purchase Price: {stock_info['purchase_price']}")

        elif choice == 4:
            print("Portfolio Value:", calculate_portfolio_value())

        elif choice == 5:
            initial_investment = float(input("Enter the initial investment value: "))
            print("Portfolio Performance:", portfolio_performance(initial_investment))

        elif choice == 6:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# Question one:Two Sum: Given a sorted array of integers in ascending order, write a function to find two numbers such that they add up closest to a specific target number. 
# Solution should be optimal and provide time complexity of your solution. 
# 

# In[24]:


def two_sum_closest(nums, target): 
    pointer_one, pointer_two = 0, len(nums) - 1
    closest_sum = float('inf')
    result = []

    while pointer_one < pointer_two:
        current_sum = nums[pointer_one] + nums[pointer_two]
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            result = [nums[pointer_one], nums[pointer_two]]

        if current_sum < target:
            pointer_one += 1
        else:
            pointer_two -= 1

    return result

print(two_sum_closest([-1, 2, 3, 4, 5], 1))


# Question 2 :
#     Given an array representing the price of a stock on different days, write a program to find the maximum profit that can be made by buying and selling the stock, with the restriction that you must wait for one day after selling the stock before buying it again.

# In[31]:


def max_profit(prices):
    if not prices:
        return 0

    n = len(prices)
    # Initialize variables to keep track of maximum profit with and without stock
    buy = [-prices[0]] * n
    sell = [0] * n

    for i in range(1, n):
        # Calculate the maximum profit on the current day if we buy or do nothing
        buy[i] = max(buy[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
        # Calculate the maximum profit on the current day if we sell or do nothing
        sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

    return max(sell)


print(max_profit([1, 2, 3, 0, 2]))

# Output: 3 (Buy on day 1 (price = 1) and sell on day 2 (price = 2), buy on day 4 (price = 0) and sell on day 5 (price = 2))


# Question 3 - Write an algorithm to find the first 100 twin primes.
# 

# In[20]:


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_twin_primes(limit):
    twin_primes = []
    n = 3
    count = 0  # Initialize a count of twin primes found
    while count < limit:
        if is_prime(n) and is_prime(n + 2):
            twin_primes.append((n, n + 2))
            count += 1  # Increment the count of twin primes found
        n += 2
    return twin_primes

# Find the first 100 twin primes
twin_prime_list = find_twin_primes(100)

# Print the result
for i in range(len(twin_prime_list)):
    p1, p2 = twin_prime_list[i]
    print(f"Twin Prime {i + 1}: ({p1}, {p2})")


# Question 4 
# What is the time complexity of the following code:
#     Please provide a brief explanation in a few words.
#   ![image.png](attachment:image.png)  

# In[ ]:



The outer loop runs from n/2 to n, which has roughly (n/2) iterations.
The inner loop runs from 2 to n. While it uses pow(2, j) as the step size, j itself varies from 2 to n. So, the inner loop actually performs n - 2 + 1 = n - 1 iterations in total, regardless of the value of n.
Now, combining the two loops, you have roughly (n/2) * (n - 1) iterations, which results in a time complexity of O(n^2)


# Question 5: What is the time complexity of the following code: Please provide a brief explanation in a few words
# ![image.png](attachment:image.png)

# In[ ]:


Outer Loop (First For Loop):

The outer loop runs from 0 to n-1, which means it has n iterations. The variable i takes on values from 0 to n-1.
Inner Loop (Second For Loop):

For each iteration of the outer loop, the inner loop runs from 0 to i-1. In other words, it performs i iterations for each value of i.
The number of iterations:
When i is 0, the inner loop runs 0 times.
When i is 1, the inner loop runs 1 time.
When i is 2, the inner loop runs 2 times.
When i is 3, the inner loop runs 3 times.
...and so on, up to n-1.
To find the total number of iterations, we sum up the number of iterations for each value of i:


0 + 1 + 2 + 3 + ... + (n-1)
This is an arithmetic series sum and can be expressed as (n * (n-1)) / 2. This formula gives us the total number of iterations the code will perform.

So, the time complexity of the given code is O(n^2).


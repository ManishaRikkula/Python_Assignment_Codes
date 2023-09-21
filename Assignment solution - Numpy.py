#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np


# Q1. Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]

# In[12]:



nums = np.array([1, 2, 3, 4])
c = np.prod(nums)
for i in nums:
    t = c/nums
t    
#defining through a function
def product(nums):
    c = np.prod(nums)
    for i in nums:
        t = c/nums
    return t 
product([3,1,5])
product([1, 2, 3, 4])


# In[13]:


#given data 
pnl_grid = {
    506: ([0.465,0.05,0.345,0.629,0.289,0.05,0.243,0.822,0.665,0.856], [-220.983,-217.841,-220.074,-222.224,-219.65,-217.841,np.nan,-223.685,np.nan,-223.942]),
    258: ([0.473,0.232,0.649,0.19,0.962,0.93,0.639,0.059,0.831,0.837], [-653.225,-654.91,-651.994,-655.203,-649.806,-650.03,-652.064,np.nan,-650.722,-650.68]),
    358: ([0.97,0.836,0.031,0.831,0.634,0.56,0.046,0.094,0.202,0.198], [687.434,686.908,683.749,686.888,686.115,685.825,683.808,683.997,684.42,684.405]),
    735: ([0.949,0.326,0.205,0.952,0.543,0.032,0.926,0.826,0.875,0.846], [-426.147,-428.488,-428.943,-426.136,-427.673,-429.593,-426.234,-426.609,np.nan,-426.534]),
    166: ([0.041,0.48,0.575,0.09,0.412,0.12,0.584,0.306,0.981,0.649], [769.374,762.653,761.199,768.624,763.694,np.nan,761.061,np.nan,754.983,760.066]),
    781: ([0.569,0.334,0.102,0.744,0.685,0.546,0.85,0.097,0.791,0.249], [-449.069,-448.246,np.nan,-449.682,np.nan,-448.989,-450.054,-447.416,-449.847,-447.948]),
    789: ([0.864,0.536,0.223,0.578,0.646,0.147,0.401,0.535,0.51,0.69], [477.718,472.913,468.328,473.528,474.525,467.215,470.936,472.899,472.532,475.169]),
    822: ([0.051,0.068,0.386,0.224,0.618,0.969,0.581,0.616,0.405,0.573], [-999.429,-999.695,-1004.679,-1002.14,-1008.315,-1013.816,-1007.735,-1008.284,-1004.977,-1007.61]),
    728: ([0.605,0.18,0.575,0.316,0.723,0.911,0.98,0.291,0.823,0.63], [336.468,332.996,336.223,334.107,np.nan,338.968,339.531,333.903,338.249,336.672]),
    725: ([0.76,0.703,0.223,0.785,0.211,0.48,0.644,0.551,0.871,0.275], [-204.815,-205.658,-212.755,np.nan,-212.933,-208.955,-206.53,-207.905,-203.174,-211.986]),
}

shocks = {
    506: 0.486,
    258: 0.661,
    358: 0.371,
    735: 0.293,
    166: 0.203,
    781: 0.633,
    789: 0.529,
    822: 0.86,
    728: 0.038,
    725: 0.886
}
cutoffs = {
    506: 0.4,
    258: 0.6,
    358: 0.3,
    735: 0.3,
    166: 0.2,
    781: 0.6,
    789: 0.5,
    822: 0.8,
    728: 0.4,
    725: 0.4
}


# Assume you are given a dictionary pnl_grid with they keys representing issuer id and values being a tuple of (shock_list, pnl_list). pnl_list corresponds to pnl obtained by schocks from shock_list. shocks gives us the shocks applied to each issuer.
# 
# Task: Find the pnl for each issuer using the shock from the shocks by interpolating between shock_list and pnl_list. Use CubicSpline from scipy

# In[14]:


shock_greater_than_cutoff = {}
for key, value in shocks.items():
    shock_greater_than_cutoff[key] = value > cutoffs[key]

print("Shock values greater than cutoff:")
print(shock_greater_than_cutoff)


# In[15]:


from scipy.interpolate import CubicSpline

result = {}

for issuer_id, (shock_list, pnl_list) in pnl_grid.items():
    # Remove NaN values from the shock and pnl lists
    valid_indices = np.isfinite(pnl_list)
    valid_shock_list = np.array(shock_list)[valid_indices]
    valid_pnl_list = np.array(pnl_list)[valid_indices]
    
    # Sort the shock and pnl lists based on shock values
    sorted_indices = np.argsort(valid_shock_list)
    sorted_shock_list = valid_shock_list[sorted_indices]
    sorted_pnl_list = valid_pnl_list[sorted_indices]
    
    # Ensure that shock values are strictly increasing
    unique_indices = np.unique(sorted_shock_list, return_index=True)[1]
    sorted_shock_list = sorted_shock_list[unique_indices]
    sorted_pnl_list = sorted_pnl_list[unique_indices]
    
    cs = CubicSpline(sorted_shock_list, sorted_pnl_list)
    interpolated_pnl = cs(shocks[issuer_id])
    result[issuer_id] = interpolated_pnl.tolist()  # Convert NumPy array to Python list

print(result)

#result{issuer_id,interpolated_pnl for each shock}


#  In addition to pnl_grid above, you are also given cutoffs below for every issuer. Assume the issuer defaults if a shock exceeds the cutoff and there are 4 timesteps in a year.
# 
# Task: Calulate the expected default pnl over the next year for each issuer by follwing the simulation(use 1000 sims) below:
# 
# Generate shock for every issuer at each timestep, shocks must lie between 0 and 1 and use issuer id as the seed
# find the scenarios where the issuer defaults
# if an issuer defaults, calculate the deault pnl at that timestep using the shock and the pnl_grid defined above, use your function from Q2
# if an issuer does not default at a timestep, default pnl is zero at that timestep
# if an issuer has defaulted in any of the previous timesteps, default pnl is zero in subsequent timesteps.
# Expected pnl for each issuer is average default pnl across all simulations

# In[16]:


import numpy as np
from scipy.interpolate import CubicSpline


# Simulation parameters
num_simulations = 1000
num_timesteps = 4

# Function to calculate default PNL using cubic spline interpolation
def calculate_default_pnl(shock, issuer_id, pnl_grid):
    x, y = pnl_grid[issuer_id]
    valid_indices = ~np.isnan(y)
    
    # Remove duplicate and non-numeric x and y values
    x_valid = np.array(x)[valid_indices]
    y_valid = np.array(y)[valid_indices]
    unique_indices = np.unique(x_valid, return_index=True)[1]
    x_unique = x_valid[unique_indices]
    y_unique = y_valid[unique_indices]
    
    # Use valid x values for cubic spline interpolation
    cs = CubicSpline(x_unique, y_unique, extrapolate=True)
    default_pnl = cs(shock)
    return default_pnl

# Perform simulations
expected_pnl = {}

for issuer_id, cutoff in cutoffs.items():
    default_pnls = []
    for _ in range(num_simulations):
        issuer_defaulted = False
        total_default_pnl = 0.0
        
        for timestep in range(num_timesteps):
            if not issuer_defaulted:
                shock = np.random.random() #generates a random value between 0 and 1
                if shock > cutoff: #issuer defaults
                    issuer_defaulted = True
                    default_pnl = calculate_default_pnl(shock, issuer_id, pnl_grid)
                    total_default_pnl = default_pnl + total_default_pnl
                else:
                    total_default_pnl += 0.0  # No default PNL for this timestep
            else:
                total_default_pnl += 0.0  # No default PNL after issuer defaults
        
        default_pnls.append(total_default_pnl)
    
    average_default_pnl = np.mean(default_pnls)
    expected_pnl[issuer_id] = average_default_pnl

print("Expected Default PNL for each issuer:")
print(expected_pnl)

print()


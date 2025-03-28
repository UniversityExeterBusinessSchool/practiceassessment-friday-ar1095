#######################################################################################################################################################
# 
# Name:ALTHAF RASHEED
# SID: 740100529
# Exam Date: 28TH MARCH 2025
# Module: PROGRAMMING BUSINESS ANALLYTICS
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-ar1095
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}
# SID : 740100529
# Write your code to process the text and count keyword occurrences

# Select keywords based on SID (first = 7, last = 9)
my_keywords = [keywords[7], keywords[9]]  # ['issues', 'materials']

# Empty dictionary to store keyword counts
keyword_counts = {}    #empty dictionary

# Convert review text to lowercase
lower_reviews = customer_reviews.lower()    # Convert to lowercase for case-insensitive matching

# Loop through selected keywords
for word in my_keywords:  # Loop through the keywords
    # Count occurrences of the keyword in the review text
    count = lower_reviews.count(word.lower())
    # Store the result in the dictionary   #storing result in the dictionary
    keyword_counts[word] = count     # storing each keyword in dictionary with count

# Print the final dictionary
print(keyword_counts)       #print the final dictionary 



##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 29

# Write your function for Gross Profit Margin
def gross_profit_margin(revenue, cost_of_goods_sold):     # Formula for getting gross profit margin (Revenue - Cost of Goods Sold) / Revenue * 100
    return ((revenue - cost_of_goods_sold) / revenue) * 100


# Write your function for Inventory Turnover
def inventory_turnover(cost_of_goods_sold, average_inventory):   # Formula for getting inventory turnover Cost of Goods Sold / Average Inventory
    return cost_of_goods_sold / average_inventory


# Write your function for Customer Retention Rate (CRR)
def customer_retention_rate(end_customers, new_customers, start_customers):  #formula for getting customer retention rate((E - N) / S) * 100
    return ((end_customers - new_customers) / start_customers) * 100        # E means number of customers, N means new customer and s means customer at

# Write your function for Break-even Analysis
def break_even_units(fixed_costs, price_per_unit, variable_cost_per_unit):  # Formula for getting break-even units Fixed Costs / (Price per unit - Variable cost per unit)
    return fixed_costs / (price_per_unit - variable_cost_per_unit)


# Call your functions here

print("Gross Profit Margin:", gross_profit_margin(74, 29))  # revenue = 74, COGS = 29
print("Inventory Turnover:", inventory_turnover(74, 29))    # same values used
print("Customer Retention Rate:", customer_retention_rate(150, 29, 74))  # E = 150, N = 29, S = 74
print("Break-even Units:", break_even_units(74, 100, 29))    # FC = 74, Price/unit = 100, VC/unit = 29



##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here

import numpy as np
import matplotlib.pyplot as plt

# inputting the data 
delivery_cost = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65, 70])
shipment_volume = np.array([500, 480, 450, 420, 400, 370, 340, 310, 290, 250])

#fitting the data to a linear regression model
m, c = np.polyfit(delivery_cost, shipment_volume, 1)

# 3. Predicting the volume at £68 using the equation y = mx + c
cost = 68
predicted_volume = m * cost + c

# find cost cost that maximizes profit
# Assuming profit = delivery_cost * shipment_volume

profits = delivery_cost * shipment_volume      # Calculate profit for each delivery cost
max_profit_index = np.argmax(profits)
optimal_cost = delivery_cost[max_profit_index]  # Get the cost that maximizes profit
max_profit = profits[max_profit_index]       # Get the maximum profit

#print all the results
print("Regression Line: Volume = {:.2f} * Cost + {:.2f}".format(m, c))
print("Predicted Shipment Volume at £68:", predicted_volume)       # Print the predicted shipment volume at £68
print("Optimal Delivery Cost for Maximum Profit: £", optimal_cost)
print("Maximum Profit: £", max_profit)       # Print the maximum profit



##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization
"""
import rand as random
import matplotlib.pyplt as plt

# Generate 100 random numbers between 1 and student ID number
your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [random.randint(your_ID, max_valu) in range(100)]

# Plotting the numbers in a histogram
plt.histogram(random_number, bin=10, edgecolour='blue', alpha=0.7, colour='red')
plt.title="Histogram of 100 Random Numbers"
plt.xlabel="Value Range"
plt.ylabel="Frequency"
plt.grid("True")
plt.show("plot")"""

#Answers

import random  # Fixed import (use 'random' not 'rand')
import matplotlib.pyplot as plt  # Fixed matplotlib import

# Get Student ID from user and convert to integer
your_ID = input("Enter your Student ID: ")
max_value = int(your_ID)

# Generate 100 random numbers between 1 and your student ID number
random_numbers = [random.randint(1, max_value) for _ in range(100)]

# Plotting the numbers in a histogram
plt.hist(random_numbers, bins=10, edgecolor='blue', alpha=0.7, color='red')
plt.title("Histogram of 100 Random Numbers")  # fixed title
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(True)  #grid argument fixed
plt.show()  # shiw call fixed




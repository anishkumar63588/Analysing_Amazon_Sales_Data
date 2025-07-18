#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 13:13:49 2025

@author: Anish
"""

# =============================================================================
# Overview
# A merchant selling goods on Amazon wants a small analysis to be done. On the 
# amazon portal, they export their sales data called sales_data.xlsx.
# =============================================================================

# Importing required libraries
import pandas as pd

# Loading data 
df = pd.read_excel("sales_data.xlsx")
df.head()

# =============================================================================
# Exploring the data
# =============================================================================

# Get summary of data
df.info()
df.describe()
df.columns

# =============================================================================
# Cleaning the data
# =============================================================================

# Checking the null/missing data
df.isnull().sum()

# Dropping the null/missing data and stored in variable called 'df'
df_cleaned_data = df.dropna()

# Verifying the data that null/missing values are dropped or not
df_cleaned_data.isnull().sum()

# =============================================================================
# The merchant wants to have a look at the following:
    
# How many sales have they made with amounts more than 1000
# How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
# The Total Sales by Category
# Average Amount by Category and Status
# Total Sales by Fulfilment and Shipment Type
# They would like the last two tables exported to send to their investors.
# =============================================================================


# How many sales have they made with amounts more than 1000
sales_above_1000 = df[df["Amount"] > 1000]
print("Total sales above amount 1000: ",sales_above_1000)

# How many sales have they made that belong to the Category "Tops" and have a Quantity of 3.
Qty_3_category_top = df[(df["Qty"] == 3) & (df["Category"] == "Top")]
print("Sales belong to Category 'Top' and Quantity of 3: ", Qty_3_category_top)

# The Total Sales by Category
sales_by_category = df.groupby("Category", as_index= False)["Amount"].sum()
sales_by_category = sales_by_category.sort_values("Amount", ascending=False)
print(sales_by_category)

# Average Amount by Category and Status
Average_amt_by_category = df.groupby(["Category", "Status"], as_index= False)["Amount"].mean()
print(Average_amt_by_category)

# Total Sales by Fulfilment and Shipment Type
total_sales_by_fulfilment_and_shipment_type = df.groupby(['Courier Status', 'Fulfilment'], as_index=False)['Amount'].sum()
total_sales_by_fulfilment_and_shipment_type = total_sales_by_fulfilment_and_shipment_type.sort_values("Amount", ascending=False)
print(total_sales_by_fulfilment_and_shipment_type)

#They would like the last two tables exported to send to their investors.
Average_amt_by_category.to_excel("average_sale_by_category_and_status.xlsx", index=False)
total_sales_by_fulfilment_and_shipment_type.to_excel("Total_sales_by_ship_and_fulfil.xlsx", index=False)




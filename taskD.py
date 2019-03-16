# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:56:41 2019

@author: Babita
Task D 
1) Measure how many people are completing a series of steps like Add To Cart and Purchase
   to see how effectively a business is driving conversions. 
2) Make necessary assumptions and aligned sample data sets to perform the task.
"""
#import libraries
import pandas as pd
#loading dataframes
df=pd.read_csv('task4.csv')
#Get list of unique items
atcList=list(set(df["addtocart"].tolist()))
#count dataframe of column 'UserId' i.e 13
cnt=df['UserId'].count()
#loop to check if addtocart is equal to purchase and create a dataset containing true or false accordingly
for i in df['UserId']:
    c= df.addtocart==df.purchase

print("people completing series of steps from add to cart to purchase:")
print(sum(c))
print("Dataset: ")
print(c)
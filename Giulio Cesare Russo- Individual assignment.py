# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 21:08:00 2021

@author: Giulio Cesare
"""

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

#import csv file
df = pd.read_csv ('customer_20.csv')

#create a graph showing customers' frequency & spending
for CustomerID in df:
    plt.scatter(df.monetary, df.frequency)
plt.show()
#create a new column showing average spending per purchase 
df['Avg_spending']=df['monetary']/df['frequency']

#calculate total and average customer revenue for all customers
df.monetary.sum()
print(df.monetary.sum())
average_spending=df.monetary.sum()/3000
print(average_spending)
print(df.monetary.median())

#create a new dataframe with constraint for current shoppers
dfnew=df.loc[(df['frequency'] > df['frequency'].quantile(q = 0.7)) & (df['recency'] < 30)]
dfnew['Avg_spending']=dfnew['monetary']/dfnew['frequency']
print(dfnew)
#calculate total and average customer revenue for current shoppers
dfnew.monetary.sum()
print(dfnew.monetary.sum())
average_spending_Curr=dfnew.monetary.sum()/534
print(average_spending_Curr)

#create a new dataframe with constraint for valuable shoppers
sel_frequency = df['frequency'] > df['frequency'].quantile(q = 0.75)
sel_monetary = df['monetary'] > df['monetary'].quantile(q = 0.75)
dfnew2=df[sel_frequency & sel_monetary]
dfnew2.reset_index(drop=True,inplace=True)
dfnew2['Avg_spending']=dfnew2['monetary']/dfnew2['frequency']
print(dfnew2)
#calculate total and average customer revenue for valuable shoppers
dfnew2.monetary.sum()
print(dfnew2.monetary.sum())
average_spending_Val=dfnew2.monetary.sum()/496
print(average_spending_Val)

#create a new dataframe with constraint for potential high frequency shoppers
dfnew3=df.loc[(df['frequency'] > df['frequency'].quantile(q = 0.7)) & (df['monetary'] < df['monetary'].quantile(q=0.6))]
dfnew3['Avg_spending']=dfnew3['monetary']/dfnew3['frequency']
print(dfnew3)
dfnew3.monetary.sum()
print(dfnew3.monetary.sum())
average_spending3=dfnew3.monetary.sum()/169
print(average_spending3)

#create a new dataframe with constraint for High-spenders low frequency shoppers
dfnew4=df.loc[(df['frequency'] < df['frequency'].quantile(q = 0.6)) & (df['monetary'] > df['monetary'].quantile(q=0.7))]
dfnew4['Avg_spending']=dfnew4['monetary']/dfnew4['frequency']
print(dfnew4)
print(dfnew4.monetary.sum())
average_spending4=dfnew4.monetary.sum()/62
print(average_spending4)

#10 best customers sorted for monetary, frequency, recency and average spending
print(dfnew2.sort_values('monetary', ascending=False).head(10))
print(dfnew2.sort_values('frequency', ascending=False).head(10))
print(dfnew2.sort_values('recency', ascending=True).head(10))

#calculate the average recency for most valuable customers      
mean= dfnew2['recency'].mean()
print(mean)
median=dfnew2['recency'].median()
print(median)

pd.options.mode.chained_assignment = None  # default='warn'

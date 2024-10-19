#!/usr/bin/env python
# coding: utf-8

# In[43]:


# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[44]:


# import files

df1=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data1.csv')
df2=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data2.csv')
df3=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data3.csv')
df4=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data4.csv')
df5=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data5.csv')
df6=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data6.csv')
df7=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data7.csv')
df8=pd.read_csv('http://api.covid19india.org/csv/latest/raw_data8.csv')


# In[45]:


df1.columns


# In[46]:


# get colmns
df1=df1.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df2=df2.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df3=df3.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df4=df4.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df5=df5.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df6=df6.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df7=df7.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]
df8=df8.loc[:,['Num Cases','Date Announced','Age Bracket', 'Gender', 'Detected City','Detected District', 'Detected State','Current Status']]


# In[61]:


# merge all data frames
df=df1.append([df2,df3,df4,df5,df6,df7,df8])
df.head()


# In[62]:


# making seperate colmns for day ,month,year
df['Date Announced'].str.split('/').head()


# In[63]:


# spliting date column into day,month,year
# df['Date Announced'].str.split('/',expand=True)

Date =df['Date Announced'].str.split('/',expand=True)
Date.columns=['Day','Month','Year']
Date.head()


# In[66]:


# df=pd.concat([df,Date],axis=1) # dont't run this again , it will again add columns


# In[67]:


df


# In[68]:


df.to_csv('CovidIndia.csv')


# In[ ]:





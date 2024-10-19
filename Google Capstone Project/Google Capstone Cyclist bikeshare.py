#!/usr/bin/env python
# coding: utf-8

# ## Google Data Analytics Professional Certificate Capstone Project
# 
# > ### By Mohamad Ehthesham S

# > ### Case Study: How Does a Bike-Share Navigate Speedy Success? ![image.png](attachment:image.png)

# * LinkedIn - https://www.linkedin.com/in/-mohamad-ehthesham/overlay/contact-info/
# 
# 
# * Mail-Id - mohammedfaiz0102@gmail.com
# 
# 
# * GitHub - https://github.com/MohamadFaiz0102
# 
# 
# * [Coursera certificate](https://www.coursera.org/account/accomplishments/verify/2JZGFKT33EKR)

# ## Project Introduction

# This case study is the [Capstone Project](https://d3c33hcgiwev3.cloudfront.net/aacF81H_TsWnBfNR_x7FIg_36299b28fa0c4a5aba836111daad12f1_DAC8-Case-Study-1.pdf?Expires=1664755200&Signature=Ytw3RCtk28WupQ44s5lr6tdexZ5~rFjCUURDuNfWP~soWkq3ELgdAf1-OAxw2rd5YQ~fVX8TXhD0-7tV87Gu2vmC0N6IXNLC1V4fn~k3SYEorEIKKfL59Umfu9FRvBKLAIyzPp9PLNASmIN5mTH6bcaabbWyThtAudanbu2CT6k_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A) of [Google Data Analytics Professional Certificate](https://www.coursera.org/professional-certificates/google-data-analytics)
# In this case study I am working as a junior data analyst in the marketing analyst team at Cyclistic, a fictional bike-share company in Chicago.
# 
# **Scenario**
# You are a junior data analyst working in the marketing analyst team at Cyclistic, a bike-share company in Chicago. The director
# of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore,
# your team wants to understand how casual riders and annual members use Cyclistic bikes differently. From these insights,
# your team will design a new marketing strategy to convert casual riders into annual members. But first, Cyclistic executives
# must approve your recommendations, so they must be backed up with compelling data insights and professional data
# visualizations.
# 
# The director of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore, my team wants to understand how casual riders and annual members use Cyclistic bikes differently. From the insights, our team will design a new marketing strategy to convert casual riders into annual members. But first, Cyclistic executives must approve our recommendations, so they must be backed up with compelling data insights and professional data visualizations.
# 
# **In order to**
# answer the key business questions, you will follow the steps of the data analysis process: **ask, prepare, process, analyze,
# share, and act.**

# - The data I used is **Cyclistic’s Historical Trip Data** to analyze and identify trends.
# - The **previous 6 months data**   **[Original Datasets link](https://divvy-tripdata.s3.amazonaws.com/index.html)**   from **2022 March 3 to 2022 August 30** is used for analysis.
# - The data is stored in **CSV files**. Each file contains **one month data**. Thus a total of 6 .csv files.
# - The data is **structured data** ie., Organised data.
# - The datasets have a different name because Cyclistic is a fictional company. For the purposes of this case study, the datasets are **appropriate.**
# - As of data Integrity, its **Accurate, Consistent and Trustworthy.**
# 

# ### Ask
# Three questions will guide the future marketing program:
# 1. How do annual members and casual riders use Cyclistic bikes differently?
# 2. Why would casual riders buy Cyclistic annual memberships?
# 3. How can Cyclistic use digital media to influence casual riders to become members?

# ### Cleaning
# 
# Most of the cleaning process I have done in **MS Excel** like -
# - changing datatypes of datetime to correct format i.e yyy-mm-dd
# - sorting column as per date 
# - removing column and row duplicates from dataset and also removing any inconsistency
# - creating new columns of ride_id_length, 
#     - started_date, ended_date,   
#     - started_time,ended_time,
#     - ride_length_miniutes,
#     - week_day_number,
#     - extraction of day from started_date column 

# ## Process / Clean

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

import datetime as dt

import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


month1=pd.read_csv(r'C:\Users\Faiz\Music\Coursera\part 7\Python\New folder (2)\month1.csv',sep=',',parse_dates=[14,16],encoding='utf-8-sig', usecols= ['ride_id','ride_id_length','rideable_type','started_at','ended_at','start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng','end_lat','end_lng','member_casual','started_date','started_time','ended_date','ended_time','week_day_number','day_name','ride_length','ride_length_minutes'])
month2=pd.read_csv(r'C:\Users\Faiz\Music\Coursera\part 7\Python\New folder (2)\month2.csv',sep=',',parse_dates=[14,16],encoding='utf-8-sig', usecols= ['ride_id','ride_id_length','rideable_type','started_at','ended_at','start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng','end_lat','end_lng','member_casual','started_date','started_time','ended_date','ended_time','week_day_number','day_name','ride_length','ride_length_minutes'])
month3=pd.read_csv(r'C:\Users\Faiz\Music\Coursera\part 7\Python\New folder (2)\month3.csv',sep=',',parse_dates=[14,16],encoding='utf-8-sig', usecols= ['ride_id','ride_id_length','rideable_type','started_at','ended_at','start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng','end_lat','end_lng','member_casual','started_date','started_time','ended_date','ended_time','week_day_number','day_name','ride_length','ride_length_minutes'])
month4=pd.read_csv(r'C:\Users\Faiz\Music\Coursera\part 7\Python\New folder (2)\month4.csv',sep=',',parse_dates=[14,16],encoding='utf-8-sig', usecols= ['ride_id','ride_id_length','rideable_type','started_at','ended_at','start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng','end_lat','end_lng','member_casual','started_date','started_time','ended_date','ended_time','week_day_number','day_name','ride_length','ride_length_minutes'])
month5=pd.read_csv(r'C:\Users\Faiz\Music\Coursera\part 7\Python\New folder (2)\month5.csv',sep=',',parse_dates=[14,16],encoding='utf-8-sig', usecols= ['ride_id','ride_id_length','rideable_type','started_at','ended_at','start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng','end_lat','end_lng','member_casual','started_date','started_time','ended_date','ended_time','week_day_number','day_name','ride_length','ride_length_minutes'])
month6=pd.read_csv(r'C:\Users\Faiz\Music\Coursera\part 7\Python\New folder (2)\month6.csv',sep=',',parse_dates=[14,16],encoding='utf-8-sig', usecols= ['ride_id','ride_id_length','rideable_type','started_at','ended_at','start_station_name','start_station_id','end_station_name','end_station_id','start_lat','start_lng','end_lat','end_lng','member_casual','started_date','started_time','ended_date','ended_time','week_day_number','day_name','ride_length','ride_length_minutes'])


# ### Merge all files into one single file

# In[3]:


data=pd.concat([month1,month2,month3,month4,month4,month5,month6],ignore_index=True)


# In[4]:


data.head(2)


# In[5]:


data.info()


# ### Droping unnessary columns

# In[6]:


data.drop(columns=['start_lat','start_lng','end_lat','end_lng'],inplace=True)


# In[7]:


data.head(2)


# ### removing negative values in ride length_minutes

#    - There are negative values in ride_length
#    - Such errors happened because the "ending time" is earlier than the "starting time" in their respective rows.
#    -Number of rows containing "ride length" less than "1" minute.
#    -Any trips that were below 60 seconds in length are potentially false starts or users trying to re-dock a bike to ensure it  was secure

# In[8]:


data[data['ride_length_minutes']<0].count()


# In[9]:


data[data['ride_length_minutes']<1].count()


# - so removing 90929 <1 min  values and negative values 

# In[10]:


# taking only above 1 min values
data = data[data['ride_length_minutes'] >= 1]

data[data['ride_length_minutes']<1].count()


# In[11]:


data.info()


# ### Getting month name from date into seprate column

# In[12]:


data['month_name']=data['started_date'].dt.month_name(locale='English')
data.head(2)


# ## Analyze / Share

# ### - Total distribution of Member and Casual Rider in 6 months

# In[14]:


a1=data.groupby(['member_casual'])['ride_id'].count()
explode=[0.02,0.02]

a1.plot(kind='pie',figsize=(5,5),wedgeprops={'linewidth':0.5,'edgecolor':'black'},colors=('olive','lightblue'),
        startangle=140,autopct='%1.1f%%',shadow=True,labels=None,explode=explode)
plt.legend(labels=a1.index,loc='upper right')

plt.tight_layout();


# ### Total Number of Rides in Each Month

# In[72]:


p1=data.groupby(['month_name','member_casual'])[['ride_id']].count()
p1


# In[67]:


a3=data.groupby(['month_name','member_casual'])['ride_id'].count()
a3.unstack().plot(kind='bar',figsize=(8,6))
plt.style.use("ggplot")
plt.xticks(rotation=360)
plt.tight_layout();


# In[68]:


a3=data.groupby(['month_name','member_casual'])['ride_id'].count()
a3.unstack().plot(kind='line',figsize=(8,6))
plt.style.use("ggplot")
plt.xticks(rotation=360)
plt.tight_layout();


# ### Average ride length in minutes per month

# In[88]:


c1=data.groupby(['member_casual','month_name'])[['ride_length_minutes']].mean().sort_values(by='ride_length_minutes',
                ascending=False)
c1


# In[89]:


plt.figure(figsize=(8,6))

sns.lineplot(x='month_name',y='ride_length_minutes',hue='member_casual', data=c1, palette='viridis')


# In[66]:



c2=data.groupby(['member_casual','month_name'])[['ride_length_minutes']].mean().reset_index()

plt.figure(figsize=(10,6))

order=['March', 'April', 'May', 'June', 'July', 'August']
sns.barplot(x='month_name',y='ride_length_minutes',hue='member_casual', data=c2, palette='viridis',order=order)


# In[18]:


data.head(2)


# In[19]:


a3=data.groupby(['day_name','member_casual'])['ride_id'].count()
a3.unstack().plot(kind='bar',figsize=(8,6))
plt.style.use("ggplot")
plt.xticks(rotation=360)
plt.tight_layout();


# ### Average ride_length in minutes during the week

# In[90]:


a3=data.groupby(['day_name','member_casual'])['ride_length_minutes'].mean()
a3.unstack().plot(kind='bar',figsize = (10,6))
plt.xticks(rotation=360);
#plt.figure()


# ### Total rides per bike type

# In[71]:


d1=data.groupby(['rideable_type','member_casual'])[['ride_id']].count()
d1


# In[21]:


a3=data.groupby(['rideable_type','member_casual'])['ride_id'].count()
a3.unstack().plot(kind='bar',figsize = (8,6))
plt.legend(fontsize=12)
plt.xlabel('rideable_type',fontsize=12)
plt.ylabel('ride_id',fontsize=12)
plt.xticks(rotation=360,fontsize=12)
plt.tight_layout();


# ### Average Ride Length by each user in  6 months

# In[22]:


data.groupby(['member_casual'])[['ride_length_minutes']].mean()


# In[25]:


plt.figure(figsize=(6,6))
sns.barplot(x='member_casual', y='ride_length_minutes', data=data, palette='viridis')


# ### Total rides per bike type per week

# In[27]:


a3=data.groupby(['day_name','rideable_type'])['ride_id'].count()
a3.unstack().plot(kind='bar',figsize = (12,6))
plt.legend(fontsize=12)
plt.xlabel('rideable_type',fontsize=12)
plt.ylabel('ride_id',fontsize=12)
plt.legend(loc='upper left',fontsize=10)
plt.xticks(rotation=360,fontsize=12)
plt.tight_layout();


# ## Conclusion

# * Annual members and Casual riders use Cyclistic bike **share differently.**
# 
# 
# * The **average ride length of casual riders** are more than **twice as of members.**
# 
# 
# * From the average ride length difference, we can conclude that **Annual members usually use bike share** 
# 
#      - **for daily commuting**, while **casual riders** mostly use bike share for **free rides mostly during Weekends**.
#      - and **members users use bike share during weekdays** for their office work or any other work.
#     
#     
# * But there are a **fixed number of casual riders** who use bike share for commuting.

# > ##                                             ** Thank You **
# 
# ### Share you valuable feedback for more improvements

# In[ ]:





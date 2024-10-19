#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Import filtered CSV file

# In[3]:


covid=pd.read_csv('CovidIndia.csv')
covid.head()


# In[4]:


covid.info()


# ### Removing unnecessary columns

# In[5]:


data=covid.iloc[:,1:] # here iloc[rows,colms]
data.head()


# ### Check for null values and % of null values in each columns

# In[6]:


# for null valaues and also check in % in each colms
data.isnull().sum(axis=0).sort_values(ascending=False)/len(data)*100


# In[7]:


data.iloc[1] # it shows rows i.e row 1


# In[8]:


data.loc[[1,23],:] # similarly [rows,colms]


# ### Covid cases Month wise 

# In[99]:


data['Current Status'].unique()


# In[67]:


n=data.groupby('Month')['Num Cases'].sum()
n


# In[68]:


n.plot(marker='.')
plt.ylabel('Number of Cases')


# ### Hospitalized cases month wise

# In[12]:


m=data[data['Current Status']=='Hospitalized'].groupby('Month')['Num Cases'].sum()
m


# In[70]:


m.plot.bar(figsize=(7,5),color=['k','b','y','r','g'])
plt.ylabel('Hospitalized cases')
plt.xlabel('Month')
plt.xticks(rotation=360);


# In[14]:


m.plot(figsize=(10,5),marker='.')


# In[100]:


# cases month wise confirmed (recovered)
#    means recovered ke per-month me katte cases hai karko 

re=data[data['Current Status']=='Recovered'].groupby('Month')['Num Cases'].sum()
re


# In[101]:


re.plot.bar(figsize=(7,5),color=['g','y','r','b','k'])
plt.ylabel('recovered cases')
plt.xticks(rotation=360);


# In[105]:


de=data[data['Current Status']=='Deceased'].groupby('Month')['Num Cases'].sum()
de


# In[110]:


de.plot.bar()
re.plot.bar(figsize=(7,5),color=['r','y','r','g','k'])
plt.ylabel('Deceased cases')
plt.xticks(rotation=360);


# ### total male and female infected

# In[16]:


data[data['Gender']=='F']


# ### Total female infected and no of cases
# 

# In[17]:


female=data[data['Gender']=='F'].groupby('Current Status')['Num Cases'].sum()
female


# ### Total male infected and no of cases
# 

# In[18]:


male=data[data['Gender']=='M'].groupby('Current Status')['Num Cases'].sum()
male


# In[19]:


plt.figure(figsize=(8,5))
plt.plot(female,linewidth=4,label='F')
plt.plot(male,linewidth=4,label='M')

plt.grid(True,color='k')

plt.title('Gender Wise Cases')
plt.xlabel('Current Status')
plt.ylabel('Number of Cases')
plt.legend()

plt.tight_layout()

fig,axes=plt.subplots(nrows=1,ncols=2,figsize=(10,5))

axes[0].plot(female,'r',marker='.')
axes[1].plot(male,marker='.')

plt.xlabel('Current Status')
plt.ylabel('num cases')

plt.tight_layout()
# In[20]:


# total male and female infected
fm=data.groupby('Gender')['Num Cases'].sum()
fm


# In[21]:


fm.plot(marker='.')


# ### pie chart of males and females cases

# In[22]:


gen=data.groupby('Gender')['Num Cases'].sum()
plt.pie(gen,labels=['Female','Male','M','NB'],autopct='%0.1f%%',shadow=True);
plt.tight_layout()


# In[113]:


# age group is infected most
n=data.groupby('Age Bracket')['Num Cases'].sum().sort_values(ascending=False).head(10)
n


# In[122]:


n.plot(color='g',marker='.',figsize=(8,5))
plt.xticks(np.arange(0,10,0.5))
plt.grid()
plt.tight_layout()
plt.xlabel('Ages')
plt.ylabel('Num Cases')
plt.title('Age wise Covid Cases')
plt.xticks(rotation=360);


# In[120]:


n.plot.bar(color='y',figsize=(8,5))
plt.xlabel('Ages')
plt.ylabel('Num Cases')
plt.xticks(rotation=360);


# In[171]:


# state wise total cases
st=data.groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False).head(10)
t=st
g=t.sort_values(ascending=True)
g   


# ### Use of barh i.e inverted form of bar chart
#     https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html

# In[175]:


g.plot.barh(figsize=(10,6),y='Detected State',color='c')
plt.xlabel('Num cases')
plt.title('State Wise Covid Cases')
plt.grid()
plt.tight_layout()
plt.xticks(rotation=360);


# #### Find the top 5 states with total no. of Hospitalized cases 

# In[27]:


# state wise total cases i.e hospitalized
data[data['Current Status']=='Hospitalized'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False).head(5)

# so Maharashtra , Tamil Nadu top hospt cases


# In[28]:


# how many cases everyday
data.head()


# ### Every Day Hospitalized Cases  (IMP) ✨

# In[29]:


# because first comes month then days
data[data['Current Status']=='Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum().head(10)


# In[30]:


# in bar graphs 
h=data[data['Current Status']=='Hospitalized'].groupby(['Month','Day'])[['Num Cases']].sum()
h.unstack(level=0).plot(subplots=True,kind='bar',figsize=(10,10))

plt.tight_layout()

plt.xlabel('Days')
plt.ylabel('Cases')


# ### Total no. of deaths state wise

# In[31]:


# no. of deaths by state wise
d=data[data['Current Status']=='Deceased'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False).head(5)
d

# so Mahra,delhi,gujra highest deaths


# ### for same code as Above pltotting

# In[186]:


# no. of deaths by state wise
death_state_wise=data[data['Current Status']=='Deceased'].groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False).head(6)

death_state_wise.plot(color='m',marker='.',figsize=(10,5))

plt.xticks(rotation=360) # here it rotates the xlabels to degree
plt.grid(True,color='k')
plt.ylabel('Deceased Cases')
plt.tight_layout()
plt.title('State wise covid Deaths')

# same as above


# ### Practice more below

# ### 1st - Ploting the curve on graph

# In[33]:


# no. of cases per month
data.groupby('Month')['Num Cases'].sum()


# In[34]:


data.groupby('Month')['Num Cases'].sum().plot(marker='.')
plt.ylabel('Covid cases')


# ### lineplots by states

# In[35]:


data.head()


# ### State wise cases

# In[36]:


data.groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False).head(2)


# In[37]:


data[data['Detected State']=='Maharashtra'].groupby('Month')['Num Cases'].sum().plot(figsize=(9,6),label='M',marker='.')
data[data['Detected State']=='Karnataka'].groupby('Month')['Num Cases'].sum().plot(label='K',marker='.')
data[data['Detected State']=='Delhi'].groupby('Month')['Num Cases'].sum().plot(label='D',marker='.')
data[data['Detected State']=='Gujarat'].groupby('Month')['Num Cases'].sum().plot(label='G',marker='.')
data[data['Detected State']=='Uttar Pradesh'].groupby('Month')['Num Cases'].sum().plot(label='UP',marker='.')
data[data['Detected State']=='Tamil Nadu'].groupby('Month')['Num Cases'].sum().plot(label='TN',marker='.')


plt.ylabel('Num Cases')
plt.legend(loc=2)


# In[38]:


data['Detected State'].unique()


# In[180]:


data.groupby('Detected State')['Num Cases'].sum().sort_values(ascending=False).head(20).plot.bar(figsize=(12,8),color=['r','g','b','y','c','m'])
                              ### ******** imp ***********                                       # changing bar colors.
plt.ylabel('Num Cases')
plt.tight_layout()

plt.xticks(rotation=40);


# In[ ]:





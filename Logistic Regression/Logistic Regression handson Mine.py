#!/usr/bin/env python
# coding: utf-8

# # **1. Introduction to Logistic Regression** <a class="anchor" id="1"></a>
# 
# 
# When data scientists may come across a new classification problem, the first algorithm that may come across their mind is **Logistic Regression**. It is a supervised learning classification algorithm which is used to predict observations to a discrete set of classes. Practically, it is used to classify observations into different categories. Hence, its output is discrete in nature. **Logistic Regression** is also called **Logit Regression**. It is one of the most simple, straightforward and versatile classification algorithms which is used to solve classification problems.

# `Logistic Regression works on Binary Classification data. Uses Sigmoid Function and only gets the values between 0 and 1 in 
# the form of probabilities and rest of tasks is performed like linear regression`

# **Logsitic Regression helsps to find out the relationship between 2 variables (categrorical) , then bases on this relationship it helps us to predict the outcome of either one of the variable based on the other.**
# 
# `For example`: **Lets say we want to guess the whether the customer will click the buy button on a shopping website or Not. Then logistic regression by using various factors like past behaviors of Cx, buying season, time spent, price factor etc.. like these we can predict wther the buys or not.**

# ### Sigmoid Function
# 
# ![Sigmoid Function](https://miro.medium.com/max/970/1*Xu7B5y9gp0iL5ooBj7LtWw.png)

# `Logistic regression vs. linear regression`
# >Linear regression predicts a continuous dependent variable by using a given set of independent variables. A continuous variable can have a range of values, such as price or age. So linear regression can predict actual values of the dependent variable. It can answer questions like "What will the price of rice be after 10 years?"
# 
# **Unlike linear regression, logistic regression is a classification algorithm. It cannot predict actual values for continuous data. It can answer questions like "Will the price of rice increase by 50% in 10 years?"**

# linear regression $ y=mx+c $
# 
# Logistic Regression 
# $$y = \frac{1}{1 + e^{-x}}$$
# 

# <a class="anchor" id="0"></a>
# # **Logistic Regression Classifier**
# 
# 
# Hello friends,
# 
# 
# In this kernel, I implement Logistic Regression with Python and Scikit-Learn. I build a Logistic Regression classifier to predict whether or not Customer will buy the Loan scheme. I train a binary classification model using Logistic Regression. 

# ## Problem Statement:
# 
# **The above data consist of the past data of customers that has been given by bank.
# Now the bank official wants to launch a plan or scheme for the customers, now being our client the officials wants us to create a model that will predict if the upcomming customers will be interested in the schemes or not**
# 
# `Here Target column is df[y] i.e. customers who have taken the loan scheme`
# * yes - interested in scheme, 
# * No - not interested in shcemme

# ### Import libraries

# In[46]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", color_codes=True, font_scale=1)
# sns.set_style('white')
sns.set_palette('deep')


# ### Import dataset

# In[47]:


df=pd.read_csv('bank-additional-full_final (1).csv',sep=";")
df.head(2)


# ### Exploratory data analysis

# In[48]:


df.info()


# ### Removing null rows

# In[49]:


df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()


# ### Removing duplicate rows

# In[50]:


df.duplicated().sum()


# In[51]:


df.drop_duplicates(inplace=True)
df.duplicated().sum()


# ### Checking for outliers in each columns

# In[52]:


numeric_cols=df.select_dtypes(include='number').columns
num_cols=len(numeric_cols)
ncols=3
nrows=(num_cols+ncols-1)//ncols

fig,axes=plt.subplots(nrows=nrows,ncols=ncols,figsize=(ncols*4,nrows*4))
axes=axes.flatten()

for ax,col in zip(axes,numeric_cols):
    sns.boxplot(y=df[col],ax=ax)
    ax.set_title(col)

for i in range(len(numeric_cols), len(axes)):
    fig.delaxes(axes[i])
    
plt.tight_layout()
plt.show()


# **Whenever there is no box for any of the boxplot we should Never consider that for outliers because there might be less values in that column.
# `for example ` here in pdays we can see that 999.0 value has 39662 times occurance**

# In[53]:


df['pdays'].value_counts()


# In[54]:


df.columns


# #### Removing outliers

# In[55]:


outlier_cols=['age','duration','campaign','cons.conf.idx']

for col in outlier_cols:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    
    iqr=q3-q1
    lower_limit=q1-(iqr*1.5)
    upper_limit=q3+(iqr*1.5)
    
    df=df[(df[col]>=lower_limit) & (df[col]<=upper_limit)]
df


# #### Rechecking now outliers

# In[56]:


numeric_cols=df.select_dtypes(include='number').columns
num_cols=len(numeric_cols)
ncols=3
nrows=(num_cols+ncols-1)//ncols

fig,axes=plt.subplots(nrows=nrows,ncols=ncols,figsize=(ncols*4,nrows*4))
axes=axes.flatten()

for ax,col in zip(axes,numeric_cols):
    sns.boxplot(y=df[col],ax=ax)
    ax.set_title(col)

for i in range(len(numeric_cols), len(axes)):
    fig.delaxes(axes[i])
    
plt.tight_layout()
plt.show()


# now we can see that in columns `['age','duration','campaign','cons.conf.idx']` most of the outliers have been excluded

# #### Label Encoding

# In[57]:


from sklearn.preprocessing import LabelEncoder



# In[58]:


df.head(2)


# In[59]:


le=LabelEncoder()
for col in df.columns:
    if df[col].dtype=='object':
        df[col]=le.fit_transform(df[col].astype(str))
df.head(2)


# ### **Feature Selection **

# In[60]:


df.corr()


# In[61]:


plt.rc('font', size=10)  
plt.rc('axes', titlesize=10)  
plt.rc('axes', labelsize=10)  
plt.rc('xtick', labelsize=8)  
plt.rc('ytick', labelsize=8)

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(),cmap='Greens',annot=True,linewidths=0.5, linecolor='black',fmt=".2f", square=True, cbar_kws={"shrink": .8})
plt.tight_layout()


# **`Always 0.8 to 1 is Generally considered as the highest correlation in any analysis`**
# >**`And < 0.5 is Low Correlation`**
# 
# So from the above heatmap there are No high or low correlation so we are going to use above method for feature selection

# From above we can see that the right-buttom side we have lot of dark squares which is more correlation between columns
# for example: corr between euribor3m and emp.var.rate, nr.employed and euribor3m , etc. but No strong corr between columns and target column y , so now we are using VIF to reduce this multicorreiliality.
# 
# > Basically we are removing features which are not important and keeping which are important

#  <div class = "alert alert-block alert-info">
#     <b> VIF - <code>Variance Inflation Factor</code> is being used to check how much multicollinearity is there in independent columns</b>
# 
# <b> Multicollinearity  -interdependencies between the Independent columns </b>
# 
#    <div class = "alert alert-block alert-success">
#  <b>The VIF directly measures the ratio of the variance of the entire model to the variance of a model with only the feature in question </b>

# >**`Colinearity is the state where two variables are highly correlated and contain similiar information about the variance within a given dataset.`**
# 
# (variables can be columns)
# >**`Multicolinearity is the state where two or More variables are highly correlated. On the other hand it is more troublesome to detect because it emerges when three or more variables`**

# **https://towardsdatascience.com/targeting-multicollinearity-with-python-3bd3b4088d0b**
# 
# **https://etav.github.io/python/vif_factor_python.html**

# In[62]:


from statsmodels.stats.outliers_influence import variance_inflation_factor


# In[63]:


X=df.drop('y',axis=1)
y=df['y']


# In[64]:


X.head(1)


# In[65]:


variance_inflation_factor(df.values,0)


# In[66]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# <div class="alert alert-block alert-info">
#     <b>
#         Since the <code>nr.employed</code> column has the highest multicollinearity, we should remove this column first. 
#         It's important to remove columns with high multicollinearity in a 
#         <div class="alert alert-block alert-warning">
#             <b>one-by-one manner</b>
#         </div> 
#         instead of all at once. Removing columns individually helps reduce multicollinearity among other columns, as removing one highly collinear column can affect the relationships between remaining columns.(becuase if we remove any highest column there might be chance that we might reduce Multicolinearity among other columns.)
#     </b>
# </div>
# 

# 
# >* **VIF ***`< 5:`***   `Acceptable level`of multicollinearity.**
# >* **VIF between ***`5 and 10`***:   `Moderate multicollinearity`. This could still be acceptable, but further investigation is recommended**
# >* **VIF ***`> 10`:   `High multicollinearity`***. In most cases, a VIF above 10 suggests that the variable is highly collinear with others and may need to be removed to improve model stability.**

# In[67]:


X.drop('nr.employed',axis=1,inplace=True)


# In[68]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# `So now by just removing 'nr.employed' column we can see that we have signigicantly reduced the Multicolinearity amoung the columns`

# In[69]:


X.drop('cons.price.idx',axis=1,inplace=True)


# In[70]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# In[71]:


X.drop('pdays',axis=1,inplace=True)


# In[72]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# In[73]:


X.drop('euribor3m',axis=1,inplace=True)


# In[74]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# In[75]:


X.drop('cons.conf.idx',axis=1,inplace=True)


# In[76]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# In[77]:


X.drop('age',axis=1,inplace=True)


# In[78]:


vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


# In[79]:


X.drop('poutcome',axis=1,inplace=True)

vif_data=pd.DataFrame()
vif_data['feature']=X.columns
vif_data['Multicolinearity']=[variance_inflation_factor(X.values,i) for i in range(len(X.columns))]
vif_data=vif_data.sort_values(by='Multicolinearity',ascending=False)

vif_data.style.background_gradient(subset=['Multicolinearity'], cmap='Greens')


#     Now since all the columns have Multicolinearity <= 5 we can proceed further. Hence feature selection task is DOne

# In[80]:


X.head(2)


# ### Model Building

# 1. splitting data into training and testing
# 2. defining a model
# 3. training a model
# 4. testing a model
# 5. Evaluation of performance of model

# In[81]:


from sklearn.model_selection import train_test_split

Xtrain,Xtest,ytrain,ytest=train_test_split(X,y,test_size=0.30,random_state=45)


# In[82]:


Xtrain


# In[83]:


ytrain


# In[84]:


ytest


# In[85]:


from sklearn.linear_model import LogisticRegression
model=LogisticRegression()


# In[86]:


model.fit(Xtrain,ytrain)


# In[87]:


predict=model.predict(Xtest)
predict


# In[88]:


ytest


# In[89]:


y_prob = model.predict_proba(Xtest)[:, 1]

sns.regplot(x=y_prob, y=ytest, logistic=True, ci=None, line_kws={"color": "red"})
plt.xlabel("Actual (y_test)")
plt.ylabel("Predicted Probability")
plt.title("Logistic Regression Curve with Seaborn")
plt.show()


# In[90]:


from sklearn.metrics import *

accuracy_score(ytest,predict)*100


# ### Confusion Matrix
# ![image.png](attachment:image.png)

# <div class="alert alert-block alert-success">
#     <b>
#       * <code> True Positive:</code> The number of times our actual positive values are equal to the predicted positive. You predicted a positive value, and it is correct.
#     <br>
#     * <code>False Positive:</code> The number of times our model wrongly predicts negative values as positives. You predicted a negative value, and it is actually positive.
#         <br>
#     * <code>True Negative</code>: The number of times our actual negative values are equal to predicted negative values. You predicted a negative value, and it is actually negative.
#             <br>
#     * <code>False Negative:</code> The number of times our model wrongly predicts negative values as positives. You predicted a negative value, and it is actually positive. 
#         </b>
#  </div>

# ![image.png](attachment:image.png)

# In[92]:


cm=confusion_matrix(ytest,predict)


# In[93]:


cm


# In[107]:


sns.heatmap(cm,annot=True,cmap="Reds",fmt='d',linewidths=0.5,linecolor='black')


# In[135]:


print('Confusion matrix\n\n' , cm)

print('\nTrue Positives(TP) (The count of clients correctly predicted who are not interested in the scheme)  = ', cm[0,0])

print('\nTrue Negatives(TN)  (The count of clients correctly predicted who are interested in the scheme) = ', cm[1,1])

print('\nFalse Positives(FP)  (The count of clients wrongly predicted who are not interested in the scheme) = ', cm[0,1])

print('\nFalse Negatives(FN)  (The count of clients wrongly predicted who are interested in the scheme) = ', cm[1,0])


# The confusion matrix shows `9505  + 188 = 9693 correct predictions` and `233 + 624 = 857 incorrect predictions`.

# #### Accuracy

# In[118]:


Accuracy =(cm[0,0]+cm[1,1])/sum(np.array(cm).flatten())
Accuracy*100


# In[ ]:





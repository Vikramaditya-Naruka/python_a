#!/usr/bin/env python
# coding: utf-8
1.)  difference between list and numpy.

2.)  difference series and dataframe.

3.)  difference between pivot and crosstab.

4.)  difference between zeros ,ones,eye,diagonal.

5.)  difference between linspace and unique method.

6.)  difference between random integer and rand and randn function.

7.)  difference between loc and iloc.

8.)  difference implace = true and reset index.

9.)  what does groupby method provide an example.

10.) what does value_count and count_plot.

11.) in which senario you perform boxplot. 


based on data(add) performance

12.) you have to analyze click through rate based on time spend by the users on the website.

13.) you have to analyze click through rate based on daily internet uses of the users.

14.) you have to analyze click through based on the age of the users.

15.) analyze click through rate based on income of the users.

based on data supply chain


1.you have to analyze between the price of the product and the revenue generated by them

2.relation between sales and type

3.you have to look at the total revenue generated from shipping carriers

4.you have to look at the stock levels of each stock keeping unit

5.you have to look at the average defect rate of our product type

6.you have to look at by mode of tranportation

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df  = pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\click.csv")

'''
12.) you have to analyze click through rate based on time spend by the users on the website.

13.) you have to analyze click through rate based on daily internet uses of the users.

14.) you have to analyze click through based on the age of the users.

15.) analyze click through rate based on income of the users.

'''
df


# In[3]:


df.shape


# In[ ]:





# In[4]:


#you have to analyze click through rate based on time spend based on users on the website


# In[5]:


df['Clicked on Ad'].value_counts().plot(kind = 'pie',autopct = '%.2f')


# In[6]:


#you have to analyze click through rate based on daily internet uses of the users.


# In[ ]:





# In[7]:


df["clickonadd(1)"] = df['Clicked on Ad'].where(df['Clicked on Ad'] == 1, other = None)


# In[8]:


df['clickonadd(1)'].isnull().sum()


# In[9]:


df = df.dropna()


# In[10]:


df.shape


# In[11]:


sns.distplot(df['Daily Internet Usage'],hist = False)


# In[12]:


# you have to analyze click through based on the age of the users


# In[13]:


df['Gender'].value_counts().plot(kind = 'pie',autopct = '%.2f')


# In[14]:


#analyze click through rate based on income of the users. Area Income


# In[15]:


sns.distplot(df['Area Income'],hist = False)


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[17]:


'''
Based on suppy chain
1.you have to analyze between the price of the product and the revenue generated by them
2.relation between sales and type
3.you have to look at the total revenue generated from shipping carriers
4.you have to look at the stock levels of each stock keeping unit
5.you have to look at the average defect rate of our product type
6.you have to look at by mode of tranportation
'''


# In[18]:


df = pd.read_csv("C:\\Users\\welcome\\Downloads\\DataFrame\\supply_chain.csv")


# In[19]:


df.head(16)


# In[20]:


df.columns


# In[21]:


#.you have to look at by mode of tranportation


# In[22]:


df['Transportation modes'].value_counts().plot(kind = 'pie',autopct = '%.2f')


# In[23]:


#.you have to look at the average defect rate of our product type


# In[24]:


df["skin care"] = df['Product type'].where(df['Product type'] == 'skincare', other = None)


# In[25]:


df["skin care"].isnull().sum()


# In[26]:


df["hair care"] = df['Product type'].where(df['Product type'] == 'haircare', other = None)


# In[27]:


df["hair care"].isnull().sum()


# In[28]:


df.shape


# In[29]:


df["cosmetics"] = df['Product type'].where(df['Product type'] == 'cosmetics', other = None)


# In[30]:


df["cosmetics"].isnull().sum()


# In[31]:


df = df.drop(columns = ["Product type"])


# In[32]:


df


# In[33]:


sns.barplot(x = df['skin care'],y = df['Defect rates'])


# In[34]:


sns.barplot(x = df['cosmetics'],y = df['Defect rates']) 


# In[35]:


sns.barplot(x = df['hair care'],y = df['Defect rates']) 


# In[36]:


#.you have to look at the total revenue generated from shipping carriers


# In[37]:


df.head()


# In[38]:


df.columns


# In[39]:


df["Shipping costs"].sum()


# In[40]:


sns.distplot(df['Shipping costs'],hist = False)


# In[41]:


#2.relation between sales and type


# In[ ]:





# In[42]:


'''
[1:27 pm, 25/08/2023] Vaishali Sharma (IT): .list => list is a datatype and it is used to store multiple datatype 
numpy is a built-in library.
numpy is less time consuming and high computional powerful.

2. Series                                               dataframe

   1-dimensional                                        multi-dimensional
   homogeneous-it store same type of datatype           heterogenous- it store differnet type of datatype
   immutable-it cannot be changeable if once created    mutable-it can be changeable
    
3.pivot- pivot is used to reshape the row and columns only of the dataframe
  crosstab - crosstab have the same functionlity as pivot but it can work on input data or as well as dataframe
             crosstab is a relation between two categorical values
    
4.zeros => zeros() is used to store only zeros value within the given number of times
           ex- np.zeros(10)
  ones => ones() is used to store only ones value within the given number of times
           ex- np.ones(10)
  diag => diag() is used for diagonal values
  eye =>  eye() is used to change diagonal values
    
5.linspace => this method is used to store range of given values and the difference between two consecutive values is same
unique method => this method is used to store unique values and through it we can calculate number of counts as well as number of index of value
syntax=> np.unique(a, return_index=True, return_count=False)

6.random.randint => this random module function is used to store integer random number
syntax= np.random.randint(min_number, max_number, total_number)

random.rand => this random module function is used to store random values in the range 0 to 1
random.randn => this random module function is used to store random values in the range -7 to 7

8.When you use inplace=True, the changes are directly to the object without returning a new object
The "reset index" operation allows to reorganize the index labels to a default integer-based sequence or to some other specified values.

9.groupby is used to group dataframe by one or more columns so that we can apply various functions on it

11.boxplot is used for detection of outliers
'''


# In[43]:


#.list => list is a datatype and it is used to store multiple datatype 
#  numpy is a built-in library.
#   numpy is less time consuming and high computional powerful.

a = [1,2,4,56]
type(a)


# In[46]:


b = np.array(a)
b


# In[47]:


'''
 Series                                               dataframe

   1-dimensional                                        multi-dimensional
   homogeneous-it store same type of datatype           heterogenous- it store differnet type of datatype
   immutable-it cannot be changeable if once created    mutable-it can be changeable
'''


# In[48]:


'''
pivot- pivot is used to reshape the row and columns only of the dataframe
  crosstab - crosstab have the same functionlity as pivot but it can work on input data or as well as dataframe
             crosstab is a relation between two categorical values
    
'''


# In[56]:


'''
.zeros => zeros() is used to store only zeros value within the given number of times
           ex- np.zeros(10)
  ones => ones() is used to store only ones value within the given number of times
           ex- np.ones(10)
  diag => diag() is used for diagonal values
  eye =>  eye() is used to change diagonal values
    
'''

print(np.zeros(5))

print(np.ones(5))

print(np.eye(4,5))
print(np.diag([2,4,6,7,8]))


# In[58]:


'''
linspace => this method is used to store range of given values and the difference between two consecutive values is same
unique method => this method is used to store unique values and through it we can calculate number of counts as well as number of index of value
syntax=> np.unique(a, return_index=True, return_count=False)
'''

print(np.linspace(1,4,5))

a = np.array([10,23,4,5,1,2,3,123,1,2,3,1,2,3,5,5,6,6,78,])
np.unique(a , return_index = True , return_counts = True)


# In[62]:


'''
random.randint => this random module function is used to store integer random number
syntax= np.random.randint(min_number, max_number, total_number)


random.rand => this random module function is used to store random values in the range 0 to 1
random.randn => this random module function is used to store random values in the range -7 to 7
'''

print(np.random.randint(1,10,4))
print(np.random.rand(5))
print(np.random.randn(6))


# In[63]:


'''
8.When you use inplace=True, the changes are directly to the object without returning a new object
The "reset index" operation allows to reorganize the index labels to a default integer-based sequence or to some other specified values.

'''


# In[ ]:


'''
groupby is used to group dataframe by one or more columns so that we can apply various functions on it

'''
grouped = df.groupby('Product type')
sum_p = grouped['Defect rates'].sum()
average=sum_p/26
print(average)


# In[66]:


#11.boxplot is used for detection of outliers

sns.barplot(x=df['Shipping carriers'], y=df['Revenue generated'])


# In[68]:


'''
.The loc() function is label based data selecting method which means that we have to pass the name of the row or column which we want to select.
The iloc() function is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column.
'''
df.loc[1:10 , 'SKU']               # [raw_range , column_name]

df.iloc[1:10 , 1:3] # [raw_range , column_range_index]


# In[2]:


a = [1,24,5,6]
type(a)


# In[7]:


b = np.array(a)
b


# In[13]:


#Series
a = pd.Series(['1','2','2','6','8','9'],index = ['a','b','c','d','e','f'])
print(a['b'])


# In[15]:


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 28],
    'Gender': ['Female', 'Male', 'Male']
}

df = pd.DataFrame(data)
df


# In[18]:


#pivot
data = {
    'Date': ['2023-08-01', '2023-08-01', '2023-08-02', '2023-08-02'],
    'Product': ['A', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 120]
}

df = pd.DataFrame(data)
pivot_table = df.pivot(index = 'Date',columns = 'Product',values = 'Sales')
pivot_table


# In[19]:


#crosstab
data = {
    'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
    'AgeGroup': ['18-25', '26-35', '18-25', '26-35', '18-25']
}
df = pd.DataFrame(data)
cross_tab = pd.crosstab(df['Gender'],df['AgeGroup'])
cross_tab


# In[23]:


#unique
a = np.array([1,2,44,5,66,7,1,2,3,44,5])
print(np.unique(a))


# In[26]:


#linespace
a = np.linspace(1,7,7)
a


# In[34]:


data = {
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles'],
    'Product': ['A', 'B', 'A', 'A', 'B'],
    'Sales': [100, 150, 200, 120, 80]
}

df = pd.DataFrame(data)
grouped = df.groupby('City')['Sales'].sum()
grouped


# In[ ]:





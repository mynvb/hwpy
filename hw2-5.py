#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[16]:


#1
n = 10
x = np.arange( -(n-1), 1 )
for i in range(len(x)):
    x[i] = x[i]*(-1)
x


# In[26]:


#2

def mtrx_from_n_to_0(n):
    mtrx = np.arange( -(n-1), 1 )
    for i in range(len(mtrx)):
        mtrx[i] = mtrx[i]*(-1)
    return np.diag(mtrx)

def count_values(inp): 
    return np.trace(inp)
    
count_values(mtrx_from_n_to_0(n = 7))


# In[54]:


#3
mov = pd.read_csv('ratings.csv').filter(items = ['movieId', 'rating']) #['movieId'].value_counts()
filtered = mov[ (mov['rating']==5) ]['movieId'].value_counts().idxmax()
print(filtered)


# In[74]:


#4
year1, year2 = 2005, 2010
power = pd.read_csv('power.csv')
filt1 = power[ (power['country']=='Latvia') | (power['country']=='Estonia') | (power['country']=='Lithuania')]
summ = filt1[ (filt1['year'] > year1) & (filt1['year'] < year2) ]['quantity'].sum()
print(summ)


# In[77]:


''' #5
4x + 2y + z = 4
x + 3y = 12
5y + 4z = -3
'''
from numpy import linalg
a = np.array([
    [4, 2, 1], 
    [1, 3, 0],
    [0, 5, 4]])

b = np.array([4, 12, -3])

print(linalg.solve(a,b))
np.allclose(np.dot(a, linalg.solve(a, b)), b)


# In[ ]:





# In[ ]:





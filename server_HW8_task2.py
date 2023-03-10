#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy import stats


# In[2]:


#Задача2. Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95

x=[131, 125, 115, 122, 131, 115, 107, 99, 125, 111]
np.array(x)


# In[7]:


#найдем среднее по выборке
x_mean=np.mean(x)
x_mean


# In[5]:


#найдем дисперсию
d_x=np.var(x, ddof=1)
d_x


# In[6]:


#найдем критерий стьюдента для доверительного интервала 95%, кол-во степеней  сравнения 10-1=9
t=stats.t.ppf(0.975,len(x)-1)
t


# In[8]:


#найдем верхнюю границу интервала
t1=x_mean+t*d_x/np.sqrt(10)
t1


# In[9]:


#найдем нижнюю границу интервала
t2=x_mean-t*d_x/np.sqrt(10)
t2


# In[ ]:





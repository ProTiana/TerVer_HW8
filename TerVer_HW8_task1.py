#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
from scipy import stats

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
zp, ks


# In[10]:


#найдем средние значения по выборкам
zp_mean=np.mean(zp)
ks_mean=np.mean(ks)
zp_ks_mean=np.mean(zp*ks)
zp_mean, ks_mean, zp_ks_mean


# In[13]:


#найдем ковариацию по формуле cov=m(xy)-m(x)*m(y)
cov1=zp_ks_mean-zp_mean*ks_mean
cov1


# In[22]:


#найдем ковариацию функцией
cov2=np.cov(zp, ks, ddof=1)
cov2


# In[26]:


#найдем коэф-т пирсона r(xy)=cov(xy)/str(x)*str(y)
zp_std=np.std(zp, ddof=0)
ks_std=np.std(ks, ddof=0)
r=cov1/(zp_std*ks_std)
zp_std, ks_std, r


# In[27]:


#найдем коэф-т пирсона функцией
np.corrcoef(zp, ks)


# In[ ]:





# In[ ]:





# In[ ]:





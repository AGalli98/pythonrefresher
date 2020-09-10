#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[8]:


x = np.arange(0,2*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)


# In[12]:


f,ax = plt.subplots()
ax.plot(x,y_sin)
ax.plot(x,y_cos)


# In[ ]:





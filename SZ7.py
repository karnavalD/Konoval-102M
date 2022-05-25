#!/usr/bin/env python
# coding: utf-8

# In[43]:


a = {'1', '2', '4', '7', '9', '3'}
len(a)


# In[48]:


a = {'1', '2', '4', '5'}
a.intersection_update({'1','2','5'})
print(a)


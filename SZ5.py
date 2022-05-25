#!/usr/bin/env python
# coding: utf-8

# In[23]:


row = "4321"

print(row[::2])


# In[27]:


a = [11, 22, 3, 46, 5, 6, 87, 8, 9, 8, 73, 6, 45, 4, 3, 2, 111]
b = 1
while b != len(a):
    if a[b] > a[b - 1]:
        print(a[b], end=' ')
    b += 1


# In[30]:


s=[3, 41, 55, 240, 12]

max_var=s.index(max(s))
min_var=s.index(min(s))

s[max_var],s[min_var]=s[min_var],s[max_var]

print (s)


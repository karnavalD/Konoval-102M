#!/usr/bin/env python
# coding: utf-8

# In[57]:


from pandas import *
from math import factorial

def goroda(n, r):
    return factorial(n)/ (factorial(n-r))
goroda(5,3)


# In[60]:


c = 16 #кол-во подбрасываний

right = 14 #кол-во угаданных вариантов

def factorial (n):
    if n == 1: return 1
    else: return n * factorial (n-1)
    
answer = factorial(c)/(factorial(right)*factorial(c-right))/c**right

print (f'{answer} % - вероятность данного события') #вероятность данного события


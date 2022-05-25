#!/usr/bin/env python
# coding: utf-8

# In[25]:


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
s = 0
for number in numbers:
    s += number
print(s)


# In[4]:


def mem(a):
    s=0
    for i in a:
        if i==0:
            s=s+1
    return s
a=[2,1,4,0,8,1,3]
print(mem(a))


# In[7]:


n = int(input()) + 1
for i in range(1, n + n + 2):
    if i <= n:
        print(' ' * (n - i), end='')
        print(*range(1, i), *range(1, i - 1)[::-1], sep='')
    else:
        print(' ' * (i - n), end='')
        print(*range(1, n + n - i), *range(1, n + n - i - 1)[::-1], sep='')


# In[9]:


num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)


# In[27]:


n = int(input())
a = ""
for i in range(n):
    a = a + str(i+1)
    print(a)


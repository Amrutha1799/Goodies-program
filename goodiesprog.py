#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
a=sorted(a)
n=int(input("Number of the employees:"))
mini=a[0+n-1]-a[0]
index=0
for i in range(1,len(a)-n):
    if(mini>a[i+n-1]-a[i]):
        mini=a[i+n-1]-a[i]
        index=i
print(a[index:index+n])
print(mini)


# In[ ]:





# In[ ]:





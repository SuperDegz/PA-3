#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[10]:


cars = pd.read_csv('cars.csv')
cars


# In[18]:


# Load the cars dataset
cars = pd.read_csv('cars.csv')

# Display the first five rows with odd-numbered columns 
print(cars.iloc[:5, ::2])

# Display the row that contains the 'Model' of 'Mazda RX4'.
print(cars[cars['Model'] == 'Mazda RX4'])

# Print the number of cylinders for the 'Camaro Z28' model
print(cars[cars['Model'] == 'Camaro Z28']['cyl'].values[0])

# Display the 'cyl' and 'gear' columns for specific models
print(cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])][['cyl', 'gear']])


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[61]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

insurance_file = pd.read_csv('insurance.csv')

#Columns Variables
insurance_age = insurance_file['age']
insurance_sex = insurance_file['sex']
insurance_bmi = insurance_file['bmi']
insurance_children = insurance_file['children']
insurance_smoker = insurance_file['smoker']
insurance_region = insurance_file['region']
insurance_charges = insurance_file['charges']

#Unique Regions
regions = insurance_file.region.unique()

print(insurance_file.head(20))


# In[75]:


#Relation between sex and bmi
mean_female_bmi = np.mean(insurance_file[insurance_file.sex == 'female'].bmi)
mean_male_bmi = np.mean(insurance_file[insurance_file.sex == 'male'].bmi)

print(mean_female_bmi)
print(mean_male_bmi)

#Relation between age and bmi
plt.hist(insurance_age , color="blue", label="AGE", alpha=0.5)
plt.hist(insurance_bmi , color="red", label="BMI", alpha=0.5)
plt.legend()
plt.show()
plt.close()


# In[28]:


#
southwest_count = insurance_region[insurance_region == 'southwest'].count()
southeast_count = insurance_region[insurance_region == 'southeast'].count()
northwest_count = insurance_region[insurance_region == 'northwest'].count()
northeast_count = insurance_region[insurance_region == 'northeast'].count()
total = insurance_region.count()

pie_values = [southwest_count, southeast_count, northwest_count, northeast_count]
pie_labels = ['southwest', 'southeast', 'northwest', 'northeast']
plt.pie(pie_values, labels=pie_labels, labeldistance = 0.45)
plt.show()
plt.close()


# In[87]:


mean_charges_per_region = insurance_file.groupby('region').charges.mean().reset_index()
total_charges_per_region = insurance_file.groupby('region').charges.sum().reset_index()

total_insurances_per_region = insurance_file.groupby('region').charges.count().reset_index()

#Relation between region and insurance charge
ax = mean_charges_per_region.plot.bar(x='region', y='charges', rot=0)


# In[118]:


counts_per_sex = insurance_file.groupby('sex').children.sum().reset_index()
counts_per_sex['mean_bmi'] = [insurance_file.bmi[insurance_file.sex == 'female'].mean(), insurance_file.bmi[insurance_file.sex == 'male'].mean()]
counts_per_sex['quantity'] = [len(insurance_file[insurance_file.sex == 'female']), len(insurance_file[insurance_file.sex == 'male'])]
counts_per_sex['smokers'] = [len(insurance_file[(insurance_file.sex == 'female') & (insurance_file.smoker == 'yes')]), len(insurance_file[(insurance_file.sex == 'male') & (insurance_file.smoker == 'yes')])]

ax = counts_per_sex.plot.bar(x='sex', y=['children', 'quantity', 'smokers'], rot=0)

print(counts_per_sex)


# In[ ]:





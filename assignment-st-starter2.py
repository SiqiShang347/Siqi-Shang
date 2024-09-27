#!/usr/bin/env python
# coding: utf-8

# In[24]:


# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
# show the title
st.title('Titanic App by Xiaoxi Wang')
# read csv and show the dataframe
data = pd.read_csv('train.csv')
st.write(data) 


# In[25]:


# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
sns.set_theme(style="whitegrid")

sub_data_1 = data[data['Pclass'] == 1]['Fare']
sub_data_2 = data[data['Pclass'] == 2]['Fare']
sub_data_3 = data[data['Pclass'] == 3]['Fare']

ax[0].boxplot(sub_data_1)
ax[0].set_title('PClass = 1',verticalalignment='bottom')
ax[0].set_xlabel('Fare')
ax[0].set_ylabel('Fare')

ax[1].boxplot(sub_data_2)
ax[1].set_title('PClass = 2',verticalalignment='bottom')
ax[1].set_xlabel('Fare')

ax[2].boxplot(sub_data_3)
ax[2].set_title('PClass = 3',verticalalignment='bottom')
ax[2].set_xlabel('Fare')
matplotlib.use('Agg')
st.pyplot(fig)














#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


pokemon=pd.read_excel("C:\\Users\Shiva Prasad.M\Downloads\pokemon.xlsx")


# In[8]:


print(pokemon.shape)
pokemon.head()


# In[10]:


sb.countplot(data = pokemon, x = 'generation_id');


# In[12]:


base_color = sb.color_palette()[0]
sb.countplot(data = pokemon, x = 'generation_id', color = base_color)


# In[14]:


base_color = sb.color_palette()[1]
gen_order = pokemon['generation_id'].value_counts().index
sb.countplot(data = pokemon, x = 'generation_id', color = base_color, 
              order = gen_order)


# In[27]:


base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, x = 'type_1', color = base_color)


# In[28]:


base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, x = 'type_1', color = base_color)
plt.xticks(rotation=90);


# In[29]:


base_color = sb.color_palette()[2]
sb.countplot(data = pokemon, y = 'type_1', color = base_color)


# In[30]:


pokemon.isna().sum()


# In[31]:


na_counts = pokemon.isna().sum()
base_color = sb.color_palette()[0]
sb.barplot(na_counts.index.values, na_counts, color = base_color)
plt.xticks(rotation=90);


# In[33]:


sorted_counts = pokemon['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False);
plt.axis('square');


# In[34]:


sorted_counts = pokemon['generation_id'].value_counts()
plt.pie(sorted_counts, labels = sorted_counts.index, startangle = 90,
        counterclock = False, wedgeprops = {'width' : 0.4});
plt.axis('square');


# In[35]:


plt.hist(data = pokemon, x = 'speed')


# In[36]:


plt.hist(data = pokemon, x = 'speed', bins = 20)


# In[37]:


bins = np.arange(0, pokemon['speed'].max()+1, 5)
plt.hist(data = pokemon, x = 'speed', bins = bins)


# In[39]:


plt.figure(figsize = [20, 10]) # larger figure size for subplots

# histogram on left, example of too-large bin size
plt.subplot(1, 2, 1) # 1 row, 2 cols, subplot 1
bin_edges = np.arange(0, pokemon['speed'].max()+1, +5)
plt.hist(data = pokemon, x = 'speed', bins = bin_edges);

# histogram on right, example of too-small bin size
plt.subplot(1, 2, 2) # 1 row, 2 cols, subplot 2
bin_edges = np.arange(0, pokemon['speed'].max()++1, 1)
plt.hist(data = pokemon, x = 'speed', bins = bin_edges);


# In[40]:


sb.distplot(pokemon['speed']);


# In[41]:


bin_edges = np.arange(0, pokemon['speed'].max()+1, 5)
sb.distplot(pokemon['speed'], bins = bin_edges, kde = False,
            hist_kws = {'alpha' : 1});


# In[ ]:





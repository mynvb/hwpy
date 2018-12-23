#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[22]:


#1
geo_data = {
    'Центр': ['москва', 'тула', 'ярославль'],
    'Северо-Запад': ['петербург', 'псков', 'мурманск'],
    'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']}

data = pd.read_csv('keywords.csv')

def classify(inp):
    for region, cities in geo_data.items(): 
        for city in cities: 
            if city in inp['keyword']:
                return region
                break
            continue
    return 'undefined'
data['region'] = data.apply(classify, axis = 1)

#проверка
filtered = data[data['region'] != 'undefined']
filtered.head()


# In[30]:


#2
ratings = pd.read_csv('ml-latest-small/ratings.csv')

def rate_film(inp):
    if inp['rating'] < 2: return 'low'
    if 2 <= inp['rating'] < 4: return 'middle'
    if inp['rating'] >= 4: return 'high'
ratings['classes'] = ratings.apply(rate_film, axis = 1)
ratings.head()


# In[69]:


#3
from datetime import datetime
kinomani = pd.read_csv('ml-latest-small/ratings.csv')
#создаем список киноманов
groupped_users = kinomani.groupby('userId').count().reset_index()
filt = groupped_users[groupped_users['rating'] > 100]
user_list = filt['userId'].tolist()

#фильтруем исходную таблицу
kinomani = kinomani[kinomani['userId'].isin(user_list)]


#определяем разницу
def lifetime_users(inp):
    dif = datetime.fromtimestamp(inp['max']) - datetime.fromtimestamp(inp['min'])
    return dif.days

group = kinomani.groupby('userId').agg(['min', 'max'])['timestamp']

group['diff'] = group.apply(lifetime_users, axis =1 )
group.head()


# In[109]:


#4
years = list(range(1950, 2018, 1))
def production_year(inp):
    for year in years:
        if str(year) in inp['title']:
            return year
    return 1900
#создаем таблицу с годами выпуска фильма
movies = pd.read_csv('ml-latest-small/movies.csv')
movies['year'] = movies.apply(production_year, axis = 1)
movies_years = movies.filter(items=['movieId', 'year'])

#объединям таблицы с рейтингами и годами выпуска
ratings = pd.read_csv('ml-latest-small/ratings.csv')
joined = ratings.merge(movies_years, on = 'movieId', how='left')

#считаем средний рейтинг и сортируем
rating_years = joined.groupby('year').mean()['rating'].reset_index()
rating_years_sorted = rating_years.sort_values('rating', ascending = False)
rating_years_sorted.head()




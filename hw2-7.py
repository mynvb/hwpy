
###### 1
import psycopg2
import os
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#параметры для подсоединения с базой данных
params = {
    "host": os.environ['APP_POSTGRES_HOST'],
    "port": os.environ['APP_POSTGRES_PORT'],
    "user": 'postgres'}

conn = psycopg2.connect(**params)


psycopg2.extensions.register_type(
    psycopg2.extensions.UNICODE,
    conn)

psycopg2.extensions.register_type(
    psycopg2.extensions.UNICODE,
    conn)

conn.set_isolation_level(
    psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

#создаем курсор
cursor = conn.cursor()

#задаем параметры выдачи 
user_item_query_config = {"AVG_RATING": 3, "LIMIT": 15}

sql_str1 = ("drop table if exists movies_top;")
sql_str2 = (
			'''
			select * into movies_top from 
				(select 
					movieid, 
					count(rating) as ratings_num, 
					avg(rating) as ratings_avg 
				from ratings 
				group by movieid) as tmp1
				where ratings_avg>%(AVG_RATING)d
				limit %(LIMIT)d;

			''' % user_item_query_config)

cursor.execute(sql_str1)
cursor.execute(sql_str2)


conn.commit()


cursor.execute("SELECT * FROM movies_top LIMIT 10")
logger.info(
    "Выгружаем данные из таблицы movies_top: (movieId, ratings_num, ratings_avg)\n{}".format(
        [i for i in cursor.fetchall()]))

########### 2


from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()


class MoviesTop(Base):
    __tablename__ = 'movies_top'

    movieid = Column(Integer, primary_key=True)
    ratings_num = Column(Float)
    ratings_avg = Column(Float)

    def __repr__(self):
        return "<User(movieid='%s', ratings_num='%s', ratings_avg='%s')>" % (self.movieid, self.ratings_num, self.ratings_avg)


# Создаём сессию

engine = create_engine('postgresql://postgres:@{}:{}'.format(os.environ['APP_POSTGRES_HOST'], os.environ['APP_POSTGRES_PORT']))
Session = sessionmaker(bind=engine)
session = Session()


# делаем запрос к таблице
query = session.query(MoviesTop).filter(MoviesTop.ratings_num>15).filter(MoviesTop.ratings_avg>3.5).order_by(MoviesTop.ratings_avg.desc()).limit(15)


top_rated_query = session.query(MoviesTop)

logger.info("Выборка из top_rated_query\n{}".format([i for i in top_rated_query.limit(1)]))

#расширил массив до 15 элементов, так как на список из 5 элементов не было выдачи
top_rated_content_ids = [int(i[0]) for i in top_rated_query.values(MoviesTop.movieid)][:15]

print(top_rated_content_ids)


################ 3

from pymongo import MongoClient


mongo = MongoClient(**{
    'host': os.environ['APP_MONGO_HOST'],
    'port': int(os.environ['APP_MONGO_PORT'])
})
db = mongo.get_database(name="movie")

db = mongo["movie"]
tags_collection = db['tags']

mongo_query = tags_collection.find(
        {"id": {"$in": top_rated_content_ids}})

mongo_docs = [i for i in mongo_query]

print("Достали документы из Mongo: {}".format(mongo_docs[:5]))

id_tags = [(i['id'], i['name']) for i in mongo_docs]

############# 4

import pandas as pd

tags_df = pd.DataFrame(id_tags, columns=['movieid', 'tags'])

groupped_tags = tags_df.groupby('tags').count().reset_index()
print(groupped_tags)
groupped_tags_sorted = groupped_tags.sort_values('movieid', ascending = False)

tag_list = groupped_tags_sorted['tags'].tolist()

print(tag_list[:5])
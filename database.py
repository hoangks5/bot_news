
import pymongo
from pymongo import UpdateOne
import time

def check_id_new(data_list, collection):
    # kiểm tra id đã tồn tại trong db chưa nếu chưa
    data_new = []
    for data in data_list:
        if data['id'] not in collection.distinct('id'):
            data_new.append(data)
    return data_new


def get_news_by_category(category):
    client = pymongo.MongoClient("mongodb+srv://hoangndute:GBkjPbgppzwxOgy6@cluster0.2tmuquc.mongodb.net/")
    db = client["news"]
    collection = db["vietnamnet"]
    # lấy tin tức theo category từ db ngày hôm nay published_date dạng string 2024-06-05T10:20:00
    news = collection.find({'category': category, 'published_date': {'$regex': f'{time.strftime("%Y-%m-%d")}'}})
    return list(news)





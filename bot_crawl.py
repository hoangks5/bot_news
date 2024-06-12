
import pymongo
from pymongo import UpdateOne
from utils import *
from database import *
import time
from sum import summarize

client = pymongo.MongoClient("mongodb+srv://hoangndute:GBkjPbgppzwxOgy6@cluster0.2tmuquc.mongodb.net/")
db = client["news"]
    
def bot_vietnamnet(db):
    collection = db["vietnamnet"]
    data = crawl_vietnamnet()
    data_new = check_id_new(data, collection)
    if len(data_new) != 0:   
        for data in data_new:
            data['content'] = crawl_content_vietnamnet(data['url'])
            data['description'] = summarize(data['content'])
            collection.insert_one(data)
            print(data)
def bot_crawl_vnexpress(db):
    collection = db["vietnamnet"]
    data = crawl_vnexpress()
    data_new = check_id_new(data, collection)
    if len(data_new) != 0:
        for data in data_new:
            data['content'] = crawl_content_vnexpress(data['url'])
            data['description'] = summarize(data['content'])
            collection.insert_one(data)
            print(data)

def get_category_vietnamnet():
    collection = db["vietnamnet"]
    categories = collection.distinct("category")
    with open('categories.txt', 'w', encoding='utf-8') as f:
        for category in categories:
            f.write(category + '\n')

while True:
    bot_vietnamnet(db)
    bot_crawl_vnexpress(db)
    # đặt thời gian nghỉ để crawl dữ liệu tiếp theo
    get_category_vietnamnet()
    time.sleep(5*60)
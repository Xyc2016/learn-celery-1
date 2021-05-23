import pymongo
db_client = pymongo.MongoClient("localhost", 27017, connect=False)
learn_celery_db = db_client["learn_celery_db"]
learn_celery_collection = learn_celery_db["learn_celery_collection"]

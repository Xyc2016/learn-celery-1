from bson.objectid import ObjectId
from db import learn_celery_collection
import time


def print_and_update_doc(doc_id):
    from tasks.the_tasks import t_update_doc_by_data
    doc = learn_celery_collection.find_one({"_id": ObjectId(doc_id)})
    print(doc)
    learn_celery_collection.update_one({"_id": ObjectId(doc_id)}, {"$set": {"ar": [
        0, 1, 2
    ]}})
    for index in range(3):
        t_update_doc_by_data.s(doc_id, index).apply_async()


def update_doc_by_data(doc_id, index):
    doc = learn_celery_collection.find_one({"_id": ObjectId(doc_id)})
    data = doc["ar"][index]
    new_data = data * 1000
    print(data * 0.1)
    time.sleep(1)
    print(new_data)
    learn_celery_collection.update_one({"_id": ObjectId(doc_id)},
                                       {"$push": {"new_data": new_data+1}}
                                       )


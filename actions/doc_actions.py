import math
from typing import List
from celery import group
from random import randint, random

from celery.canvas import chord
from oss_utils.bucket import learn_oss_bucket
from bson.objectid import ObjectId
from datetime import datetime
from db import learn_celery_collection
import time


def print_and_update_doc(doc_id):
    from tasks.the_tasks import t_update_doc_by_data
    doc = learn_celery_collection.find_one({"_id": ObjectId(doc_id)})
    print(doc)
    ar = [
        randint(1, 5) for _ in range(randint(6, 20))
    ]
    now = datetime.now()

    learn_celery_collection.update_one({"_id": ObjectId(doc_id)},
                                       {"$set": {
                                           "updated": now,
                                           "ar": ar}})
    tasks = [t_update_doc_by_data.s(
        doc_id, page, ar[page * 5: (page + 1) * 5]) for page in range(math.ceil(len(ar) / 5))]

    # g = group(*tasks)
    from tasks.the_tasks import t_notify_done
    c = chord(tasks, t_notify_done.s("1"))
    c.apply_async()


def update_doc_by_data(doc_id, index, ar: List[int]):
    print(doc_id, ar)
    doc = learn_celery_collection.find_one({"_id": ObjectId(doc_id)})
    dt = doc["updated"].strftime("%Y%m%d")
    data = f"{doc['ar'][:5]}_{''.join(str(o) for o in  ar)}"
    learn_oss_bucket.put_object(f"{dt}/{doc_id}/{index}.txt", data)
    print('a')
    return 'a'


def notify_done(*args):
    print(args)
    # learn_celery_collection.update_one(
    # {"_id": doc_id}, {"$set": {"status": "done"}})

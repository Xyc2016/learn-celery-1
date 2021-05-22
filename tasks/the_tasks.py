from bson.objectid import ObjectId
from .celery_settings import celery_instance
from db import learn_celery_collection
from actions.doc_actions import print_and_update_doc, update_doc_by_data
@celery_instance.task
def t(*args, **kwargs):

    return args



@celery_instance.task
def t_print_doc(doc_id):
    print_and_update_doc(doc_id)
    return

@celery_instance.task
def t_update_doc_by_data(doc_id, index):
    update_doc_by_data(doc_id, index)
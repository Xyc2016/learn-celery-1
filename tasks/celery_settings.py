from celery import Celery

celery_instance = Celery(
    "tasks",
    backend="redis://localhost:6379",
    broker="redis://localhost:6379",
    include=["tasks.the_tasks"]
)

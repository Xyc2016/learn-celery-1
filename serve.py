from flask import Flask, json, request
from tasks.the_tasks import t, t_print_doc
from db import learn_celery_collection

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    t.s("a", k=1).apply_async()
    return "a."

@app.route("/create_doc", methods=["POST"])
def create_doc():
    d = json.loads( request.data)
    doc_id = learn_celery_collection.insert(d)
    t_print_doc.s(str(doc_id)).apply_async()
    return "done"

if __name__ == "__main__":
    app.run("0.0.0.0", 10001)

import time
import random
import celery
from celery import chord

app = celery.Celery(
    "tasks", broker="pyamqp://guest@rabbitmq//", backend="redis://redis:6379/0"
)

@app.task(name="task.build_server")
def build_server():
    print("wait 10 sec")
    time.sleep(10)
    server_id = random.randint(1, 100)
    return server_id


@app.task(name="task.build_servers")
def build_servers():
    g = chord(build_server.s() for _ in range(10))
    return g()


@app.task(name="task.callback")
def callback(result):
    for server_id in result:
        print(server_id)
    print("cleanup complete")
    return "done"


@app.task(name="task.build_server_with_cleanup")
def build_server_with_cleanup():
    c = chord((build_server.s() for _ in range(10)), callback.s())
    return c()

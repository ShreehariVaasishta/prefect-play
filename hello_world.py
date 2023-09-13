import time
from datetime import datetime

@task
def curl_cmd():
    time.sleep(10)
    x = datetime.now().time()
    return x.strftime("%H:%M:%S")


@task
def printf(x):
    print(x)


@flow
def hello():
    for _ in range(5):
        x = curl_cmd.submit()
        printf.submit(x.result())

hello()

from django.shortcuts import redirect
import time
import random

# Create your views here.


def performance_in(request, delay=None):
    if delay is None:
        delay = 10
    delay = random.random() * int(delay)
    print("sleep {0}s".format(delay))
    time.sleep(delay)
    return redirect("/")

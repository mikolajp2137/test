import math
import os
import sys

import requests


def greet(who):
    greeting = "hello, {}".format(who)
    return greeting


print(greet('jarek'))
print(sys.version)
r = requests.get('https://google.com')
print(r.status_code)
a = 1

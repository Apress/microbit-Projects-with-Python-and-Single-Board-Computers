#!/bin/python3

import urllib.request as ur
import json

url = 'https://the-trivia-\
api.com/api/questions?limit=1’

response = ur.urlopen(url).read()
print(response)

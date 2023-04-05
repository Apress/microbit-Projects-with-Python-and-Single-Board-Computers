#!/bin/python3

import urllib.request as ur
import json
from random import shuffle

url = 'https://the-trivia-\
api.com/api/questions?limit=1'

response = ur.urlopen(url).read()
# print(response)
json_response = json.loads(response)

print(json_response[0]['question'])
mylist = json_response[0]['incorrectAnswers']
mylist.append(json_response[0]['correctAnswer'])
shuffle(mylist)
print(mylist)

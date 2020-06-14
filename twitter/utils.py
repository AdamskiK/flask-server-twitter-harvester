import os
import requests


class Request(object):
    def __init__(self, url):
        self.url = url
        self.headers = {"Content-Type": "application/json"}

    def post(self, data):
        _ = requests.post(self.url, data=data, headers=self.headers)

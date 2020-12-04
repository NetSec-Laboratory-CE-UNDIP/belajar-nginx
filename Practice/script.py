import requests
import os

for i in range(10000):
	requests.get(f"http://{os.getenv('IP')}")

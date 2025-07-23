import requests
from lxml import html
import json
import csv
import subprocess
from time import sleep

names = []
lens = []
with open('length.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['Rank', 'Name', 'ID', 'Length(s)', 'Score', 'Creator', 'Version', 'Video', 'Description'])
	for i in range(1, 1001):
		target_url = f"https://api.demonlist.org/levels/classic?place={i}"
		response = requests.get(target_url)
		#print(response.content)
		data = json.loads(response.content)
		data = data['data'][0]
		n = data['name']
		l = data['length']
		id = data["level_id"]
		version = data["created_in"]
		rank = data["place"]
		s = data["score"]
		creator = data["creator"]
		video = data["video"]
		desc = data["description"]
		print(n, l)
		writer.writerow([rank, n, id, l, s, creator, version, video, desc])
		names.append(n)
		lens.append(l)
		sleep(1)

# Run a shell command
subprocess.run("start length.csv", shell=True)
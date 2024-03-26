import requests
import json

# make api call, store response
url = "http://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"status {r.status_code}")

# explore data structure
response_dict = r.json()
readable_file = "data/readable_hn_topstories.json"
with open(readable_file, "w") as f:
    json.dump(response_dict, f, indent=4)

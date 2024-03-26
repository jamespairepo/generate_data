from operator import itemgetter

import requests

# make api call, store response
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"status: {r.status_code}")

# process info about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # make separate api call for each
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id {submission_id}\tstatus {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"http://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict.get("descendants", 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f"\ntitle {submission_dict['title']}")
    print(f"discussion link {submission_dict['hn_link']}")
    print(f"comments {submission_dict['comments']}")

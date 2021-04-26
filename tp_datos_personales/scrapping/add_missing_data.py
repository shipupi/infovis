import json
from urllib.parse import urlparse
import requests

API_KEY1 = "API_KEY1" #bail@itba.edu.ar
API_KEY2 = "API_KEY2" #zetapb@gmail.com
API_KEY3 = "API_KE3" #ail.brianez@gmail.com


def get_video_details(video_url):
    o = urlparse(video_url)
    video_id = o.query.split("=")[1]
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key={}".format(video_id, API_KEY3)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Unable to get details: {}".format(response.status_code))


with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\personal_data_added.json') as json_file:
    data = json.load(json_file)

for v in data:
    if "categoryId" not in v:
        video_details = get_video_details(v["url"])
        if  video_details is None:
            continue
        if len(video_details["items"]) == 0:
            continue
        v0 = video_details["items"][0]
        snippet = v0["snippet"]
        if "tags" in snippet:
            v["tags"] = snippet["tags"]
        if "categoryId" in snippet:
            v["categoryId"] = snippet["categoryId"]
with open("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\personal_data_added.json", "w") as f:
    json.dump(data, f)
    f.close()
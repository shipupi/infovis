import requests
import json
from html.parser import HTMLParser
from urllib.parse import urlparse


API_KEY1 = "API_KEY1" #bail@itba.edu.ar
API_KEY2 = "API_KEY2" #zetapb@gmail.com
API_KEY3 = "API_KE3" #ail.brianez@gmail.com

def get_video_details(video_url):
    o = urlparse(video_url)
    video_id = o.query.split("=")[1]
    url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={}&key={}".format(video_id, API_KEY2)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Unable to get details: {}".format(response.status_code))


newVideoAttr = "mdl-typography--body-1"
videos = []

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.inside = 0
        self.current_video = {}

    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            # attr[0] es el nombre del attributo
            # attr[1] es el valor
            if newVideoAttr in attr[1] and "class" == attr[0]:
                self.inside += 1
                self.current_video = {}

            if self.inside == 2 and attr[0] == "href":
                self.current_video["url"] = attr[1]
            elif self.inside == 3 and attr[0] == "href":
                self.current_video["uploader_url"] = attr[1]

    def handle_endtag(self, tag):
        if tag == "div" and self.inside > 0:
            self.inside = 0
        # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        if self.inside == 1 and "Watched a video that has been removed" in data:
            self.inside = 0
            return
        if self.inside == 2:
            self.current_video["name"] = data
        elif self.inside == 3:
            self.current_video["uploader"] = data
        elif self.inside == 4:
            self.current_video["watched_date"] = data
            videos.append(self.current_video)

        if self.inside > 0:
            self.inside = (self.inside + 1) % 5

        # print("Encountered some data  :", data)

with open("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\watch-history_personal.html", "r", encoding="utf-8") as f:
    data = f.read()
    f.close()

parser = MyHTMLParser()
parser.feed(data)


for v in videos:
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

with open("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\personal_data.json", "w") as f:
    json.dump(videos, f)
    f.close()









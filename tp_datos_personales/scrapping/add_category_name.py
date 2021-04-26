import requests
import json
from urllib.parse import urlparse

API_KEY1 = "API_KEY1" #bail@itba.edu.ar
API_KEY2 = "API_KEY2" #zetapb@gmail.com
API_KEY3 = "API_KE3" #ail.brianez@gmail.com



categories = {}
def get_category_name(categoryId):
    if categoryId in categories:
        return categories[categoryId]
    else:
        categoryName = get_category_name_from_api(categoryId)
        if categoryName:
            categories[categoryId] = categoryName
            return categoryName

def get_category_name_from_api(categoryId):
    url = "https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&id={}&key={}".format(categoryId, API_KEY3)
    response = requests.get(url)
    if response.status_code == 200:
        j =  response.json()
        if j and "items" in j and len(j["items"]) > 0 and "snippet" in j["items"][0] and "title" in j["items"][0]["snippet"]:
            return j["items"][0]["snippet"]["title"]
    else:
        print("Unable to get details: {}".format(response.status_code))

with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data.json') as json_file:
    data = json.load(json_file)

for v in data:
    if "categoryId" in v:
        categoryname = get_category_name(v["categoryId"])
        v["category"] = categoryname

with open("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data_with_category.json", "w") as f:
    json.dump(data, f)
    f.close()





import json


with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\personal_data.json') as json_file:
    personal_data = json.load(json_file)

with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\itba_data.json') as json_file:
    itba_data = json.load(json_file)



for v in personal_data:
    v["type"] = "personal"

for v in itba_data:
    v["type"] = "itba"

merged_data = personal_data + itba_data
with open("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data.json", "w") as f:
    json.dump(merged_data, f)
    f.close()



import json

# Open
with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data_with_category.json') as json_file:
    data = json.load(json_file)

for v in data:
    if "tags" in v:
        v.pop("tags")

# # Save
with open("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data_without_tags.json", "w") as f:
    json.dump(data, f)
    f.close()



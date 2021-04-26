import json



with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data_with_category.json') as json_file:
    data = json.load(json_file)

print(len(data))
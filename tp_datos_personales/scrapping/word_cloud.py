import re
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import json

# Credit to el word cloud de Nachito: https://github.com/ignacioVidaurreta/infovis/blob/gh-pages/processing/cloud.py
_RE_COMBINE_WHITESPACES = re.compile(r"\s+")

def normalize_word(line):
    return _RE_COMBINE_WHITESPACES.sub(" ", line.replace("-", " ")).strip().upper()


# Open
with open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\merged_data_with_category.json') as json_file:
    data = json.load(json_file)

tags = {}
for v in data:
    if "tags" in v:
        for tag in v["tags"]:
            tag = normalize_word(tag)
            if len(tag) <= 3:
                continue
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1


mask = np.array(Image.open('C:\\Users\\Brian\\Downloads\\tp_datos_personales\\comment_mask.png'))

wc = WordCloud(width=4000, height=3000, random_state=1, max_words=70,
                      background_color='black', colormap='Pastel1', collocations=False,
                      stopwords=STOPWORDS, normalize_plurals=True, mask=mask
                      ).generate_from_frequencies(tags)
# plt.axis("off")
# plt.figure(figsize=(50, 40))
# # plt.imshow(wordcloud, interpolation='bilinear')
wc.to_file("C:\\Users\\Brian\\Downloads\\tp_datos_personales\\word_cloud.jpg")

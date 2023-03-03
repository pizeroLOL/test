import requests
import os

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"}

ul_begin = "<ul class=\"movie-list\">"
href_begin = "href=\""
href_after = "\""

url = "https://news.cyol.com/gb/channels/vrGlAKDl/index.html"

next_web_begin = "<title>"
next_web_after = "<"

html = requests.get(url=url, headers=headers)
html.encoding = 'utf-8'
html = html.text
start = html.find(ul_begin)

herf_start = html.find(href_begin, start)+len(href_begin)
herf_end = html.find(href_after, herf_start)
url = html[herf_start:herf_end]
end_slash = url.rfind("/")

next_web = requests.get(url=url, headers=headers)
next_web.encoding = 'utf-8'
next_web = next_web.text

next_web_start = next_web.find(next_web_begin)+len(next_web_begin)
next_web_end = next_web.find(next_web_after, next_web_start)
title = next_web[next_web_start:next_web_end]

output = url[:end_slash]+"/images/end.jpg"


bad_web = "<!DOCTYPE html><html lang=\"zh-Hants\"><head><meta charset=\"UTF-8\"><meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>" +\
    title+"</title><style>* {margin: 0;background-color: black;}div {text-align: center;position: absolute;align-items:center;align-self: center;width: 100%;height: 100%;}img {max-height: 100vh;max-width: 100vw;align-self: center;}</style></head><body><div><img src=\"" +\
    output+"\"></div></body></html>"

with open("index.html", "w") as file:
    file.write(bad_web)


# c = "#/bin/sh\
#     \ncurl `echo $TEST` -H \'Content-Type: application/json\' -d \'{\"msgtype\": \"text\",\"text\": {\"content\": \""+output+"\"}}\'\
#     \n\ncurl `echo $DingAPI` -H 'Content-Type: application/json' -d '{\"msgtype\": \"text\",\"text\": {\"content\":\""+output+"\"}}'"

# with open("send.sh", "w") as t:
#     t.write(c)
# os.system("sh send.sh")

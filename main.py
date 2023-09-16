import requests
import re
import os


def get(url: str):
    html = requests.get(url=url, headers=headers)
    html.encoding = 'utf-8'
    return html.text


def get_abouts(text: str):
    movie_list = re.findall(get_list, text)[0]
    movie_items = re.findall("<li>(.*?)</li>", movie_list)
    movie_about = map(lambda x: re.findall(get_item, x)[0][0], movie_items)
    return movie_about


def get_title_and_end(url: str):
    html = get(url)
    title: str = re.findall(get_title, html)[0]
    image: str = url.replace("m.html", "images/end.jpg")
    return title, image


def io_write_output(title: str, image: str):
    output_file = f"{output_dir}{title}.html"
    if os.path.isfile(output_file):
        return title, f"{title}.html"

    output = bad_web.replace("<!-- [TITLE] -->", title)
    output = output.replace("<!-- [IMAGE] -->", image)
    with open(output_file, "w") as f:
        f.write(output)
    print(output_file)
    return title, f"{title}.html"


def gen_index(files, is_server=False):
    path = f"{output_dir}index.html"
    if os.path.isfile(path):
        os.remove(path)
    output = []
    for title, file in files:
        ir = f"<li><a href=\"{file}\">{title}</a></li>"
        output.append(ir)
    index = bad_web_index.replace("<!-- [FILE] -->", "\n".join(output))
    if is_server is True:
        output = index.replace(
            "<!-- [UPDATE] -->", "<a href=\"/update\">更新数据</a>")
    # print(index)
    with open(path, "w") as f:
        f.write(index)


def init():
    if os.path.isfile(output_dir):
        print(f"检查 {output_dir} 是否为文件")
        exit(1)
    if os.path.exists(output_dir) is not True:
        # os.rmdir(output_dir)
        os.mkdir(output_dir)


def main(is_server=False):
    init()
    first_web = get(url).replace("\n", "").replace("  ", "")
    print("get first web OK")

    movie_about = get_abouts(first_web)

    print("get movies OK")

    titles_images = map(get_title_and_end, movie_about)
    index = []
    for title, image in titles_images:
        ir = io_write_output(title, image)
        index.append(ir)
    gen_index(index, is_server)


url = "https://news.cyol.com/gb/channels/vrGlAKDl/index.html"
bad_web = ""
bad_web_index = ""
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

output_dir = "public/"

get_list = "<ul class=\"movie-list\">(.*?)</ul>"
get_item = "<a href=\"(.*?)\" class=\"transition\" target=\"_blank\">(.*?)</a>"
get_title = "<title>(.*?)</title>"

with open("./template/bad_web.html", "r") as f:
    bad_web = "".join(f.readlines())
with open("./template/index.html", "r") as f:
    bad_web_index = "".join(f.readlines())


if __name__ == '__main__':
    main()

from bs4 import BeautifulSoup
import requests

get_url = lambda root, topic: root + topic 
get_html = lambda url: requests.get(url).text
parse_html = lambda text: BeautifulSoup(text, "html.parser")
extract_infobox = lambda html: html.find_all("table", {"class": "infobox vcard"}) # TODO: Need better way to specify target

replace_spaces = lambda text, seperator: text.replace(" ", seperator)
create_filename = lambda topic: topic + ".md"

def save_infobox(file_name, content):
    with open(file_name, "w+") as file:
        file.write(str(content))

def main():
    root_url = "https://en.wikipedia.org/wiki/"
    topic = replace_spaces("Barack Obama", "_")

    url = get_url(root_url, topic)
    html = parse_html(get_html(url))
    infobox = extract_infobox(html)

    file_name = create_filename(topic)
    save_infobox(file_name, infobox)


if __name__ == "__main__":
    main()
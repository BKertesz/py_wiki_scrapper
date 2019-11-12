from bs4 import BeautifulSoup
import requests, general_helpers

get_url = lambda root, topic: root + topic 
get_html = lambda url: requests.get(url).text
parse_html = lambda text: BeautifulSoup(text, "html.parser")
extract_infobox = lambda html: html.find_all("table", {"class": "infobox"})
extract_text = lambda element: element.find_all(text=True) if element != None else ["Unkown Page"]

def extract_data(list_of_topics, base_url="https://en.wikipedia.org/wiki/"):
    infobox_content = {}
    for item in list_of_topics:
        topic_url = general_helpers.replace_spaces(item)
        complete_url = get_url(base_url, topic_url)
        raw_page = get_html(complete_url)
        html_content = parse_html(raw_page)
        infobox = extract_infobox(html_content)
        text = extract_text(general_helpers.head(infobox))
        infobox_content[item] = text
    return infobox_content


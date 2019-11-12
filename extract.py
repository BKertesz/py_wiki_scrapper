from bs4 import BeautifulSoup
import requests

get_url = lambda root, topic: root + topic 
get_html = lambda url: requests.get(url).text # TODO: Error checking to see if there is no page of that context
parse_html = lambda text: BeautifulSoup(text, "html.parser")
extract_infobox = lambda html: html.find_all("table", {"class": "infobox vcard"}) # TODO: Need better way to specify target
extract_text = lambda element: element.find_all(text=True)

head = lambda list_object: list_object[0]
replace_spaces = lambda text: text.replace(" ", "_")

def extract_data(list_of_topics, base_url="https://en.wikipedia.org/wiki/"):
    infobox_content = {}
    for item in list_of_topics:
        topic_url = replace_spaces(item)
        complete_url = get_url(base_url, topic_url)
        raw_page = get_html(complete_url)
        html_content = parse_html(raw_page)
        infobox = extract_infobox(head(html_content))
        text = extract_text(infobox)
        infobox_content[item] = text
    return infobox_content

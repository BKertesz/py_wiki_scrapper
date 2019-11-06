from bs4 import BeautifulSoup
import requests

root_url = "https://en.wikipedia.org/wiki/"
topic = "Barack_Obama"

get_url = lambda root, topic: root + url 
get_html = lambda url: requests.get(url).text
parse_html = lambda text: BeautifulSoup(text, "html.parser")
extract_infobox = lambda html: html.find_all("table", {"class": "infobox vcard"}) # TODO: Need better way to specify target

open_file = lambda file_name: open(file_name, "w+")
write_file = lambda file, content: file.write(content)
close_file = lambda file: file.close() 

def save_infobox(file_name, content):
    with open(file_name) as file:
        file.write(content)

def main():
    url = get_url(root_url, topic) # TODO: Need to replace spaces with underscore

if __name__ == "__main__":
    main()
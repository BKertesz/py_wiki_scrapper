from bs4 import BeautifulSoup
import requests

topic = "Barack_Obama"
wikipedia_url = f"https://en.wikipedia.org/wiki/{topic}"
target_class = "infobox vcard"

response = requests.get(wikipedia_url).text
html_file = BeautifulSoup(response, "html.parser")
infobox = html_file.find_all("table", {"class": "infobox vcard"})


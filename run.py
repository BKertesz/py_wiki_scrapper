from bs4 import BeautifulSoup
import requests, argparse

get_url = lambda root, topic: root + topic 
get_html = lambda url: requests.get(url).text # TODO: Error checking to see if there is no page of that context
parse_html = lambda text: BeautifulSoup(text, "html.parser")
extract_infobox = lambda html: html.find_all("table", {"class": "infobox vcard"}) # TODO: Need better way to specify target
extract_text = lambda element: element.find_all(text=True)

replace_spaces = lambda text, seperator: text.replace(" ", seperator)
create_filename = lambda topic: topic + ".md" # TODO: Select rather what type of file you wish to contain the text

def parse_command_line():
    parser = argparse.ArgumentParser("Input names surroneded by \" \", if wish to save result use the -S or --save flag.")
    parser.add_argument('names', metavar='N', type=str, nargs="+",help="A name or a list of names of inviduals.")
    parser.add_argument("--save" ) # TODO: An argument with -s and --save to save the search to content


def save_infobox(file_name, content):
    with open(file_name, "w+") as file:
        file.write(str(content))

def main():
    root_url = "https://en.wikipedia.org/wiki/"
    topic = replace_spaces("Barack Obama", "_")

    url = get_url(root_url, topic)
    html = parse_html(get_html(url))
    infobox = extract_infobox(html)[0]
    text = extract_text(infobox)

    # Currently the code downloads and extracts the next, for next step it needs to write it to a file.
    # TODO: Rename this file to extract and parse, maybe seperate to two different file
    # TODO: Create a new file that is the search options
    # TODO: Create a structure more of a module, so files can be easily accessed as functions

if __name__ == "__main__":
    main()
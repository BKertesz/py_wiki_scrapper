import extract, file_helper

def main():
    list_of_pages = ["Barack Obama", "Donald Trump", "Mike Pence"]
    result = extract.extract_data(list_of_pages)
    file_helper.save_contents_to_file(result)

if __name__ == "__main__":
    main()
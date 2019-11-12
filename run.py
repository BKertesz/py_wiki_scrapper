import scraper, file_helper, cli

def main():
    list_of_topics = cli.retrive_arguments()
    result = scraper.extract_data(list_of_topics)
    file_helper.save_contents_to_file(result)

if __name__ == "__main__":
    main()
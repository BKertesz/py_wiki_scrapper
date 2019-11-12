import cli, file_helper

def search_terms(list_of_terms):
    # load index file
    # load all file content from index file
    # create result dictionary
    # if term exits in file content
    # then add key to that term in dictionary
    # return dictionary
    pass

def main():
    list_of_searched_terms = cli.retrive_arguments()
    results = search_terms(list_of_searched_terms)
    print(results)

if __name__ == "__main__":
    main()
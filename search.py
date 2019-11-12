import cli, file_helper

def search_terms(list_of_terms, file_contents):
    result = {}
    for key, contents in file_contents.items():
        for term in list_of_terms:
            if(term in contents):
                result[key] = (term, contents)
    return result

def main():
    list_of_searched_terms = cli.retrive_arguments()
    index_file = "index.txt"
    index_content = file_helper.load_content(index_file)
    file_contents = file_helper.load_all_from_index(index_content)
    results = search_terms(list_of_searched_terms, file_contents)
    print(results)

if __name__ == "__main__":
    main()
import cli, file_helper

def main():
    list_of_searched_terms = cli.retrive_arguments()
    result = file_helper.load_content("barack_obama.txt")
    print(result)

if __name__ == "__main__":
    main()
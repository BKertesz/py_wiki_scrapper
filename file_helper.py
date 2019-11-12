create_filename = lambda topic: topic + ".txt" # TODO: Select rather what type of file you wish to contain the text

def save_to_file(file_name, content):
    with open(file_name, "w+") as file:
        file.write(str(content))

def save_contents_to_file(dictionary):
    for key, value in dictionary:
        save_to_file(create_filename(key, value))
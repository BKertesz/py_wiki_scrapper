import general_helpers

create_filename = lambda topic: general_helpers.replace_spaces(topic.lower()) + ".txt"
list_to_string = lambda list_object: "\n".join(list_object)

def save_to_file(file_name, content):
    with open(file_name, "w+") as file:
        file.write(content)

def save_contents_to_file(dictionary):
    for key, value in dictionary.items():
        save_to_file(create_filename(key), list_to_string(value))
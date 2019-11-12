import general_helpers, os

create_filename = lambda topic: general_helpers.replace_spaces(topic.lower()) + ".txt"
list_to_string = lambda list_object: "\n".join(list_object)
is_present_in_index = lambda topic_name, index_content: True if topic_name in index_content else False
is_not_present_in_index = lambda topic_name, index_content: not is_present_in_index(topic_name, index_content)

def save_to_file(file_name, content):
    with open(file_name, "w+", encoding="utf-8") as file:
        file.write(content)

def create_index(file_name="index.txt"):
    if(not os.path.exists(file_name)):
        save_to_file(file_name, "")

def load_content(file_name):
    file_content = ""
    with open(file_name, "r", encoding="utf-8") as file:
        file_content = file.read()
    return file_content.splitlines()

def update_index(topic_name, index_name="index.txt"):
    index_content = load_content(index_name)
    if(is_not_present_in_index(topic_name, index_content)):
        save_to_file(index_name, general_helpers.append_with_new_line(index_content, topic_name))

def save_contents_to_file(dictionary):
    create_index()
    for key, value in dictionary.items():
        save_to_file(create_filename(key), list_to_string(value))
        update_index(key)

def load_contents_from_list(list_of_file_names):
    contents = {}
    for item in list_of_file_names:
        contents[item] = load_content(create_filename(item))
    return contents

def load_all_from_index(index_content):
    return load_contents_from_list(index_content)

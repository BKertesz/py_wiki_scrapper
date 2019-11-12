import general_helpers, os

create_filename = lambda topic: general_helpers.replace_spaces(topic.lower()) + ".txt"
list_to_string = lambda list_object: "\n".join(list_object)

def save_to_file(file_name, content):
    with open(file_name, "w+", encoding="utf-8") as file:
        file.write(content)

def load_content(filename):
    file_content = ""
    with open(file_name, "r", encoding="utf-8") as file:
        file_content = file.read()
    return file_content

def save_contents_to_file(dictionary):
    for key, value in dictionary.items():
        save_to_file(create_filename(key), list_to_string(value))

def create_index(file_name="index.txt"):
    if(not os.path.exists(file_name)):
        save_to_file(file_name, "")

def update_index(index_name="index.txt",topic_name):
    index_content = load_content(index_name)
    if(not topic_name in index_content):
        save_to_file(index_name, index_content.append(topic_name))
        

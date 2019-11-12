head = lambda sequence: sequence[0] if len(sequence) else None
replace_spaces = lambda text: text.replace(" ", "_")
append_with_new_line = lambda text, string: text + "\n" + string if len(text) else string
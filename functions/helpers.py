def _get_file_content_as_string(filename):
    with open('../input/' + filename, 'r') as file:
        return file.read()


def get_file_content_as_int_list(filename):
    content = _get_file_content_as_string(filename)
    new_list = []

    for char in content:
        new_list.append(int(char))

    return new_list

def get_file_content_as_string(filename):
    with open('../input/' + filename, 'r') as file:
        return file.read()


def get_file_content_as_lines_list(filename):
    return get_file_content_as_string(filename).split('\n')


def get_file_content_as_lines_int_list(filename):
    return list(map(lambda s: int(s), get_file_content_as_lines_list(filename)))


def get_file_content_as_int_list(filename):
    content = get_file_content_as_string(filename)
    new_list = []

    for char in content:
        new_list.append(int(char))

    return new_list


def get_tvs_file_content_as_int_spreadsheet(filename):
    lines = get_file_content_as_lines_list(filename)
    outer_list = []

    for line in lines:
        inner_list = line.split('\t')
        outer_list.append(list(map(lambda word: int(word), inner_list)))

    return outer_list


def get_file_content_as_single_int(filename):
    return int(get_file_content_as_string(filename))

def calculate_spreadsheet_checksum_day2_1(sheet):
    sum_sheet = 0
    for row in sheet:
        sum_sheet += max(row) - min(row)
    return sum_sheet


def calculate_spreadsheet_checksum_day2_2(sheet):
    sum_sheet = 0
    for row in sheet:
        numbers = _find_evenly_divisive_numbers_tuple(row)
        sum_sheet += numbers[0] / numbers[1]
    return sum_sheet


def _find_evenly_divisive_numbers_tuple(input_list):
    number_a = -1
    number_b = -1
    done = False

    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i == j:
                continue

            if input_list[i] % input_list[j] == 0:
                number_a = input_list[i]
                number_b = input_list[j]
                done = True
                break

        if done:
            break

    return number_a, number_b

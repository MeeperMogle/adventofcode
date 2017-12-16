def calculate_spreadsheet_checksum_day2_1(sheet):
    sum_sheet = 0
    for row in sheet:
        sum_sheet += max(row) - min(row)
    return sum_sheet

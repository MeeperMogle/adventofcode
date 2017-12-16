def solve_captcha_day1_1(arr):
    # The captcha requires you to review a sequence of digits (your puzzle input)
    # and find the sum of all digits that match the next digit in the list.
    # The list is circular, so the digit after the last digit is the first digit in the list.

    arr.append(arr[0])

    captcha_sum = 0

    for i in range(len(arr) - 1):
        captcha_sum += arr[i] if arr[i] == arr[i + 1] else 0

    return captcha_sum

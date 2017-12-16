def solve_captcha_day1_1(arr):
    # The captcha requires you to review a sequence of digits (your puzzle input)
    # and find the sum of all digits that match the next digit in the list.
    # The list is circular, so the digit after the last digit is the first digit in the list.

    new_arr = arr[:]
    new_arr.append(new_arr[0])

    captcha_sum = 0

    for i in range(len(new_arr) - 1):
        captcha_sum += new_arr[i] if new_arr[i] == new_arr[i + 1] else 0

    return captcha_sum


def solve_captcha_shift(arr, shift=1):
    # Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular
    # list. That is, if your list contains 10 items, only include a digit in your sum if the digit
    # 10 / 2 = 5 steps forward matches it.Fortunately, your list has an even number of elements.
    captcha_sum = 0

    for i in range(len(arr)):
        compare_index = i + shift if i + shift < len(arr) else i + shift - len(arr)
        captcha_sum += arr[i] if arr[i] == arr[compare_index] else 0

    return captcha_sum

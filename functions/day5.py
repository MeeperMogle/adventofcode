def jumps_required_to_escape_offsets(offset_list, decrement_on_higher_than_two=False):
    increment_after_jump = 1
    index = 0
    steps_taken = 0

    while index < len(offset_list):
        index_before_decrease = index

        higher_than_two = offset_list[index] > 2

        index += offset_list[index]
        offset_list[index_before_decrease] += increment_after_jump

        if decrement_on_higher_than_two and higher_than_two:
            offset_list[index_before_decrease] -= increment_after_jump
            offset_list[index_before_decrease] -= 1

        steps_taken += 1

    return steps_taken

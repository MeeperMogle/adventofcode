def jumps_required_to_escape_offsets(offset_list):
    increment_after_jump = 1
    index = 0
    steps_taken = 0

    while index < len(offset_list):
        index_before_decrease = index
        index += offset_list[index]
        offset_list[index_before_decrease] += increment_after_jump
        steps_taken += 1

    return steps_taken

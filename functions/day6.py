def find_highest_index(the_list):
    highest = max(the_list)
    return the_list.index(highest)


def give_if_store_has_left(the_list, index_target, index_store):
    still_to_distribute = the_list[index_store]
    if still_to_distribute > 0:
        the_list[index_store] -= 1
        the_list[index_target] += 1


def redistributed_to_others(the_list, index):
    other_list = the_list[:]

    current_index = index + 1 if index + 1 < len(the_list) else 0

    while current_index != index:
        give_if_store_has_left(other_list, index_target=current_index, index_store=index)
        current_index = current_index + 1 if current_index + 1 < len(the_list) else 0

    return other_list[:]


def steps_until_earlier_state_reached(original_list):
    previous_states = [original_list[:]]
    new_list = original_list[:]

    new_list = redistributed_to_others(new_list, find_highest_index(new_list))
    steps_done = 1

    while True:
        new_list = redistributed_to_others(new_list, find_highest_index(new_list))

        if new_list in previous_states:
            break

        previous_states.append(new_list[:])

        steps_done += 1

    return steps_done

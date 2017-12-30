def find_highest_index(list):
    highest = max(list)
    return list.index(highest)


def redistributed_to_others(list, index):
    other_list = list[:]
    value = other_list[index]
    sharing = len(other_list) - 1
    keep = value % sharing
    each_get = int(value / sharing)
    other_list[index] = keep

    for i in range(0, len(other_list)):
        if i == index:
            continue
        other_list[i] += each_get
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

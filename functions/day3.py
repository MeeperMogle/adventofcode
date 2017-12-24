# Start increments
# Top left: 4
# Mid left: 5
# Bot left: 6
# Mid top: 3
# Mid bot: 7
# Top right: 2
# Mid right: 1
# Bot right: 8


def find_outer_side(steps, start_increase):
    on = 1
    increase = start_increase
    steps_taken = 0

    while steps_taken < steps:
        on += increase
        increase += 8
        steps_taken += 1
    return on


def num_top_right_after_steps(steps):
    return find_outer_side(steps, 2)


def num_mid_right_after_steps(steps):
    return find_outer_side(steps, 1)


def num_top_left_after_steps(steps):
    return find_outer_side(steps, 4)


def num_bot_left_after_steps(steps):
    return find_outer_side(steps, 6)


def num_mid_top_after_steps(steps):
    return find_outer_side(steps, 3)


def num_mid_left_after_steps(steps):
    return find_outer_side(steps, 5)


def num_mid_bot_after_steps(steps):
    return find_outer_side(steps, 7)


def calculate_steps_needed(target):
    on = 1

    if target == on:
        return 0

    bottom_rights = []

    increase = 8

    while on < target:
        on += increase
        increase += 8

        bottom_rights.append(on)

    steps_outward = len(bottom_rights)

    top_right = num_top_right_after_steps(steps_outward)
    top_left = num_top_left_after_steps(steps_outward)
    bot_left = num_bot_left_after_steps(steps_outward)
    bot_right = bottom_rights[-1]

    if target in (top_right, top_left, bot_left, bot_right):
        return steps_outward * 2

    if target < top_right:
        straight_right = num_mid_right_after_steps(steps_outward)
        return steps_outward + abs(straight_right - target)
    elif target < top_left:
            straight_up = num_mid_top_after_steps(steps_outward)
            return steps_outward + abs(straight_up - target)
    elif target < bot_left:
            straight_left = num_mid_left_after_steps(steps_outward)
            return steps_outward + abs(straight_left - target)
    elif target < bot_right:
            straight_down = num_mid_bot_after_steps(steps_outward)
            return steps_outward + abs(straight_down - target)
    else:
        print('Broke the rules of mathematics, the number does not exist...')

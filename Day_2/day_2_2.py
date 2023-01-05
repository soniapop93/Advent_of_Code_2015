input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def total_ribbon(input_list):
    total_ribbon = 0
    for i in input_list:
        splited_i = i.split("x")
        l_length = int(splited_i[0])
        w_width = int(splited_i[1])
        h_height = int(splited_i[2])

        list_values = [l_length, w_width, h_height]
        first_min_value = min(list_values)
        list_values.remove(first_min_value)
        second_min_value = min(list_values)

        ribbon_needed = (first_min_value + first_min_value + second_min_value + second_min_value) + (
                    l_length * w_width * h_height)
        total_ribbon += ribbon_needed
    return total_ribbon


print(total_ribbon(input_list))

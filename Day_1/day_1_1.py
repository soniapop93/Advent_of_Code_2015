input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def get_floor(input_list):
    count_floor = 0
    for i in input_list[0]:
        if "(" in i:
            count_floor += 1
        else:
            count_floor -= 1

    return count_floor


print(get_floor(input_list))

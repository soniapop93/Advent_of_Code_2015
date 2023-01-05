input_list = []

with open("input.txt", "r+") as f:
    input_list = [line.replace("\n", "") for line in f]

print(input_list)


def total_value_of_paper(input_list):
    total_wrapping_paper = 0
    for i in input_list:
        splited_i = i.split("x")
        l_length = int(splited_i[0])
        w_width = int(splited_i[1])
        h_height = int(splited_i[2])
        slack_value = 0

        l_w = l_length * w_width
        l_h = l_length * h_height
        w_h = w_width * h_height

        slack_value = min([l_w, l_h, w_h])

        paper_needed = 2 * l_length * w_width + 2 * w_width * h_height + 2 * h_height * l_length

        total_wrapping_paper = total_wrapping_paper + (paper_needed + slack_value)

    return total_wrapping_paper


print(total_value_of_paper(input_list))

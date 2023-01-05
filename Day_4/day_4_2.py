import hashlib

input_string = "bgvyzdsv"


def find_hash_value(input_string):
    counter = 0
    while True:
        value_to_check = input_string + str(counter)
        hash_string = hashlib.md5(value_to_check.encode('utf-8')).hexdigest()

        if "000000" in hash_string[:6]:
            return counter
        counter += 1


print(find_hash_value(input_string))

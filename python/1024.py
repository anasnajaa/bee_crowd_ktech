# https://www.beecrowd.com.br/judge/en/problems/view/1024

# string
# chr (94)
# ord ('a')
# divmod(4, 2)

# each uppercase or lowercase letter must be shifted three positions to the right
# each line must be reversed
# "all characters" from the half on (truncated) must be moved one position to the left in ASCII
import string


def execute_test_case(test_case):
    shifted_string = ""
    reveresed_string = ""
    shifted_second_half_string = ""

    for character in test_case:
        if (character in string.ascii_letters):
            char_order = ord(character)
            char_order = char_order + 3
            shifted_string += chr(char_order)
        else:
            shifted_string += character

    reveresed_string = shifted_string[::-1]

    # split in half
    reveresed_string_length = len(reveresed_string)
    half_point, remainder = divmod(reveresed_string_length, 2)

    first_half = reveresed_string[0:half_point]
    second_half = reveresed_string[half_point:reveresed_string_length]

    # truncate
    first_half = first_half
    second_half = second_half

    for character in second_half:
        char_order = ord(character)
        char_order = char_order - 1
        shifted_second_half_string += chr(char_order)

    print(first_half + shifted_second_half_string)


# manual testing
counter = 1
rounds = int(input())

while counter <= rounds:
    test_case = input()
    execute_test_case(test_case)
    counter = counter + 1

# automated testing
# test_cases = ["Texto #3", "abcABC1", "vxpdylY .ph", "vv.xwfxo.fd"]
# for test_case in test_cases:
#     execute_test_case(test_case)

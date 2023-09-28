# https://www.beecrowd.com.br/judge/en/problems/view/1168

# LEDS of numbers 0 1 2 3 4 5 6 7 8 9
numbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

rounds = int(input())
counter = 1

numbers_to_leds = [None] * rounds

while counter <= rounds:
    numbers_to_leds[counter-1] = input()
    leds_nums = list(numbers_to_leds[counter-1])

    total = 0

    for num in leds_nums:
        total += numbers[int(num)]

    print("{number} leds".format(number=total))

    counter = counter + 1

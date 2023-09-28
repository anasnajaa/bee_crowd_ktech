# if conditions
age = 10
if age >= 10:
    print('Above 10')
else:
    print('Below 10')


# multiple if conditions
is_hot = False
is_cold = False

if is_hot:
    print("Hot day")
    print("Drink water")
elif is_cold:
    print("cold day")
    print("Wear coat")
else:
    print("its a lovely day")

print("Enjoy your day")


# comparison operators and nested conditions

has_high_income = True
has_good_credit = False
has_criminal_record = True

if not has_criminal_record:
    if has_high_income and has_good_credit:
        print("Eligible for loan")
    elif has_high_income or has_good_credit:
        print("Eligible for small loan")
else:
    print("loan denied, criminal record found")


# nested comparison operators
temperature = -1

if temperature > 30:
    print("it's a hot day")
elif temperature >= 20:
    print("it's a warm day")
elif temperature >= 10:
    print("it's a cold day")
elif temperature > 0:
    print("it's freezing")
elif temperature == 0:
    print("temp is 0")
else:
    print("It's below zero")

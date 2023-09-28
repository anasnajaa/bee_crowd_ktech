# variables
x = 5
y = "John"
print(x)
print(y)

"""------------------"""

x = 4        # x is of type int
x = "Sally"  # x is now of type str
print(x)

"""------------------"""

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

"""------------------"""

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


n = "246.2458"
n = float(n)
print(int(n))


# arithmetic operators
print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)


# assignment operators
x = 10
x = x + 3
print(x)

x += 3
print(x)

x -= 3
print(x)


# Operators Precedence
# **
# * / % //
# + -

x = 10 + 3 * 2
print(x)

y = 10 * 2 + 3
print(y)

z = 10 * 2 + 3 ** 2
print(z)

t = 10 * (2 + 3) ** 2
print(t)

# https://www.beecrowd.com.br/judge/en/problems/view/1002

pi = 3.14159
r = float(input())
a = round(pi * r * r, 4)
a = "{:.4f}".format(a)
print("A={number}".format(number=a))

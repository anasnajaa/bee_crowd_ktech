'''
https://www.beecrowd.com.br/judge/en/problems/view/1011
'''
import math
# volume of a sphere
# provided the value of its radius (R)

# (4/3) * pi * R3
# pi the value 3.14159

pi = 3.14159
radius = int(input())
volume = (4/3) * (pi * radius ** 3)
print(f"VOLUME = {volume:.3f}")

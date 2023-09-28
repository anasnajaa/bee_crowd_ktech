# https://www.beecrowd.com.br/judge/en/problems/view/1005

A = float(input())
B = float(input())

W_A = float(3.5)
W_B = float(7.5)

A_FINAL = A * W_A
B_FINAL = B * W_B

MEDIA = (A_FINAL+B_FINAL)/(W_A+W_B)

MEDIA = "{:.5f}".format(MEDIA)
print("MEDIA = {number}".format(number=MEDIA))

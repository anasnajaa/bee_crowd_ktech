A=float(input())
B=float(input())
C=float(input())

W_A = float(2)
W_B = float(3)
W_C = float(5)

A_FINAL = A * W_A
B_FINAL = B * W_B
C_FINAL = C * W_C

MEDIA=(A_FINAL+B_FINAL+C_FINAL)/(W_A+W_B+W_C)

MEDIA = "{:.1f}".format(MEDIA)
print("MEDIA = {number}".format(number=MEDIA))
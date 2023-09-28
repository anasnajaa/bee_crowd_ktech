# https://www.beecrowd.com.br/judge/en/problems/view/1010

# inputs
# read a code of a product 1
# the number of units of product 1
# the price for one unit of product 1,

# calculate and show the amount to be paid

product_1_info = input()
product_2_info = input()

p1_code = product_1_info.split(" ")[0]
p1_units = product_1_info.split(" ")[1]
p1_units = int(p1_units)
p1_price = product_1_info.split(" ")[2]
p1_price = float(p1_price)

p2_code = product_2_info.split(" ")[0]
p2_units = product_2_info.split(" ")[1]
p2_units = int(p2_units)
p2_price = product_2_info.split(" ")[2]
p2_price = float(p2_price)

total_amount = (p1_units * p1_price) + (p2_units * p2_price)

print(f"VALOR A PAGAR: R$ {total_amount:.2f}")

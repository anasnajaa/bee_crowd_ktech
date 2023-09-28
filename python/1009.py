"""
https://www.beecrowd.com.br/judge/en/problems/view/1009

"""
# inputs
# reads a seller's name
# his/her fixed salary
# the sale's total made by himself/herself in the month

# seller receives 15% over all products sold

# outputs
# write the final salary (total) of this seller at the end of the month , with two decimal place

seller_name = input()
fixed_salary = float(input())
sales_total = float(input())

sales_total_with_comm = (sales_total * .15) + fixed_salary

print(f"TOTAL = R$ {sales_total_with_comm:.2f}")

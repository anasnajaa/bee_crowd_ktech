"""
https://www.beecrowd.com.br/judge/en/problems/view/1008
inputs
- read an employee's number
- his/her worked hours number in a month
- amount he received per hour

outputs
- Print the employee's number
- salary that he/she will receive at end of the month, with two decimal places
"""

employee_number = int(input())
employee_work_hours = int(input())
amount_per_hour = float(input())

salary = employee_work_hours * amount_per_hour
salary = "{:.2f}".format(salary)

print("NUMBER = {n1}".format(n1=employee_number))
print("SALARY = U$ {n1}".format(n1=salary))

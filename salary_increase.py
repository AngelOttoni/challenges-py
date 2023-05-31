salary = float(input())
initial_value = salary
if (initial_value <= 600.00):
    final_value = initial_value * 1.17
    readjustment = final_value - initial_value
    percentage = 17
elif (600.01 <= initial_value <= 900.00):
    final_value = initial_value * 1.13
    readjustment = final_value - initial_value
    percentage = 13
elif (900.01 <= initial_value <= 1500.00):
    final_value = initial_value * 1.12
    readjustment = final_value - initial_value
    percentage = 12
elif (1500.01 <= initial_value <= 2000.00):
    final_value = initial_value * 1.10
    readjustment = final_value - initial_value
    percentage = 10
else:
    final_value = initial_value * 1.05
    readjustment = final_value - initial_value
    percentage = 5
print('New salary: {:.2f}'.format(final_value).replace('.',','))
print('Readjustment received: {:.2f}'.format(readjustment).replace('.',','))
print('In percentage:: {} %'.format(percentage))

#or

# x = float(input())
# if x <= 400.00:
#     s = x * 1.15
#     r = s - x
#     p = 15
# if 400.01 <= x <= 800.00:
#     s = x * 1.12
#     r = s - x
#     p = 12
# if 800.01 <= x <= 1200.00:
#     s = x * 1.10
#     r = s - x
#     p = 10
# if 1200.01 <= x <= 2000.00:
#     s = x * 1.07
#     r = s - x
#     p = 7
# if  x > 2000.00:
#     s = x * 1.04
#     r = s - x
#     p = 4
# print('Novo salario: {:.2f}'.format(s).replace('.',','))
# print('Reajuste ganho: {:.2f}'.format(r).replace('.',','))
# print('Em percentual: {} %'.format(p))

# Salário	            Percentual de Reajuste
# 0 - 600.00          17%
# 600.01 - 900.00     13%
# 900.01 - 1500.00    12%
# 1500.01 - 2000.00   10%
# Acima de 2000.00    5%


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

#
salario = int(input())

reajustes = {
    600: 0.17,
    900: 0.13,
    1500: 0.12,
    2000: 0.10
}

reajuste = 0.05

for limite, percentual in reajustes.items():
    if salario <= limite:
        reajuste = percentual
        break

novo_salario = salario + (salario * reajuste)

print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {salario * reajuste:.2f}\nEm percentual: {reajuste * 100:.0f} %") 

# Salário	            Percentual de Reajuste
# 0 - 600.00          17%
# 600.01 - 900.00     13%
# 900.01 - 1500.00    12%
# 1500.01 - 2000.00   10%
# Acima de 2000.00    5%

#o que passou na plataforma:

salario = int(input())
reajuste = 0
if salario <= 600:
    reajuste = 0.17
elif salario <= 900:
    reajuste = 0.13
elif salario <= 1500:
    reajuste = 0.12
elif salario <= 2000:
    reajuste = 0.10
else:
    reajuste = 0.05
       
novo_salario= (salario *reajuste) + salario 
print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {salario * reajuste:.2f}\nEm percentual: {reajuste * 100:.0f} %") 
first_name = "Pero"
last_name = 'Peric'

#full_name = 'Puno ime osobe je: ' + first_name + " " + last_name
#full_name = 'Puno ime osobe je: Pero Peric'
#full_name = 'Puno ime osobe je: {1} {0}'.format(first_name, last_name)
full_name = f'Puno ime osobe je: {last_name} {first_name}'

print(full_name)



a = 5 
b = 8

result = f'Umnozak broja {a} i broja {b} je {a * b}'
print(result)
result = f'{a} * {b} = {a * b}'
print(result)



first = 192
second = 168
third = 0
fourth = 1

#print(f'IP adresa: {first}.{second}.{third}.{fourth}')


IP_address_for_print = f'IP adresa: {first}.{second}.{third}.{fourth}'
print(IP_address_for_print)

IP_address_for_print = f'IP adresa: {hex(first).removeprefix("0x")}.{second}.{third}.{fourth}'
print(IP_address_for_print)
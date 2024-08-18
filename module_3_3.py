def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b = 25)
print_params(c = [1,2,3])
print()

values_list = [3, 'Still', False]
values_dict = {'a': 22, 'b': 'Aero', 'c': False}
values_list_2 = [44, 55.05]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 101)

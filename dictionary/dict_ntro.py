vehicles = {
    # Key: Value
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

my_car = vehicles['er5']
car = vehicles.get('dream')
print(my_car, car, sep=" | ")
print()

# adding new key with value
vehicles['toy'] = 'glider'

# upgrading they old key value
vehicles['virago'] = 'Yamaha XC535'

# deleting keys and values
del vehicles['virago']
# del vehicles['f1']
result = vehicles.pop('f1', None)
print(result)
print()


# Iterating over dictionaries
# when we are iterating over dictionaries it will get us keys so if we want to access value we use indexing.
# for keys in vehicles:
#     print(keys, vehicles[keys], sep=", ")

for keys, values in vehicles.items():
    print(keys, values, sep=", ")

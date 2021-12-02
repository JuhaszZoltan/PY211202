# csak python:

nev = input('neved: ')
# print(f'{nev}\n' * 10)

# range(10) -> előállítja a számokat [0; 10) között 
# azaz: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(5, 10) -> [5, 6, 7, 8, 9]

# range(3, 10, 3) -> [3; 10) között minden harmadikat
# azaz [3, 6, 9]

for i in range(10):
    print(f'{i + 1}.: {nev}')
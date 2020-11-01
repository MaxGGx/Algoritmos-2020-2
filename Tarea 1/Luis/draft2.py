import random

def suma(array, num=6):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in suma(array[1:], num):
        yield solution
    for solution in suma(array[1:], num - array[0]):
        yield [array[0]] + solution

#array = [6,4,3,3,3,2,2,2]
array = []
for x in range(50):
    array.append(random.randint(1,10))
print(array)
print(list(suma(array,27)))
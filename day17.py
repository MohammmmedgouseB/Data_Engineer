# data = (10, 20, 30)
# numbers = list(data)
# numbers[1]=200
# data = tuple(numbers)
# print(data)

data = (10, 20, 30, 20, 40, 20)
smallest = data[0]
for i in data:
    if smallest > i :
        smallest = i
print(smallest)


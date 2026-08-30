# numbers = [10, 15, 20, 25, 30, 35]
# result =[i**2 for i in numbers if i > 20]
# print(result)

# numbers = [5, 10, 15, 20, 25, 30]
# result = [i*2 for i in numbers if i%2==0]
# print(result)

data = [
    [10, 15],
    [20, 25],
    [30, 35]
]
Result = [j for i in data for j in i if j%2==0]
print(Result)
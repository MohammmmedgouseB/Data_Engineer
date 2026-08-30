
# try:
#     a = int(input("Enter a num : "))
#     b = int(input("enter b num : "))
#     res = a/b
# except ValueError:
#     print("enter  a valid number")
# except ZeroDivisionError:
#     print("the number cannot divide by zero")
# else:
#     print(res)
# finally:
#     print("program ran successfully")

# try:
#     student = {
#     "name": "Gouse",
#     "age": 22
# }
#     a = input("Enter the key : ")
#     res = student[a]
# except KeyError:
#     print("Enter the valid key")
# else:
#     print(res)

try : 
    numbers = [10, 20, 30]
    a =  int(input("enter the index"))
    res = numbers[a]
except IndexError:
    print("enter valid index")
else:
    print(res)
# with open("skills.txt","w") as file :
#     data = file.write("Python\n")
#     data = file.write("SQL\n")
#     data = file.write("Pyspark\n")

# with open("skills.txt","a") as file:
#     file.write("pandas\n")

# with open("skills.txt","r") as file :    
#     data = file.read()
# print(data)

# with open("numbers.txt","w") as file:
#     file.write("10\n")
#     file.write("20\n")
#     file.write("30\n")
#     file.write("40\n")
#     file.write("50\n")

# with open("numbers.txt","r")as file:
#     sum = 0
#     for i in file:
#         sum+=int(i)
# print(sum)

# with open("numbers.txt","w") as file:
#     file.write("10\n")
#     file.write("25\n")
#     file.write("7\n")
#     file.write("40\n")
#     file.write("18\n")
# with open("numbers.txt","r")as file:
#     for i in file:
#         if int(i) > 20:
#             print(int(i))

employees = {
    "Gouse": 22,
    "Rahul": 25,
    "Arun": 19,
    "Vijay": 28
}
with open("employees.txt","w") as file:
    for name, age in employees.items():
        file.write(f"{name},{age}\n")

with open("employees.txt","r") as file:
    for  i in file:
        name , age = i.strip().split(",")
        if age > 25:
            print(name,age)
 
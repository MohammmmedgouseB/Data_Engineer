employees = {
    "Gouse": [22, "Coimbatore", "Python"],
    "Rahul": [25, "Chennai", "SQL"],
    "Arun": [19, "Bangalore", "Python"],
    "Vijay": [28, "Coimbatore", "PySpark"],
    "Priya": [24, "Chennai", "Pandas"]
}

with open ("employees.txt","w") as file:
    for name,details in employees.items():
        file.write(f"{name},{details[0]},{details[1]},{details[2]}\n")

with open("employees.txt","r") as file:
    count = 0
    sum_age = 0
    avg_age = 0 
    for i in file:
        name,age,city,skill = i.strip().split(",")
        sum_age += int(age)
        count+=1
    avg_age = sum_age/count
    print(avg_age)
        

    #     if largest < int(age):
    #         largest = int(age)
    #         largest_name = name
    #         largest_age = age
    # print(f"Oldest employee : {largest_name}")
    # print(f"Age: {largest_age}")

 
                


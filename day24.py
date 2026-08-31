employees = {
    "Gouse": [22, "Coimbatore", "Python"],
    "Rahul": [25, "Chennai", "SQL"],
    "Arun": [19, "Bangalore", "Python"],
    "Vijay": [28, "Coimbatore", "PySpark"],
    "Priya": [24, "Chennai", "Pandas"]
}
def create_employee_file():
    with open ("employees.txt","w") as file:
        for name,details in employees.items():
            file.write(f"{name},{details[0]},{details[1]},{details[2]}\n")

def search_by_skill():
    with open("employees.txt","r") as file:
        value = input("Enter the skill : ")
        Found = False
        with open("result.txt","w") as res_file:
            for i in file:
                name,age,city,skill = i.strip().split(",")
                if skill == value:
                    Found = True
                    res_file.write(f"{name},{age},{city},{skill}\n")
            return Found
create_employee_file()
result = search_by_skill()

if not result :
    print("Skill not found")

with open("result.txt","r") as res_file:
    print(res_file.read())







    #     if largest < int(age):
    #         largest = int(age)
    #         largest_name = name
    #         largest_age = age
    # print(f"Oldest employee : {largest_name}")
    # print(f"Age: {largest_age}")

 
                


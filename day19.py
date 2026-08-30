# student = {
#     "name": "Gouse",
#     "age": 22,
#     "city": "Coimbatore"
# }
# for key,value in student.items():
#     print(key,":",value) 

# student = {
#     "name": "Gouse",
#     "age": 22,
#     "city": "Coimbatore"
# }
# student.update({"department":"AIDS"})
# for key,value in student.items():
#     print(key,":",value)    

# student = {
#     "name": "Gouse",
#     "age": 22,
#     "city": "Coimbatore"
# }
# student.update({"age":"23"})
# for key,value in student.items():
#     print(key,":",value)    

# student = {
#     "name": "Gouse",
#     "age": 22,
#     "city": "Coimbatore"
# }
# student.pop("city")
# for key,value in student.items():
#     print(key,":",value)    

# student = {
#     "name": "Gouse",
#     "age": 22,
#     "city": "Coimbatore"
# }
# print("city" in student) 

# student = {
#     "name": "Gouse",
#     "age": 22,
#     "city": "Coimbatore",
#     "department": "AI&DS"
# }
# count  = 0
# for key,value in student.items():
#     count += 1
# print(count)

# marks = {
#     "Python": 85,
#     "SQL": 92,
#     "PySpark": 88,
#     "Excel": 95
# }
# smallest = marks.get("Excel")
# smallest_key = ''
# for key,value in marks.items():
#     if value < smallest:
#         smallest = value
#         smallest_key = key
# print(smallest_key)

# marks = {
#     "Python": 85,
#     "SQL": 92,
#     "PySpark": 88,
#     "Excel": 95
# }
# sum = 0 
# for value in marks.values():
#     sum += value
# print(sum)

marks = {
    "Python": 85,
    "SQL": 92,
    "PySpark": 88,
    "Excel": 95
}
count = 0
for value in marks.values():
    if value > 90:
        count += 1
print(count)
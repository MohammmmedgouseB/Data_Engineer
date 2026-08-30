# def find_largest(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(find_largest(10, 25))

# def find_largest(a,b):
#     if a < b:
#         return a
#     else:
#         return b
# print(find_largest(10, 25))

# numbers = [10, 20, 30, 40]

# def sum(numbers):
#     res = 0
#     for i in numbers :
#         res += i
#     return res
# print(sum(numbers))

# numbers = [10, 45, 20, 80, 35]
# def find_largest(numbers):
#     largest = 0
#     for i in numbers :
#         if largest < i:
#             largest = i
#     return largest
# print(find_largest(numbers))


# def count_char(a):
#     count = 0
#     for ch in a :
#         count +=  1
#     return count
# print(count_char("python"))
    

# def count_vowels(a):
#     count = 0
#     for ch in a:
#         if ch in "aeiou" :
#             count += 1
#     return count
# print(count_vowels("python"))

# def reverse(a):
#     res = ""
#     for ch in a[::-1]:
#         res += ch
#     return res
# print(reverse("python"))

def count_char(a,b):
    count = 0
    for ch in a:
        if ch == b:
            count += 1
    return count
print(count_char("banana","a"))
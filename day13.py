#count consonants
# word = input()
# count = 0
# for i in word:
#     if i not in 'aeiou':
#         count+=1
# print(count)

#palindrome
# word = input()
# res = word[::-1]
# if res == word:
#     print('palindrome')
# else:
#     print('not a palindrome')

#count words in sentence
# word = input()
# count = 0
# split = word.split(" ")
# for i in split:
#     count+=1
# print(count)

#Find the Longest Word in sentence
# input = input()
# word = input.split()
# length = 0
# for i in word:
#     if len(i)>length:
#         length = len(i)
#         res = i
# print(res)

# Remove Spaces
# sentence  = input()
# print(sentence.replace(" ",""))

# sentence  = input()
# sentence = sentence.strip()
# word = sentence.split(",")
# print("Name:",word[0])
# print("Age",word[1])
# print("Department",word[2])

numbers = [10, 20, 30, 40]

numbers[1] = 200
numbers[3] = 400

print(numbers)
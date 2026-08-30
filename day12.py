
# # split and keep first letters as cap
# data = "  gouse,22,ai&ds  "

# word = data.split(',')

# for i in word:
#     if i==word[0]:
#         print((word[0].title()).strip())
#     elif i==word[1]:
#         print(word[1])
#     else:
#         print((word[2].upper()).strip())    


# #Count a Character
# word = input()
# print(word.count('g'))

# Count Vowels
# word = input()
# res=0
# for i in word:
#     if i=='a' or i=='e' or i=='i' or i=='o'or i=='u':
#         res = res+word.count(i)
# print(res)


#reverse string
word = input()
for i in word[::-1]:
    print(i,end='')

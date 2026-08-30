# def count_words(a):
#     count = 0
#     words = a.split(" ")
#     for i in words:
#         count += 1
#     return count
# print(count_words("Python is used for Data Engineering"))

# def count_words(a):
#     words = a.replace(" ","")
#     return words
# print(count_words("Python Data Engineering"))

# def char_freq(a):
#     freq = {}
#     for ch in a:
#         if ch in freq :
#             freq[ch]+=1
#         else:
#             freq[ch] = 1
#     return freq
# print(char_freq("Banana"))

def non_repeating(a):
    word = {}
    for ch in a:
        if ch in word:
            word[ch]+=1
        else :
            word[ch] = 1
    res = ''
    for key,value in word.items():
        if value == 1:
            res = key
            return res
            
print(non_repeating("swiss"))


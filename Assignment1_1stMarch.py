# A = input("Enter the input")
# print(A.isnumeric())


# str1 = input("Enter")
# unique = set(str1)
# print("Unique words", unique)

# A = input("Enter a sentence")
# x = "#".join(A)
# print(x)
#
# vowels = 'aeiouAEIOU'
# Str2 = input("Enter a sentence")
# count = {}.fromkeys(vowels,0)
#
# for char in Str2:
#     if char in count:
#         count[char] +1
# print(count)

str3 = input("Enter a string")
print(*[i for i in str3.split() if len(i) == max([len(k) for k in str3.split()])])
print(*[i for i in str3.split() if len(i) == min([len(k) for k in str3.split()])])
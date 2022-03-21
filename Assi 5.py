# print("Enter the Name of Source File: ")
# sFile = input()
# print("Enter the Name of Target File: ")
# tFile = input()
#
# fileHandle = open(sFile, "r")
# texts = fileHandle.readlines()
# fileHandle.close()
#
# fileHandle = open(tFile, "w")
# for s in texts:
#     fileHandle.write(s)
# fileHandle.close()
#
# print("\nFile Copied Successfully!")
#Hello Everyone How are you
# def frequency(input):
#     freq = {}
#     for word in input.split():
#         freq[word] = freq.get(word, 0) + 1
#     words = list(freq.keys())
#     words.sort()
#     for w in words:
#         print(f'{w}:{freq[w]}')
# str = input('enter string: ')
# frequency(str)

# string1 = input('Enter the String :')
# count = 0
# for i in string1:
#     count += 1
# print(count)

# string = input().lower()
# if string == string[::-1]:
#   print("It's a palindrome")
# else:
#   print("It's not a palindrome")

# numbers = [1, 3, 4, 6, 7]
# print(numbers)
# print("Square of every number of the given  list:")
# square_no = list(map(lambda x: x ** 2, numbers))
# print(square_no)
# print("Cube of every number of the given list:")
# cube_no = list(map(lambda x: x ** 3, numbers))
# print(cube_no)

print("Enter a string")
string = input().lower()
if string == string[::-1]:
  print("It's a palindrome")
else:
  print("It's not a palindrome")





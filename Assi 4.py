# i = 0
# x = 0;
# while i <= 100:
#     x = x + i;
#     i += 1
# print(x)


# def name_adder(list):
#     i = 0
#     new_list = []
#     while i < len(list):
#         if list[i] != "":
#             new_list.append(list[i])
#         i = i+1
#     return new_list
#
# lst1=["Orange", "Blue","","Green", "Red", "Pink"]
# i=0
# print(name_adder(lst1))


# lst1=["Phil", "Oz", "Seuss", "Dre"]
# lst2=[]
# for i in lst1:
#     lst2.append("Dr. " + i)
# print(lst2)
#
#
# lst1=[3.14, 66, "Teddy Bear", True, [], {}]
# lst2=[]
# for i in lst1:
#     lst2.append(type(i))
# print(lst2)

#
num = int(input("enter no."))

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")
#
#
# a = int(input("Number of classes held:"))
# b = int(input("Number of classes attended:"))
#
# per = b/a*100
#
# if per >= 75:
#     print("The student is allowed to sit in exam")
# else:
#     print("The student is not allowed to sit in exam")



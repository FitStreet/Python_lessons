# a = 'b'
# if a in "sadsafrga": # все что после If переводится в bool type(true or false)
#     print("yes")

# str = "hello world i am alive"
# counter = 0
# for i in str:
#     if i in 'auioye':
#         counter += 1
# print(counter)
 
# list_ = [1, 2, 3, 4, 5, 7, 9]
# for i in list_:
#     print(i)

lst = ['hello', 1, 2, 3, 6, 8, 'fgh', False, None]
lst_1 = []
for i in lst:
    if type(i) == int:
        lst_1.append(i)
print(lst_1)        
# for i in range(1,11) :
#     print(i)
#     if i == 5 :
#         break

# list_coll = [1,2,3,4,'hello',6,7,8,9,10]
# i = 0
# while i < len(list_coll) :
#     if type(list_coll[0]) != type(list_coll[i]) :
#         print('it is hetrogenous list collection')
#         break
#     i += 1
# else:
#     print('it is homogenous list collection')

# "ABCD"
# it contains only upper case characters
# "AbcD"
# it not contains only upper case characters

# string = input("enter the string : ")
# for char in string:
#     if not ('A'<= char <= 'Z'):
#         print('it not contains only upper case characters')
#         break
# else:
#     print('it contains only upper case characters')

#wap to check whether the number is prime or not
# num = int(input('enter the number : '))
# for i in range(2,num):
#     if num%i == 0:
#         print('it is not a prime number')
#         break
# else:
#     if num > 1:
#         print('it is a prime number')
#     else:
#         print('it is not a prime number')

# pwd = input('Enter the password : ')
# while True:
#     if 'alex@8055' == pwd:
#         print('logged in')
#         break
#     print('incorrect password')
#     pwd = input('Please enter the password again : ')

# list_coll = eval(input('enter the list collection : '))
# #output [True,3+4j,'hello'[1,2],(10,20)]
# out = []
# for item in list_coll:
#     if type(item) == int:
#         continue
#     out.append(item)
# print(out)

# for i in range(1,31):
#     if i in (10,15,25):
#         continue
#     print(i)

# n  = 2
# if n % 2 == 0:
#     pass
# else:
#     print('hai')
# for  i in range(1,4):
#       print('i = ',i)
#       for j in range(1,4):
#           print('j = ',j)

#input  ['hello','hai','bye','good']
#output ['eo','ai','e','oo']
# words_coll = ['hello', 'hai', 'bye', 'good']
# out = []
# vowel = ''
# for word in words_coll:
#     for char in word:
#         if char in 'aeiouAEIOU':
#             vowel += char
#     out.append(vowel)
#     vowel = ''
# print(out)


#input [12,'python',True,34,'hello']
#output {'python':1,'hello':2}

# list_coll = [12,'python',True,34,'hello']
# out = {}
# for item in list_coll:
#     count = 0
#     if type(item) == str:
#         for char in item:
#             if char in 'aeiouAEIOU':
#                 count += 1
#         out[item] = count
# print(out)

#input [12,'python',True,34,'hello']
#output { 12:3, 34:7 }
list_coll = [12, 'python', True, 34, 'hello']
out = {}
for item in list_coll:
    sum = 0
    if type(item) == int:
        for digit in str(item):
            sum += int(digit)
        out[item] = sum
print(out)

#input [12,'python',True,34,'hello']
#output [12,'nohtyp',True,34,'olleh']
#without using slicing
list_coll = [12, 'python', True, 34, 'hello']
out = []
for item in list_coll:
    if type(item) == str:
        rev = ''
        for char in item:
            rev = char + rev
        out.append(rev)
    else:
        out.append(item)
print(out)

#print prime numbers from the range 1 to 100
# for num in range(1,101):
#     for i in range(2,num):
#         if num%i == 0:
#             break
#     else:
#         if num > 1:
#             print(num)

# for num in range(1,101):
#     sum = 0
#     for i in range(1,num):
#         if num%i == 0:
#             sum += i
#     if sum == num:
#         print(num)

# employee = {}
# n = int(input('enter the number : '))
# for i in range(n):
#     employee_name = input('Enter the employee name : ')
#     first_name = input('Enter the first name : ')
#     last_name = input('Enter the last name : ')
#     job_name = input('Enter the job name : ')
#     sal = int(input('Enter the salary : '))
#     employee.update({employee_name: {'first_name': first_name, 'last_name': last_name,'job_name': job_name,'salary':sal}})
#     print('1 employee details updated')
# print(employee)


#input 'www.facebook.com  www.twitter.com www.google.com www.linkedin.com www.instagram.com www.pyspiders.com'
#output  [facebook, twitter, google,linkedin, instagram, pyspiders]
string = 'www.facebook.com  www.twitter.com www.google.com www.linkedin.com www.instagram.com www.pyspiders.com'
out = []
url_coll = string.split()
for url in url_coll:
    n = url.split('.')
    out.append(n[1])
    #out += n[1]
print(out)


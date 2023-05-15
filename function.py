def greeting():
    print('Hello, good morning')


def number():
    for i in range(1,101):
        print(i)

def add():
    num1 = int(input('enter the number : '));num2 = int(input('enter the number : '));print('the sum of two number is : ',num1 + num2)

def add():
    num1 = int(input('enter the number : '))
    return
    num2 = int(input('enter the number : '))
    return num1 + num2

def u_upper():
    string = input('enter the string : ')
    res = ''
    for char in string:
        if 'a'<=char<='z':
            res += chr(ord(char)-32)
        else:
            res += char
    return res

def add(n1,n2,n3,n4):
    print('n1:',n1)
    print('n2:',n2)
    print('n3:', n3)
    print('n4:', n4)


#add(n4= 40,n2=20,n3=30,n1=10)

def u_append(list_coll,val):
    res=list_coll+[val]
    print(res)

# u_append([1,2,3,4,5],6)

# u_append(['apple','mango','banana'],val='grapes')

def u_remove(list_coll,val):
    out = []
    for item in list_coll:
        if item == 
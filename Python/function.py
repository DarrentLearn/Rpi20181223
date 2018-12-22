def fun():
    print('fun')
    pass;
fun()

def fun2():
    return False
if fun2():
    print ('True')
else:
    print('False')
    
def fun3(param):
    print(param)
fun3('This is fun3')

obj= None
if obj is None:
    print("It's some thing")
else:
    print("No thing")

def fun4(item1,item2,item3):
    return{'a':item1,'B':item2,'C':item3}
print(fun4('aa','bb','cc'))
print('chang param location')
print(fun4(item2='bbb',item3='ccc',item1='aaa'))

def fun5 (p1,p2,p3='param3'):
    'This is the function document'
    return{'p1=':p1,'p2=':p2,'p3':p3}
print(fun5('param1','param2'))
print(fun5('param1a','param2a','param3a'))

print(fun5.__doc__)

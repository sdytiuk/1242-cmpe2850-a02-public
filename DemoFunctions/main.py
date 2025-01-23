def foo(left, right):
    pass

def food(left, right, other = 7):
    pass

def fook(left,right): #this returns a tuple
    return left, right, (left+right)/2

def goo(*args):
    print(args)
    for i in (x for x in args if x % 2 == 0):
        print(i)

def hoo(**kwargs):
    print(kwargs)

def joo(left,right,*args):
    print(left,right,args)

def koo(left :'int',right:'int',*args : 'tuple',**kwargs: 'dict'):
    """

    :param left:
    :param right:
    :param args:
    :param kwargs:
    :return:
    """
    print(left,right,args,kwargs)

def EasyGenerator(*args):
    for i in args:
        yield i

def JacobsGenerator():
    yield 1 #finite generator!!

def ColesGenerator():
    while True:
        yield 1

print(ColesGenerator()) #don't unpack Cole's Generator!!
print("is 5 a string or an int? ", isinstance("5",(str,int)))
arg = ("5",(str,int))
print("Tuple Unpacked",isinstance(*arg))
print(*EasyGenerator(1,2,3,4,5)) #you can unpack a generator!!
koo("Coup d'etat",2,num=1,num2=2)
joo(1,2,3,4,5,6)

print(fook(5,6))

l,r,avg = fook(7,8) #unpacking into discretes

print(avg)

goo(1,2,3,4,5,1,2,3,4,5)

p=[1,2,3,4]
goo(*p)

print("unpack?",*p)

hoo(Day='Monday',hrs=7,Donuts=4)
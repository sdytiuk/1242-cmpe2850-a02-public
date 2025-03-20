#Classes

class Dud :
    pass

dud = Dud()

print(dud)

class AlsoDud:
    pass

class PocoUtil:
    secret = 55

    @classmethod
    def ChangeSecret(cls, num):
        cls.secret = num

class Nums (Dud, AlsoDud, PocoUtil) :
    num = 3 #STATIC
    numbers = [1,2,3,4]
    x,y,z = 0,0,0

    @classmethod
    def ChangeSecret(cls, num):
        super().ChangeSecret(num)

    #constructor time!!
    def __init__(self):
        self.fantasma = "I dunno"
        #NOTE: Nums.fantasma does not exist just because it's in the instance ctor

    #no CTOR OVERLOAD!
    '''def __init__(self, a, b, c):
        self.num = a
        self.numbers[0] = b
        self.x = c'''

    #TOSTRING equivalent
    def __str__(self):
        return (f"Instance?: {self.fantasma} {self.num}, {self.numbers}, {self.x}, {self.y}, {self.z}\n"
                f"Class: {Nums.num}, {Nums.numbers}, {Nums.x}, {Nums.y}, {Nums.z}")

    # THREE TYPES OF METHODS
    # INSTANCE
    def HaveISeenAGhost(self):
        if self.fantasma == 'yes':
            return True
        return False

    #INSTANCE (note first arg is usually self...)
    def IsMyNumBigger(yo, what:int) -> bool:
        '''

        :param what:
        :return:
        '''
        return yo.num > what

    #CLASS
    @classmethod
    def jacob (cls, name):
        #you cannnot access self!!! (instance vars)
        cls.num += 8888

    #STATIC
    @staticmethod
    def hudson(number):
        z = number #this means nothing happens... has NO access to anything useful
        #maybe print stuff out
        print("Hudson's favourite number is: ", number)

    #override equals! ==
    def __eq__(self, other):
        print(self, " : ", other)
        return self.num == other.num

    #lessthan <
    def __lt__(self, other):
        return self.num < other.num



num_a = Nums()
num_b = Nums()
num_a.jacob("Tane")
Nums.jacob("no importa")
num_a.hudson(-1000)
Nums.num += 1
num_a.num += 5
print(num_a.num)
print(num_b.num)
print(Nums.num)
num_a.room = 55
print(num_a.room)

Nums.numbers[2] += 10
Nums.x += 3

print(Nums.numbers[2])

num_a.numbers[2] = 99

print(num_a.numbers)

arr = [1,2,3,4]
arr2 = arr #this is the same as creating an instance one that points to the class!
arr2[2] = 77
print(arr)
num_a.fantasma = "yes"
print("Finally... the class print outs")
print(num_a)
print(num_b)

print(num_b.HaveISeenAGhost())

print(num_a.IsMyNumBigger(2))

num_a.num = 7
num_b.num = 5

print(num_a == num_b)
print (num_a < num_b)
print(num_a > num_b)

print("POCO UTIL TIME")
print(num_a.secret)
num_a.ChangeSecret(22)
#num_a.super().ChangeSecret(22) weird and doesn't work
print(num_a.secret)


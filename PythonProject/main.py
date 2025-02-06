import sys #for command line usage

def SayHello():
    """
    >>> SayHello()
    'Hello'

    :return:
    """
    return "Hello"

if __name__ == '__main__':
    print(len(sys.argv))
    print(sys.argv)
    if len(sys.argv) < 2:
        print("I need more arguments!")
    else:
        print("Arg1=",sys.argv[0],"Arg2=",sys.argv[1])
    print(SayHello())
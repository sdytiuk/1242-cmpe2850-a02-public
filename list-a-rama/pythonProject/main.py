

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    debug = True
    numbers = [1,2,3,4,5]
    #get the squares of the numbers
    squares = [x**2 for x in numbers if x % 2 != 0]
    #enumerate returns index, value
    #unpacking the tuple
    squares_of_odd_indices=[x**2 for i,x in enumerate(numbers) if i % 2 != 0]
    #not unpack the tuple up front
    colesnotes = [t[1] ** 2 for t in enumerate(numbers) if t[0] % 2 != 0]
    print(squares)
    print('odd indices', squares_of_odd_indices)
    print('cole', colesnotes)

    numbers = list(range(1,11))
    if debug:
        print('numbers:', numbers, type(numbers))
    print( [num for num in numbers if num%3 ==0])

    #matrix transpose
    matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    transposed = [[row[i] for row in matrix]
                  for i in range(len(matrix[0]))]
    print('transposed: ',transposed)

    #character uppercasing
    word="hello"
    upperList = [c.upper() for c in word]
    print(word,word.upper(),upperList
          ,str(upperList),"".join(upperList))

    #conditional expression
    cond_nums = [1,-2,3,-4,5]

    nums_from_comp = [num if num%2 ==1 else -1*num
                      for num in range(1,6)]
    print(cond_nums, nums_from_comp)
    #now we only want positive numbers
    #RESTRICT/FILTER
    print([x for x in nums_from_comp if x > 0])
    #we want all numbers but any less than 0 show as 0
    #TRANSFORM
    print([0 if x < 0 else x for x in nums_from_comp])

    #flattening a list of lists
    nested_list = [[1,2],[3,4],[5,6]]
    print(nested_list)
    #make into a 1D list
    print([item for sublist in nested_list for item in sublist])

    #create a dictionary from two lists
    keys = ['a','b','c','a']
    values = [1,2,3,4]

    my_dict = {keys[i]: values[i] for i in range(len(keys))}
    print(my_dict)

    #cartesian product
    list1 = [1,2]
    list2 = ['a','b']

    cartesian_product = [(x,y) for x in list1 for y in list2]
    print(cartesian_product)

    #generating a list of file names
    #that end in a certain extension!!
    import os
    file_names = [f for f in os.listdir(".") if f.endswith('.py')]
    print(file_names)

    #creating a set of unique elements
    numbers = [1,2,2,3,3,3,4,4,4,4]
    unique = list(set(x for x in numbers))
    print(unique)
    print(list(set(numbers)))

    #shallow vs deep copy
    original_list = [1,2,[3,4,[5,6]]]

    #copy by assignment
    copy1 = original_list

    copy1[0] = 97
    copy1[2][0] = 99
    print(original_list)

    copy2 = original_list.copy()
    copy2[0] = 101
    copy2[2][0] = 102

    print(original_list)

    #deepcopy!!
    import copy
    copy3 = copy.deepcopy(original_list)
    #starting [97, 2, [102, 4, [5, 6]]]
    copy3[0] = 201
    copy3[2][0] = 202
    copy3[2][2][0] = 555
    print(original_list)


    #sort vs sorted
    my_list = [3,1,4,1,5,9,2]

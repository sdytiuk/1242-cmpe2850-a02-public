#sort vs sorted
# sort modifies the list in-place
# can only be used for lists
# better efficiency and memory usage

#sorted creates a new sorted list
#works with any iterable
#general and flexible sorting approach

my_list = [3,1,4,1,5,9,2]
my_list.sort()
print(my_list)
my_list2 = [3,1,4,1,5,9,2]
new_list = sorted(my_list2)
print(my_list2, new_list)

words = ["apple", "banana", "cherry", "avocado"]
sorted_words = sorted(words)
print(sorted_words)

points = [(2,5),(1,8),(4,3),(1,4),(1,9)]
sorted_points = sorted(points)
print(sorted_points)

#sort a list of objects
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " " + str(self.age)

people = [Person("Alice",30), Person("Bob",25),
          Person("Charlie",35)]

def sort_by_age(person):
    return person.age

#sorted_people = sorted(people, key=sort_by_age)
sorted_people = sorted(people, key=lambda x : x.name, reverse=True )

print([str(x) for x in people])
print([str(x) for x in sorted_people])

my_dict = {'zucchini':5, 'apple':3, 'banana':1, 'cherry':2}
sorted_dict = sorted(my_dict.items())
print(my_dict)
print(dict(sorted_dict))

sort_by_number = sorted(my_dict.items(), key=lambda x: x[1])
print("What is .items?",my_dict.items())
print(sort_by_number)

data = [(1,'a',10), (2, 'B', 5), (3, 'C', 15), (4, 'a', 8),
        (5, 'B', 12), (2, 'Z', 12)]
sorted_data = sorted(data, key=lambda x:(-x[2],x[0]))
print(sorted_data)

#more lambda
add = lambda x, y : x+y

print(add(5,4))

to_upper = lambda text: text.upper()
print(to_upper("Hello World!"))

numbers = [1,2,3,4,5,6,7,8,9]
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

#map executes a specified function for each item in an iterable
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#can we use a list comp to accompish both the above at the same time?
print( [x**2 for x in numbers if x%2 == 0])

people2 = [Person("Alice",30), Person("Bob",25),
          Person("Charlie",35)]

people2.sort(key=lambda x:x.age)
print([str(x) for x in people2])

#how to convert a list to a dictionary?
#each item in the list will have a dictionary value of the number of
#occurrences in the list

#1
my_list = [1,2,2,2,3,4,4,5,5,5,5,5,5]
count_dict = {}
for item in my_list:
    if item in count_dict.keys():
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)

#2 a bit more elegant
count_dict = {}
for item in my_list:
    #.get returns the item OR 0 if item doesn't exist yet
    count_dict[item] = count_dict.get(item,0) + 1

print(count_dict)

#3 COMPREHENSION
count_dict_comp = {item: my_list.count(item) for item in set(my_list)}
print(count_dict_comp)
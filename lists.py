
#list in python

my_list= []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)

another_list = [50, 60, 70]


my_list.extend(another_list)

my_list.sort()

print(my_list)

print("index of the value 30 is " + str(my_list.index(30)))
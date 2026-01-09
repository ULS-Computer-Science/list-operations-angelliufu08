#Task 1 .apend()

fruits = ['apple', 'orange', 'strawberry']
print(len(fruits))
print('What is your favorite fruit?')
newFruit = input()
fruits.append(newFruit)
print(len(fruits))


#Task 2 .insert()

animals = ['cat', 'dog', 'cow', 'bat']
animals.insert(1,'tiger')
print(animals)


#task 3 concatenation and replication

row = ['_'] * 3
addOn = ['X', 'O']
finalRow = row + addOn
print(finalRow)


#task 4 .extend() method

backpack = ['book', 'pen']
foundItems = ['apple', 'map']
print(backpack)
print(foundItems)
backpack.extend(foundItems)
print(backpack)


#task 5 .remove() method

task5 = [1,3,6,4,7,9,4,4,5]
print(task5.count(4))
task5.remove(4)
print(task5.count(4))


#task 6 .pop() method

vip = 'ava caden emmett thea ellie liam cade zlata harvey'.split()
kickedOut = vip.pop(5)
print(f'We removed {kickedOut} from the party.')
print(vip)


#Task 7 del statement

numbers = [1,2,3,4,5,6,7,8,9,10]
print (numbers)
del numbers[3:6]
print (numbers)


#task 8 .index() method

colors = ['red', 'blue', 'green', 'yellow', 'pink', 'cyan', 'brown', 'white', 'teal', 'orange']
print('Pick a color.')
colorPicked = input().lower()
if colorPicked in colors:
    print('Danger! That item is in the list! It\'s index is:')
    print(colors.index(colorPicked))
else:
    print('Safe! That item is not in the list!')


#task 9 ordering (.sort() and .reverse())

task9 = [3, 7, 34, 26, 0]
task9.sort()
print(task9)
task9.reverse()
print(task9)


#task 10 .copy() method

original = [1,2,3]
backup = original.copy()
original.clear()
print(backup)


#task 11 random selection (random.choice)
import random
magic8ball = ['yes', 'no', 'maybe', 'try again later', 'definitely', 'of course not']
for i in range(3):
    print(random.choice(magic8ball)) 


#task 12 nested lists
task12 = [[8,9],[7,0]]
print(task12[1][0])
#Exercise4 : To print the items of list which are collection of numbers and greater than equal to 6

Mylist= ["Harry", "Larry", "Carry", "Harpic", "Vim Bar", 2, 5, 6, 7, 10, 1, 15]
for item in Mylist:
    if str(item).isnumeric() and item>=6:
        print(item)

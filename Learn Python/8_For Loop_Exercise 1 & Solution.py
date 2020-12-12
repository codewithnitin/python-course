#Exercise3 : To print the items of list which are collection of alphabets and ends with rry


Mylist= ["Harry", "Larry", "Carry", "Harpic", "Vim Bar", 2, 5, 7, 10]
for item in Mylist:
    if str(item).isalpha() and item.endswith("rry"):
        print(item)

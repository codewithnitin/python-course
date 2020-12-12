"""

Write a program to fetch the data set of iris.data from website UCI ML Repository and then write
it into a text file then need to parse the content of a file in a list of list form where first
element of list would be the first line of text file and so on then pickle that list of list and
write a code to unpickle that list as well ?

"""


import requests
import pickle


r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# print(r.text)

# with open("UCI_ML_Repository_Dataset.txt", "w") as f:
#     f.write(r.text)

# with open("UCI_ML_Repository_Dataset.txt", "r") as f:
#     Dataset =f.read()

# print(Dataset)

# Dataset_list = Dataset.splitlines()
# print(Dataset_list)

# with open("UCI_ML_Repository_Dataset.pkl", "wb") as f:
#     pickle.dump(Dataset_list, f)

with open("UCI_ML_Repository_Dataset.pkl", "rb") as f:
    Required_iris_dataset_list = pickle.load(f)

print(Required_iris_dataset_list)


"""

In above approach, we imported two modules requests and pickle then we visit to the website
UCI Machine Learning Repository into its dataset section where we click on iris dataset in
popular dataset list then click on data folder where we will get options like iris.data &
iris.names so we need to click on iris.data or we can right click on iris.data to copy the
url of this dataset.

After that we got a response of this url like :

r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
so if we print print(r.text) so will get an output of dataset in console but we have to save
it into a text file so created a file UCI_ML_Repository_Dataset.txt in write mode and wrote
all the content of r.text into this file like this :

with open("UCI_ML_Repository_Dataset.txt", "w") as f:
    f.write(r.text)
    
Again reopened the same file in a read mode to get the content of a file like this :

with open("UCI_ML_Repository_Dataset.txt", "r") as f:
    Dataset =f.read()

print(Dataset)

so, here we read the content of a file and save it into a variable Dataset and then applied
a function splitlines() on Dataset to get the output in a list where first element would be
the first line of content in Dataset variable like this :

Dataset_list = Dataset.splitlines()
print(Dataset_list)

Now opened a new file UCI_ML_Repository_Dataset.pkl in write binary mode and dump this
Dataset_list into this file like this :

with open("UCI_ML_Repository_Dataset.pkl", "wb") as f:
    pickle.dump(Dataset_list, f)
    
Reopened the same file in read in binary mode this time like this :

with open("UCI_ML_Repository_Dataset.pkl", "rb") as f:
    Required_iris_dataset_list = pickle.load(f)

print(Required_iris_dataset_list)

Here, pickle.load(f) will have content of file UCI_ML_Repository_Dataset.pkl in binary mode
as pickle.load() or pickle.loads() accepts the binary code ( bytes stream ) and convert it
into the python object which was list ( Dataset_list ) which is stored into the new variable
Required_iris_dataset_list so if we print print(Required_iris_dataset_list) so we will get
the same output as in list which we had in Dataset_list so pickling or unpickling is done.





Note : When we were reading the file UCI_ML_Repository_Dataset.txt like this :

with open("UCI_ML_Repository_Dataset.txt", "r") as f:
    Dataset =f.read()
    
we could apply f.readlines() function here which gives the content of a file in a list of list
where first element would be the content of first line of the above file along with \n character
in each element which was not our required output so we used f.read() to read the full content
of a file and stored it into a variable Dataset and then applied splitness() on this variable
which gives a list of list where first element would be the first line of the content which is
stored in this variable Dataset except \n character and this is what we were looking for.





"""








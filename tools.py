import random

# generates random data to sort
def generateRandomArray():
	data = []

	for i in range(1,101):
		data.append(random.randint(1,100))

	random.shuffle(data)

	return data

# loads data from file
def readData(fileName):
	with open(fileName, "r") as f:
			data = f.readlines()

	data = [int(i.strip()) for i in data]

	return data

# saves sorted data
def saveSorted(data):
	with open("sorted.txt", "w") as f:
		for item in data:
			f.write(str(item) + "\n")
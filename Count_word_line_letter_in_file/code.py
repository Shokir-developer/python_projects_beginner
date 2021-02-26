from string import punctuation

lines = 0
words = 0
letters = 0


with open("salom.txt") as f:
	listx = f.readlines()
lines = len(listx)


newList = []
for i in range(lines):
	newList.append(listx[i].split())

newList2 = []
for item in newList:
	for char in item:
		newList2.append(char)


string = ""
for x in newList2:
	for charx in x:
		if charx in punctuation:
			continue
		else:
			string += charx


print("letters: ", len(string))
print("word: ", len(newList2))
print("lines: ", lines)


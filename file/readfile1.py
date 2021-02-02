# W A P to read data from a file
f=open("sample.txt")
data=f.read()
print(data)
f.close()
print("numbers of characters in file= " ,len(data))
lines =data.split("\n")
print("numbers of lines in a file=" , len(lines))
words=0
for x in lines:
    words+=len(x.split("-"))
    print("numbers of word in file", words)
 

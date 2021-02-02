f=open("sample.txt",'r')
num_line=0
for line in f:
    num_line += 1
    print("number of lines:",num_line)
    

f.close()


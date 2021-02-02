import numpy as np 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
  
print("Enter the entries in a single line (separated by space): ") 
arrlist= list(map(int, input().split())) 

matrix = np.array(arrlist).reshape(R, C) 
print(matrix)
print("----------------------------------------")
print(matrix[0][0],[1][0],[2][0])

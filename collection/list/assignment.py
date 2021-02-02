e_marks=[
    [[52,53,62,58,96,65],[32,68,67,95,85,82]],
    [[23,58,94,74,52],[45,52,84,89]],
    [[51,85,94,56,63],[45,67,23,21]],
    [[56,88,78,94,66],[65,97,13,61]]
    ]

sum=0
for marks1 in e_marks:
    for marks2 in  marks1:
        for marks3 in marks2:
            sum=sum+marks3
print("Total marks of All Semester:",sum)
print("---------------------------------------")

mark=0
for first in e_marks[0][0]:
    mark=mark+first
for first in e_marks[0][1]:
    mark=mark+first
print("1st year mark:",mark)

print("---------------------------------------")
mark=0
for second in e_marks[1][0]:
    mark=mark+second
for second in e_marks[1][1]:
    mark=mark+ second
print("2nd year mark:",mark)

print("---------------------------------------")
mark=0
for third in e_marks[2][0]:
    mark= mark + third
for third in e_marks[2][1]:
    mark= mark + third
print("3rd year mark:", mark)

print("---------------------------------------")
mark=0
for fourth in e_marks[3][0]:
    mark= mark + fourth
for fourth in e_marks[3][1]:
    mark= mark + fourth
print("4th year mark:", mark)
print("---------------------------------------")

print("****************************************************")

s1=0
for sem1 in e_marks[0][0]:
    s1=s1+sem1
print("1st semester:",s1)

print("****************************************************")
s1=0
for sem2 in e_marks[0][1]:
    s1=s1+sem2
print("2nd semester:",s1)
print("****************************************************")
s1=0
for sem3 in e_marks[1][0]:
    s1=s1+sem3
print("3rd semester:",s1)
print("****************************************************")
s1=0
for sem4 in e_marks[1][1]:
    s1=s1+sem4
print("4th semester:",s1)
print("****************************************************")
s1=0
for sem5 in e_marks[2][0]:
    s1=s1+sem5
print("5th semester:",s1)
print("****************************************************")
s1=0
for sem6 in e_marks[2][1]:
    s1=s1+sem6
print("6th semester:",s1)
print("****************************************************")
s1=0
for sem7 in e_marks[3][0]:
    s1=s1+sem7
print("7th semester:",s1)
print("****************************************************")
s1=0
for sem8 in e_marks[3][1]:
    s1=s1+sem8
print("8th semester:",s1)


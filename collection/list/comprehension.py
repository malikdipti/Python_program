ur_friend=["Raj","Krishna","Dipti","Jack"]
my_friend=["Raj","Krishna","lucy","Gibbon"]
common_friend=[]

for friend in ur_friend:
    if friend in my_friend:
        common_friend.append(friend)
print(common_friend)

print("---------------------------------------")

common_friend=[friend for friend in ur_friend if friend in my_friend]
print(common_friend)
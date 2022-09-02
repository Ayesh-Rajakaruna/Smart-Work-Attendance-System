import os
localpath=".\\static\\photo_of_new_employer"
lis = localpath.split('\\')[1:]
print(lis)
if not ".\\{}".format(lis[0]) in [x[0] for x in os.walk(".")]:
    print("no")
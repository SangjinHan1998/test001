import os
print(os.getcwd())  # identify present path 
print(os.listdir()) # 1. Organize existent file and directory list 2. return 
print(os.listdir('C:/Users/'))  # print 

files = os.listdir('C:/Users/')
print(len(files))
print(type(files))

for x in os.listdir('C:/Users/sangj/Downloads'):
    if x.endswith('png'):
        print(x)
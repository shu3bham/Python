import os

path=r"C:\Users\shubham.deshmukh\Downloads\New folder"

dir_list = os.listdir(path) 
print("List of directories and files before creation:")
print(dir_list)
print()
file = 'myfile.csv'
with open(os.path.join(path, file), 'w') as fp:
    pass
    # To write data to new file uncomment
    # this fp.write("New file created")
  
# After creating 



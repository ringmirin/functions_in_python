# # Write a Python program to write a list to a file.

color=["red","blue","white"]
fname=open("list.txt","w")
for element in color:
   fname.write(element+"\n")
fname.close()

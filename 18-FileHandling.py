#Syntax :::
# To open a file :
    # fileObject = Open(<file-name>,<access-mode>,<buffering>)
# To read content
    # fileObject.read()
# To close a file
    # fileObject.close()


fileObject = open("C:\Data\github\python-basics\item.txt", "a")

# appending the content to the file
fileObject.write('EmpName   Department     Salary')
fileObject.close()
#fileObject.write('\n A    B       1000234')
#fileObject.write('\n Bernhard  Telenor        4530234')
fileObject = open("C:\Data\github\python-basics\item.txt", "")

fileText  = fileObject.read()
print(fileText)

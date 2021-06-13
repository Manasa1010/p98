def swapFileData():
    file1=input("Enter a file name")
    file2=input("Enter second file name")
    with open(file1,'r') as a:
        data_a=a.read()
    with open(file2,'r') as b:
        data_b=b.read()
    with open(file1,'w') as c:
        a.write(data_b)
    with open(file2,'w') as d:
        b.write(data_a)
 
swapFileData()       
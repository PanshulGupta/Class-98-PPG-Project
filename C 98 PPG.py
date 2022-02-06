def swapData():
    
    file1 = input("enter the file name: ")
    file2 = input("enter the file name: ")

    with open(file1, 'r')as a:
        data_a = a.read()

    with open(file2, 'r')as b:
        data_b = b.read()

    with open(file1, 'w') as b:
        c.write(data_b)


    with open(file2, 'w') as a:
        d.write(data_a)
        
swapData()

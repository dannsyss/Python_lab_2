def rf():
    file1 = open("test.txt", "r")
    lines = file1.readlines()
    list=[]
    for line in lines:
        list.append(line[:-1:].split(';'))
    file1.close
    return list
"""
problem statement :
       1) how many types os modes there and example
       2) write a program using class  read, rite and  append a  file
       3) how to optiize reading file
       4) read  2gb file from ram  of  1gb
       5) hoe many method function files
       6) what is  r+


"""

class files:
    def my_function():
        f = open("testing.txt", "r")
        print(f.read())  # reading complete file
        f.close()
    def my_fun():
        f = open("testing.txt", "r")
        print(f.read(5))  # read (5) it read onl 5 charecters of the file
        f.close()

    def my_fun1():
        f = open("testing.txt", "r")
        print(f.readline())     # it reads fist line of the file
        f.close()

    def my_fun2():
        f = open("testing.txt", "a")  # a is append it is used to add the text to exsisted file
        f.write("\n Now the file has one more line!")
        f.close()
        e = open("testing.txt", "r")
        print(e.read())
        e.close()

    def my_fun3():
        f = open("testfile.txt", "w")  # writes info in a  new file , if it is  already exsisred file it over writes file
        f.write("Woops! I have deleted the content!")
        f.close()
        e = open("testfile.txt", "r")
        print(e.read())
        e.close()

    def my_fun4():
        f = open("testfile.txt","r+")  # r+ used to read as wellas write file

        print(f.read())  # file is reading
        f.write("Woopsdddddddddd! I have deleted the content!") # writing  file
        f.close()

    def my_fun5():
        f = open("testfile.txt", "w+")  # w+ used to read as wellas write file
        print(f.read()) # file is reading
        f.write("Woopsd vinay! I have deleted the content!")  # writing  file

        f.close()

    def my_fun6():
        f = open("testfile.txt", "r+b")  # w+ used to read as wellas write file
        print(f.read())  # file is reading
        #f.write("Woopsd vinay! I have deleted the content!")  # writing  file

        f.close()


files.my_function()
files.my_fun()
files.my_fun1()
files.my_fun2()
files.my_fun3()
files.my_fun4()
files.my_fun5()
files.my_fun6()
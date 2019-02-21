"""
problem statement :
       1) how many types of modes there and example
       2) write a program using class  read, write and  append a  file
       3) how to optiize reading file
       4) read  2gb file from ram  of  1gb
       5) 2 modes function files
       6) what is  r+


"""

class files:



    def __init__(self,  file ):
        self.file=file

    def my_function(self):
        f = open(self.file, "r")
        print(f.read())  # reading complete file
        f.close()
    def my_fun(self):
        f = open(self.file, "r")
        print(f.read(5))  # read (5) it read onl 5 charecters of the file
        f.close()

    def my_fun1(self):
        f = open(self.file, "r")
        print(f.readline())     # it reads fist line of the file
        f.close()

    def my_fun2(self):
        f = open(self.file, "a")  # a is append it is used to add the text to exsisted file
        f.write("\n Now the file has one more line!")
        f.close()
        e = open(self.file, "r")
        print(e.read())
        e.close()

    def my_fun3(self):
        f = open(self.file, "w")  # writes info in a  new file , if it is  already exsisred file it over writes file
        f.write("Woops! I have deleted the content!")
        f.close()
        e = open(self.file, "r")
        print(e.read())
        e.close()

    def my_fun4(self):
        f = open(self.file,"r+")  # r+ used to read as wellas write file

        print(f.read())  # file is reading
        f.write("Woopsdddddddddd! I have deleted the content!") # writing  file
        f.close()

    def my_fun5(self):
        f = open(self.file, "w+")  # w+ used to read as wellas write file
        print(f.read()) # file is reading
        f.write("Woopsd vinay! I have deleted the content!")  # writing  file

        f.close()

    def my_fun6(self):
        f = open(self.file, "r+b")  # w+ used to read as wellas write file
        print(f.read())  # file is reading
        #f.write("Woopsd vinay! I have deleted the content!")  # writing  file

        f.close()



obj = files("testing.txt")
print(obj.my_function())
print(obj.my_fun1())
print(obj.my_fun2())
print(obj.my_fun3())
print(obj.my_fun4())
print(obj.my_fun5())
print(obj.my_fun6())



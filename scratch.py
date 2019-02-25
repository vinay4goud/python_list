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

    def __init__(self,  file , m):
        self.file=file
        self.m=m

    def _read(self):

        """
        here mode helps to read the file
        :return: reads files
        """


        f = open(self.file, self.m)
        return f.read() # reading complete file
        f.close()

    def _write(self):
        """
        writing  the  file and also creating new file
        :return: new file and  writing files
        """
        f = open(self.file,self.m)
        return f.write("not expected things in this way") # writing file and creating new file
        f. close()

    def  _read_write(self):
        """
        reading and write a file at once using mode r+
        :return: reads file and writes the files
        """



        f = open(self.file, self.m)
        f.write("wondeful")
        return f.readline()
        f.close()

    def _read__write(self):
        """
        reads the files as well as writes the files with mode w+
        :return: reading and writing file
        """

        f = open (self.file, self.m)
        f.write(" i thing all the thigs are being good")
        return f.read()
        f.close()

    def  _append(self):
        """
        we  upadating or adding new line in the exsisting  files with the help of mode a
        :return: adding new line to  exsiting file
        """

        f = open (self.file, self.m)
        return f.write (" \n very good morning  ")
        f.close()

    def _appendplus(self):

        """
        here updating or adding new lines to the exsisting files as well as reading the file by using mode a+

        :return: reading  file and adding new lines to file
        """

        f= open(self.file, self.m)

        f.write("\n great to see you ")

        print(f.read())

        f.close ()






obj = files("txt.txt", "r")
d = files("txt.txt","w")
e = files("txt.txt","r+")
f = files("lage.txt","w+")
g = files("large.txt", "a")
h = files("large.txt", "a+")
print(obj._read())
print (d._write())
print (e._read_write())
print (f._read__write)
print (g._append())
print (h._appendplus())

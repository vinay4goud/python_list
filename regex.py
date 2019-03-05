"""
reading a file , extracting date , name and content from the file
"""

import re
import json

class expresions:
    def __init__(self, filesinfo):

        self.fi= filesinfo

    def readfile(self):
        filez = open(self.fi, "r")
        reading = filez.read()
        return reading

    def readlinz(self):
        filez = open(self.fi, "r")
        reading = filez.readline()
        return reading

    def date(self):


        match = re.findall('\d{2}/\d{2}/\d{2}', self.readfile())

        return match

    def time(self):


        match = re.findall("\d{2}:\d{2} am|\d{2}:\d{2} pm", self.readfile())



        return match


    def name(self):

        match = re.split("\-",self.readlinz())
        smatch = match[1]
        #filedictionary = json.loads(smatch)
        divideinfo = re.split("\:",smatch)

        return divideinfo

    def dataf(self):

        date = re.findall("\d{2}/\d{2}/\d{2}",self.readlinz())

        time = re.findall("\d{1}:\d{2} am|\d{1}:\d{2} pm", self.readlinz())

        match = re.split("\-", self.readlinz())
        smatch = match[1]
        # filedictionary = json.loads(smatch)
        divideinfo = re.split("\:", smatch)


        return "".join(date) , "".join(time) , divideinfo[0], divideinfo[1]


    def gaol(self):

        x = self.dataf()

        return (x)

    def extractinformation(self):
        information_data = {}

        information_data['date'] = self.gaol()[0]
        information_data['time'] = self.gaol()[1]
        information_data['name'] = self.gaol()[2]
        information_data['content'] = self.gaol()[3]

        return information_data




wfile = expresions("Chat with.txt")

datez = wfile.date()
timez = wfile.time()
name = wfile.name()
dataf = wfile.dataf()
gaol = wfile.gaol()
infrom = wfile.extractinformation()

#print (f'{datez} \n {timez}')



#print (f'{name}')

#print (f'{dataf}')
print (f'{gaol[3]}')

print (f'{infrom}')




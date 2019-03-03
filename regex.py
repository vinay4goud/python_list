import re

class expresions:
    def __init__(self, filesinfo):

        self.fi= filesinfo

    def readfile(self):
        filez = open(self.fi, "r")
        reading = filez.read()
        return reading

    def date(self):


        match = re.findall('\d{2}/\d{2}/\d{2}', self.readfile())

        return match

    def time(self):


        match = re.findall("\d{1}:\d{2} am|\d{1}:\d{2} pm", self.readfile())



        return match

wfile = expresions("Chat with.txt")

datez = wfile.date()
timez = wfile.time()

print (f'{datez} \n {timez}')




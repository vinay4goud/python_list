"""
reading a file , extracting datetime , name and content from the file
"""
# importing regular expression  to execute the string as per requirment
import re
import datetime


# Classes provide a means of bundling data and functionality together
class expresions:

    # function to assign values
    def __init__(self, filesinfo):

        self.fi = filesinfo

    # function to read the file lines by line
    def dataf(self):

        """
        opeing file and reading file using mode
        READING file line by line
        :return: reading all the lines in file
        """
        with open(self.fi, 'r') as filez:


            a = filez.readlines()

            list_file = []
            for i in  a:
                dctionary_file = {}
                datez = re.findall("\d{2}/\d{2}/\d{2}|\d{1}/\d{2}/\d{2} \d{1}:\d{2} am| \d{2}:\d{2} am |\d{1}:\d{2} pm |\d{2}:\d{2} pm ",i)

                # date  contains read line
                if datez:


                    #date_obj1 = datetime.datetime.strptime(" ".join(datez), '%d/%m/%y %I:%M %p ')
                    match = re.split("\-", i)

                    #
                    date_obj1 = datetime.datetime.strptime(match[0], '%d/%m/%y, %I:%M %p ')

                    matchsecual= match[1].split(":",1)

                    dctionary_file['datetime']= date_obj1
                    dctionary_file['name']    = matchsecual[0]
                    dctionary_file['content']    = matchsecual[1].rstrip()


                    #print(dctionary_file)
                    list_file.append(dctionary_file )


            print(list_file)



# passing  value
wfile = expresions("Chat with.txt")

dataf = wfile.dataf()

print(dataf)
# infrom = wfile.extractinformation()

# print (f'{infrom}')

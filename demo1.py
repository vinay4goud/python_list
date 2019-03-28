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

    # function to read thelines by line
    @property
    def dataf(self):

        """
        opeing file and reading file using mode
        READING file line by line
        :return: reading all the lines in file
        """
        with open(self.fi, 'r') as filez:


            contentz = filez.readlines()

            list_file = []
            for i in  contentz:
                dctionary_file = {}
                datez = re.findall("\d{2}/\d{2}/\d{2}|\d{1}/\d{2}/\d{2} \d{1}:\d{2} am| \d{2}:\d{2} am|\d{1}:\d{2} pm|\d{2}:\d{2} pm",i)
                #datez = re.findall('(\d+/\d+/\d+),\s(\d{2}\:\d{2}\s(?:AM|PM|am|pm))')
                # read line if it has date in it
                if datez:


                    #date_obj1 = datetime.datetime.strptime(" ".join(datez), '%d/%m/%y %I:%M %p ')
                    # split the line
                    match = i.split("-", 1)

                    # read date from list
                    try :

                        date_obj1 = datetime.datetime.strptime(match[0], '%d/%m/%y, %H:%M ')

                    except:
                        date_obj1 = datetime.datetime.strptime(match[0], '%d/%m/%y, %I:%M %p ')






                    if ':' not in match[1]:
                        matchsecual = []
                        matchsecual.append('none')
                        matchsecual.append (match[1])
                    else:

                        # split list into two
                        matchsecual= match[1].split(":",1)


                    # add key and values to empty dictionary
                    dctionary_file['datetime']= date_obj1

                    dctionary_file['name'] = matchsecual[0]


                    dctionary_file['content']    = matchsecual[1].rstrip()


                    #print(dctionary_file)

                    # add dictionay to list
                    list_file.append(dctionary_file )




            # print the list
            return (list_file)



# passing  value
wfile = expresions("Chat with.txt")



dataf = wfile.dataf



print(dataf)

w_file =expresions("WhatsApp Chat with Builders real estate.txt")

datafile = w_file.dataf

print(datafile)


# infrom = wfile.extractinformation()

# print (f'{infrom}')

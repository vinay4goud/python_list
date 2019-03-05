"""
reading a file , extracting date , name and content from the file
"""
#importing regular expression  to execute the string as per requirment
import re

#Classes provide a means of bundling data and functionality together
class expresions:


    #function to assign values
    def __init__(self, filesinfo):

        self.fi= filesinfo

    # function to read the file lines by line
    def readfile(self):

        """
        opeing file and reading file using mode
        READING file line by line
        :return: reading all the lines in file
        """

        filez = open(self.fi, "r")

        reading = filez.readlines()

        return reading



    # function to extract required info from  lines in a file
    def dataf(self):

        """
        extract date , time and name and content from each line from read file
        :return: date , time and name  and content from file
        """

        for i in self.readfile():  # read line by line by  looping

            # extract date from read line
            date = re.findall("\d{2}/\d{2}/\d{2}|\d{1}/\d{2}/\d{2}",i)
            # # extract time from read line
            time = re.findall("\d{1}:\d{2} am| \d{2}:\d{2} am |\d{1}:\d{2} pm |\d{2}:\d{2} pm", i)
            # spliting line two
            match = re.split("\-", i)
            #  picking  name and content from list
            smatch = match[1]
            # split name and content into two values
            divideinfo = re.split("\:", smatch)

            # assining  date , time , name and  content to variable
            dict_chat_info = "".join(date) , "".join(time) , divideinfo[0], divideinfo[1]

            # empty dictionary
            information_data = {}


            # aadding values to empty  dictionary
            information_data['date'] = dict_chat_info[0]
            information_data['time'] = dict_chat_info[1]
            information_data['name'] = dict_chat_info[2]
            information_data['content'] = dict_chat_info[3]
            # print dictionary
            print ( information_data)



    """
    def extractinformation(self):


        information_data = {}

        information_data['date'] = self.dataf()[0]
        information_data['time'] = self.dataf()[1]
        information_data['name'] = self.dataf()[2]
        information_data['content'] = self.dataf()[3]

        return information_data  """
# passing  value to
wfile = expresions("Chat with.txt")

dataf = wfile.dataf()

print(dataf)
#infrom = wfile.extractinformation()

#print (f'{infrom}')
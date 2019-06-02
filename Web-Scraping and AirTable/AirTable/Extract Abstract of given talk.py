from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
import re
#The required libraries have been imported
url_airtable = " https://api.airtable.com/v0/appN4MSVPspT61ZEc/Talks"
api_key = "keyGP5NypsZdD6Jkf"
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}
#The URL and the key have been mentioned
r = requests.get(url_airtable, headers=headers)
data = r.json()

url_airtable1 = " https://api.airtable.com/v0/appN4MSVPspT61ZEc/Talks?offset="+data['offset']
r1 = requests.get(url_airtable1, headers=headers)
data1 = r1.json()
#The data corresponding to both data and offset data have been loaded
c = []
d = []
#Empty lists defined for further use
for book in data['records']:
    if 'Discipline' in book['fields']:
            c.append(book['fields']['Discipline'])
for book in data1['records']:
    if 'Discipline' in book['fields']:
            c.append(book['fields']['Discipline'])
for i in c:
    if i not in d:
        d.append(i)
#A list is created containing the list of all disciplines
s = 0
p = 0
for i in range (len(d)):
    s = s+1
    print(str(s)+". "+d[i])
print("Choose the discipline which you want to select")
t = int(input())
output_file = open("output.txt","w")
for book in data['records']:
    if 'Discipline' in book['fields'] and book['fields']['Discipline']==str(d[t-1]):
        p = p+1
        output_file.write("\n")
        output_file.write(str(p)+". "+str(book['fields']['FullTitle']))
        output_file.write("\n")
        output_file.write("By: "+str(book['fields']['Speaker']))
        output_file.write("\n")
        output_file.write("The date of the talk is "+str(book['fields']['Date'][0:10]))
        output_file.write("\n")
        output_file.write("\n")
        #All required fields are appropriately wriiten on the output file
        if 'Abstract' in book['fields']:
            output_file.write("The abstract of the talk is:")
            output_file.write("\n")
            output_file.write(book['fields']['Abstract'])
        else:
            output_file.write("Abstract not available")
        #An abstract is wriiten if available and an appropriate message is displayed if no abstract is available
        output_file.write("\n")
for book in data1['records']:
    if 'Discipline' in book['fields'] and book['fields']['Discipline']==str(d[t-1]):
        p = p+1
        output_file.write("\n")
        output_file.write(str(p)+". "+str(book['fields']['FullTitle']))
        output_file.write("\n")
        output_file.write("By: "+str(book['fields']['Speaker']))
        output_file.write("\n")
        output_file.write(book['fields']['Date'][0:10])
        output_file.write("\n")
        output_file.write("\n")
        #All required fields are appropriately wriiten on the output file
        if 'Abstract' in book['fields']:
            output_file.write("The abstract of the talk is:")
            output_file.write("\n")
            output_file.write(book['fields']['Abstract'])           
        else:
            output_file.write("Abstract not available")
        #An abstract is wriiten if available and an appropriate message is displayed if no abstract is available
        output_file.write("\n")
output_file.close()
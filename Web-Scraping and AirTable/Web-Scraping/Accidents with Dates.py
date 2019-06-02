from bs4 import BeautifulSoup
from datetime import date
import requests
import re
#all the required libraries and third pary applications like requests have been imported
f = str(input())
#an input has been taken
if int(f) > 2017:
    print("This year exists in the future")
elif int(f) < 1919:
    print("The commercial aviation industry wasn't put in place")
elif int(f) == 1921:
      print("No accident/incident took place in this year")
elif int(f) == 1925:
      print("No accident/incident took place in this year")
elif int(f) == 1932:
      print("No accident/incident took place in this year")
#the two cases in which the input taken is less than or greater than the time period have been dealt with
else:
    r = requests.get("http://en.wikipedia.org/wiki/List_of_accidents_and_incidents_involving_commercial_aircraft")
    c = r.content
#the content of the desired website has been loaded
    n = 0
    soup = BeautifulSoup(c,"html.parser")
    b = []
    d = []
#empty lists have been defined for future reference
    e = soup.find_all("h3")
    for i in range (len(e)-11):
       b.append(e[i].text.replace("[edit]",""))
#the list containing all years in which the incidents/accidents took place
    for i in range(len(b)):
        if f == b[i]:
           n = i
           break
    h = soup.find_all("ul")[n].text
    k = re.findall(r"(.*)\.\n",h)
#A list has been created containing description of all events, but the elements of the list are strings which contain all instances and need to be splitted using regular expressions
    a = soup.find_all("ul")
    g = []
    for i in range(len(a)-11):
       g.append([])
       for c in a[i].find_all('a'):
           g[i].append(c.get('href'))
#URLs of the various accidents/incidents have been captured into a list containing various nested lists
    for i in range(len(g)):
       for j in range (len(g[i])):
           g[i][j]= "https://en.wikipedia.org"+str(g[i][j])
#the appropriate starting of the URL has been appended to the URLs contained in the nested lists
    for i in range (len(k)):
       print(k[i])
       print("The URL of the above mentioned accident/incident is "+str(g[n][i]),"\n")
#a for loop is run to print all the accidents/incidents that took place in the year sequentially with the URL written separately below each instance

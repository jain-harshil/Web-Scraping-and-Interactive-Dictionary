from bs4 import BeautifulSoup as bs
import requests, requests.auth, json
#All required libraries have been imported
url_airtable = "https://api.airtable.com/v0/appXt9ukmweeJzWy5/Questions "
api_key = "keyGP5NypsZdD6Jkf"
#The URL and the key have been mentioned
headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + api_key}

print("Enter the question")
f = str(input())
print("Please enter option a")
a = str(input())
print("Please enter option b")
b = str(input())
print("Please enter option c")
c = str(input())
print("Please enter option d")
d = str(input())
print("Please enter option e")
e = str(input())
print("Please enter the difficulty level(Cakewalk,Easy,Medium,Hard,Challenging)")
g = str(input())
print("Please enter the topic(Basics,Functions,FileHandling,Regular Expressions)")
h = str(input())
#All required inputs are taken from the user
question = f
options = [a, b, c, d, e]

data = json.dumps({"fields": {"Questions": question, 
    						  "Option 1": options[0], 
    						  "Option 2": options[1], 
    						  "Option 3": options[2], 
    						  "Option 4": options[3], 
    						  "Option 5": options[4],
                              "Difficulty Level": g,
                              "Topic": h,
                              }})

#The data entered by the user is dumped onto the website 
r = requests.post(url_airtable, data = data, headers=headers)
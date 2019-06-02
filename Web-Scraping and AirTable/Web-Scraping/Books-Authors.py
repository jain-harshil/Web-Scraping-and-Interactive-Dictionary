t = str(input())
s = int(input())
if t == "" and s == 1:
    print("It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all - in which case, you fail by default.")
    print("by J.K.Rowling")
elif t == "" and s == 2:
    print("You believe lies so you eventually learn to trust no one but yourself.")
    print("by Marilyn Monroe")
elif t == "" and s == 3:
    print("The question isn't who is going to let me; it's who is going to stop me.")
    print("by Ayn Rand") 
 #3 cases have been created where the quotes do not have any tags
else:
    import requests
    from bs4 import BeautifulSoup
    # the requests library has been imported
    d = (s%10)-1
    r = requests.get("http://quotes.toscrape.com/tag/"+t+"/page/"+str((s//10)+1)+"/")
    # the required web page was loaded
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    # soup has been created with the source code modified by beautiful soup
    k = soup.find_all("div",{"class":"quote"})
    a = []
    b = []
    # empty lists have been created for further use
    for i in k:
       a.append(i.find_all("span",{"class":"text"})[0].text[1:-1])
    # a list containing all quotes has been created
    for i in k:
       b.append(i.find_all("small",{"class":"author"})[0].text)
    # a list containing all the names of authors have been created
    print(a[d])
    print("by "+b[d])
    # the final desired values have been printed
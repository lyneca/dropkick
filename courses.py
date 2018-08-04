url = "http://sydney.edu.au/handbooks/science/table1/table1_computer_science.shtml"

from bs4 import BeautifulSoup
import urllib
html_doc = urllib.request.urlopen(url)
soup = BeautifulSoup(html_doc, 'html.parser')

course = {}
import re
def matchCode(string):
    result = re.match("^[A-Z]{4}[0-9]{4}$", string)
    if result!=None:
        return True
    else:
        return False

class Course():
    def __init__(self, *initial_data,**kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

table = soup.find(id="w4")
for row in table.find_all('tr',valign="top"):
    col = row.find_all('td')

    if len(col)==4:
        name = col[0].text
        credit = col[1].text
        time = col[3].text
        course[name] = Course(name=name, credit = credit,time=time)
        APN = col[2].text
        A = []
        P = []
        N = []
        if len(APN)!=1:
            #empty prerequisite bar
            pass


        print(name,credit,APN,time)
    print("--")

print(type(soup))
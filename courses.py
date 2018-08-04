url = "file:///Users/shirley/Desktop/dropkick/Table%201_%20Computer%20Science%20-%20Science%20-%20The%20University%20of%20Sydney.htm"
chemurl = "http://sydney.edu.au/handbooks/science/table1/table1_chemistry.shtml"
from bs4 import BeautifulSoup
import urllib

html_doc = urllib.request.urlopen(chemurl)
soup = BeautifulSoup(html_doc, 'html.parser')

course = {}
import re
def matchCode(string):
    result = re.match("^[A-Z]{4}[0-9]{4}$", string)
    if result!=None:
        return True
    else:
        return False

def matchList(string):
    #find all matched course code in a string.
    return re.findall("[A-Z]{4}[0-9]{4}", string)


class Course():
    def __init__(self, *initial_data,**kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        return 'Unit Code: ' + self.code + '\n' + '\nName: ' + self.name+ '\n' + '\nCredit:' + self.credit+'\n'+'\nA:' + str(self.A) + '\n'+'\nP:' + str(self.P) + '\n'+'\nN:' + str(self.N) + '\n' + '\nTime:' + self.time + "\n"



table = soup.find(id="w4")
for row in table.find_all('tr',valign="top"):
    col = row.find_all('td')

    if len(col)==4:
        name = col[0].text
        code = matchList(name)[0]
        credit = col[1].text
        time = col[3].text
        APN = col[2].text

        A = []
        P = []
        N = []
        A_pos = APN.find("A ")
        P_pos = APN.find("P ")
        N_pos = APN.find("N ")
        if len(APN)!=1:
            #non empty prerequisite bar
            if A_pos!=-1:
                A_pos = A_pos+2
                if P_pos!=-1:
                    A.append(APN[A_pos:P_pos])
                elif N_pos!=-1:
                    A.append(APN[A_pos:P_pos])
                else:
                    A.append(APN[A_pos:])
                AL = matchList(A[0])
                if len(AL)>0:
                    A = AL
            if P_pos!=-1:
                P_pos =P_pos+2
                if N_pos!=-1:
                    P.append(APN[P_pos:N_pos])
                else:
                    P.append(APN[P_pos:])
                PL = matchList(P[0])
                if len(PL)>0:
                    P=PL
            if N_pos!=-1:
                N_pos = N_pos+2
                N.append(APN[N_pos:])
                if  len(matchList(N[0]))>0:
                    N = matchList(N[0])


                #try to extract substring of Assumed Knowledge




        course[code] = Course(code =code,name=name, credit=credit,time=time, A=A, P=P, N=N)


def matchObjects(A):
    #A =['1110' '1111'...]
    A= list(set(A) & set(course.keys()))
    l = [course[x] for x in A]
    if len(l)>0:
        return l
    else:
        return A


# for i in course.values():
#     i.A=matchObjects(i.A)
#     i.P=matchObjects(i.P)
#     i.N=matchObjects(i.N)
    #print("--")

for i in course.values():
    print(i)

import networkx as nx

G = nx.DiGraph()

G.add_nodes_from(course.keys())
print(G)
for i in G.nodes:
    for j in course[i].P:
        if j in G.nodes:
            G.add_edge(i, j)
    for j in course[i].A:
        if j in G.nodes:
            G.add_edge(i, j)


#print(G.edges())
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

nx.draw_spring(G, with_labels = True)
# plt.draw()
# plt.show()
# print('____End of the program____')

def queryCourse(coursename):
    #should return the nested json file rooted at the course.
    d = nx.dfs_successors(G, coursename)

    



    #file = open("course.json","w")





    return None

queryCourse('CHEM3117')
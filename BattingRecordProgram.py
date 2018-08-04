import requests
import bs4
import scrap
count=0
teamscount=0
for i in range(0,8):
    #print(scrap.test[i])
    tr=requests.get(scrap.test[i])
    #print(tr.text)
    teamscount=teamscount+1
    sopu=bs4.BeautifulSoup(tr.text,'lxml')
    rt=[]
    containers = sopu.findAll('table')[2].tbody.findAll('tr')
    for row in sopu.findAll('table')[2].tbody.findAll('tr'):
        count=count+1

        if i==1 or i==4 :
            first_column = row.findAll('td')[0]
            runs = row.findAll('td')[4].contents
            ave = row.findAll('td')[6].contents
            strike = row.findAll('td')[8].contents
            print("{}  {}  {}  {}  {} ".format(scrap.teams[i],(first_column.a.text), (runs[0].text), (ave[0]), (strike[0])))
        else:
            first_column = row.findAll('td')[0]
            runs = row.findAll('td')[5].contents
            ave = row.findAll('td')[7].contents
            strike = row.findAll('td')[9].contents
            print("{}  {}  {}  {}  {} ".format(scrap.teams[i],(first_column.a.text), (runs[0].text), (ave[0]), (strike[0])))
print("total teams retrived are : {} ".format(teamscount))
print("total no of players data retrived are : {} ".format(count))

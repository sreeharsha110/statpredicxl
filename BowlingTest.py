import requests
import bs4
import scrap
import csv
# funtion takes input: a file name to store data
# output : scrapped data is stored in csv file it collects test match data
def testBowling(filename):
    try:


        count=0
        teamscount=0
        with open(filename,'w',newline='')as f: #opening a csv file
            thewritter=csv.writer(f)
            thewritter.writerow(['Nation','Playername','Wickets','Average','Economy','Strikerate'])


            for i in range(0,8):
                #print(scrap.test[i])
                tr=requests.get(scrap.testbowl[i])
                #print(tr.text)
                teamscount=teamscount+1
                sopu=bs4.BeautifulSoup(tr.text,'lxml')
                rt=[]
                containers = sopu.findAll('table')[2].tbody.findAll('tr')
                for row in sopu.findAll('table')[2].tbody.findAll('tr'):

                    count=count+1

                    if i==1   or i==4 : # if and else are used to change in rows data in diffrent webpages
                        first_column = row.findAll('td')[0]
                        wickets= row.findAll('td')[6].contents
                        ave = row.findAll('td')[9].contents
                        eco=row.findAll('td')[10].contents
                        strike = row.findAll('td')[11].contents
                        thewritter.writerow([scrap.teams[i],first_column.a.text,wickets[0].text,ave[0],eco[0],strike[0]])
                        #print("{}  {}  {}  {}  {}  {} ".format(scrap.teams[i],(first_column.a.text), (wickets[0].text), (ave[0]),eco[0], (strike[0])))
                    else:
                        first_column = row.findAll('td')[0]
                        wickets = row.findAll('td')[7].contents
                        ave = row.findAll('td')[10].contents
                        eco = row.findAll('td')[11].contents
                        strike = row.findAll('td')[12].contents
                        thewritter.writerow([scrap.teams[i], first_column.a.text, wickets[0].text, ave[0],eco[0],strike[0]])
                        #print("{}  {}  {}  {}  {}  {} ".format(scrap.teams[i],(first_column.a.text), (wickets[0].text), (ave[0]),eco[0] ,(strike[0])))
        print("total teams retrived are : {} ".format(teamscount))
        print("total no of players data retrived are : {} ".format(count))
    except:
        print("No internet connection cant update the data")

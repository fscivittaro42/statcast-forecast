import csv
import sqlite3
import re
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

# import pdb; pdb.set_trace()

#PlayerID,Name,Team,G,AB,PA,H,1B,2B,3B,HR,R,RBI,BB,IBB,SO,HBP,SF,SH,GDP,SB,CS,AVG

def grabData():
    ## Shift Data
    Normal = 'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=1&type=0&season=2016&month=0&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    Shift = 'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=1&type=0&season=2016&month=61&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    No_Shift = 'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=1&type=0&season=2016&month=62&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    Shift_Traditional = 'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=1&type=0&season=2016&month=63&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    Shift_NonTraditional = 'http://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=1&type=0&season=2016&month=64&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'

    Url_Main =  Shift_NonTraditional
    Page = urlopen(Url_Main)
    soup = BeautifulSoup(Page, "lxml")

    player_list = soup.select('#LeaderBoard1_dg1_ctl00 tr')

    players = []

    #players = [['PlayerID','Name','Team','G','PA','HR','R','RBI','SB','BBPer','KPer','ISO','BABIP','AVG','OBP','SLG','wOBA','wRCPlus','BSR','Off','Def','WAR']]
    #players = [['PlayerID','Name','Team','G','AB','PA','H','1B','2B','3B','HR','R','RBI','BB','IBB','SO','HBP','SF','SH','GDP','SB','CS','AVG']]

    for row in player_list:
        if row.attrs.get('class') and row.attrs.get('class')[0] in ['rgRow', 'rgAltRow']:
            info = row.select('td')
            name = info[1].text
            team = info[2].text
            G = info[3].text
            PA = info[4].text
            HR = info[5].text
            R = info[6].text
            RBI = info[7].text
            SB = info[8].text
            BBPer = info[9].text
            KPer = info[10].text
            ISO = info[11].text
            BABIP = info[12].text
            AVG = info[13].text
            OBP = info[14].text
            SLG = info[15].text
            wOBA = info[16].text
            wRCPlus = info[17].text
            BSR = info[18].text
            Off = info[19].text
            Def = info[20].text
            WAR = info[21].text
            AVG = info[22].text
            result = re.search("playerid=(\\d*)", str(info[1]))
            if result:
                playerid = result.group(1)
            else:
                playerid = None

            l = [playerid, name, team, G, PA, HR, R, RBI, SB, BBPer, KPer, ISO, BABIP, AVG, OBP, SLG, wOBA, wRCPlus, BSR, Off, Def, WAR, AVG]
            players.append(l)


    ## remove pitches, which we aquire from here, from the above sample


    P_Normal = 'http://www.fangraphs.com/leaders.aspx?pos=p&stats=bat&lg=all&qual=1&type=0&season=2016&month=0&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    P_Shift = 'http://www.fangraphs.com/leaders.aspx?pos=p&stats=bat&lg=all&qual=1&type=0&season=2016&month=61&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    P_No_Shift = 'http://www.fangraphs.com/leaders.aspx?pos=p&stats=bat&lg=all&qual=1&type=0&season=2016&month=62&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    P_Shift_Traditional = 'http://www.fangraphs.com/leaders.aspx?pos=p&stats=bat&lg=all&qual=1&type=0&season=2016&month=63&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'
    P_Shift_NonTraditional = 'http://www.fangraphs.com/leaders.aspx?pos=p&stats=bat&lg=all&qual=1&type=0&season=2016&month=64&season1=2016&ind=0&team=0&rost=0&age=0&filter=&players=0&page=1_1000'

    Url_Main =  P_Shift_NonTraditional
    Page = urlopen(Url_Main)
    soup = BeautifulSoup(Page, "lxml")

    pitcher_list = soup.select('#LeaderBoard1_dg1_ctl00 tr')

    pitchers = []

    # pitchers = [['PlayerID','Name','Team','G','AB','PA','H','1B','2B','3B','HR','R','RBI','BB','IBB','SO','HBP','SF','SH','GDP','SB','CS','AVG']]

    for row in pitcher_list:
        if row.attrs.get('class') and row.attrs.get('class')[0] in ['rgRow', 'rgAltRow']:
            info = row.select('td')
            name = info[1].text
            team = info[2].text
            G = info[3].text
            PA = info[4].text
            HR = info[5].text
            R = info[6].text
            RBI = info[7].text
            SB = info[8].text
            BBPer = info[9].text
            KPer = info[10].text
            ISO = info[11].text
            BABIP = info[12].text
            AVG = info[13].text
            OBP = info[14].text
            SLG = info[15].text
            wOBA = info[16].text
            wRCPlus = info[17].text
            BSR = info[18].text
            Off = info[19].text
            Def = info[20].text
            WAR = info[21].text
            AVG = info[22].text
            result = re.search("playerid=(\\d*)", str(info[1]))
            if result:
                playerid = result.group(1)
            else:
                playerid = None

            p = [playerid, name, team, G, PA, HR, R, RBI, SB, BBPer, KPer, ISO, BABIP, AVG, OBP, SLG, wOBA, wRCPlus, BSR, Off, Def, WAR, AVG]
            pitchers.append(p)

    # batters = [x for x in players if x[0] not in pitchers[0]]

    # batter_df = pd.DataFrame(batters)

    # batter_df.to_csv('shift_nontrad_data.csv', index=False, header=False)

    # pitcher_df = pd.DataFrame(pitchers)

    # pitcher_df.to_csv('pitcher_shift_nontrad.csv', index=False, header=False)



## SQl Prep

# Batters

batter_data = list(csv.reader(open('batter_data.csv','r')))

batter_shift_data = list(csv.reader(open('shift_data.csv','r')))

batter_noshift_data = list(csv.reader(open('no_shift_data.csv','r')))

batter_nontrad_data = list(csv.reader(open('shift_nontrad_data.csv','r')))

batter_trad_data = list(csv.reader(open('shift_trad_data.csv','r')))

## Pitchers

pitcher_data = list(csv.reader(open('pitcher_data.csv','r')))

pitcher_shift_data = list(csv.reader(open('pitcher_shift.csv','r')))

pitcher_noshift_data = list(csv.reader(open('pitcher_noshift.csv','r')))

pitcher_nontrad_data = list(csv.reader(open('pitcher_shift_nontrad.csv','r')))

pitcher_trad_data = list(csv.reader(open('pitcher_shift_trad.csv','r')))


b = batter_data
bs = batter_shift_data
bns = batter_noshift_data
bt = batter_trad_data
bnt = batter_nontrad_data

for player in b:
    player.append(False)
    player.append(False)

for player in bs:
    player.append(True)
    player.append(False)

for player in bns:
    player.append(True)
    player.append(False)

for player in bt:
    player.append(True)
    player.append(False)

for player in bnt:
    player.append(True)
    player.append(False)


p = pitcher_data
ps = pitcher_shift_data
pns = pitcher_noshift_data
pt = pitcher_trad_data
pnt = pitcher_nontrad_data

for player in p:
    player.append(False)
    player.append(True)

for player in ps:
    player.append(True)
    player.append(True)

for player in pns:
    player.append(True)
    player.append(True)

for player in pt:
    player.append(True)
    player.append(True)

for player in pnt:
    player.append(True)
    player.append(True)


## connecting to the database

# https://docs.python.org/3/library/sqlite3.html

connection = sqlite3.connect('sqlcode.sqlite3')

cursor = connection.cursor()

# import pdb; pdb.set_trace();
# example
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", b)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bs)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bns)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bt)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", bnt)

cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", p)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ps)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", pns)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", pt)
cursor.executemany("INSERT INTO players VALUES (?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", pnt)
# Save / commit changes
connection.commit()

# close the connection
connection.close()

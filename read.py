from bs4 import BeautifulSoup
import urllib.request as urllib2
import pandas as pd
from datetime import datetime

url = "http://www.cricketedmonton.com/season-2018/fixtures/"
text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text, "html.parser")


div = soup.find('div', attrs={'class':'entry-content'})
link = div.a.get('href')

print(link)
xls = pd.ExcelFile(link, header=None)
print(xls.sheet_names)

# load the sheet
schedule = xls.parse('Schedule')
schedule.columns = ['Date', 'Day', 'Victoria ParkM', 'Victoria ParkE', 'MillwoodsM', 'MillwoodsE', 'StAlbertM', 'StAlbertE', 'CastledownsM', 'CastledownsE', 'Red Deer', 'Out of City Events', '', 'Premier Division', 'T20 Premier Division']


for index, row in schedule.iterrows():
    if str(row["Date"]) != 'NaT':
        this_date = str(row["Date"])
        date = datetime.strptime(this_date, '%Y-%m-%d %H:%M:%S').date()
        search_for = 'CHA'
        ground = ''
        match = ''

        today = datetime.now().strftime('%Y-%m-%d')

        if str(row['Victoria ParkM']) != 'nan' and str(row['Victoria ParkM']).find(search_for) != -1:
            ground = 'VP'
            match = row['Victoria ParkM']
        elif str(row['Victoria ParkE']) != 'nan' and str(row['Victoria ParkE']).find(search_for) != -1:
            ground = 'VP'
            match = row['Victoria ParkE']
        elif str(row['MillwoodsM']) != 'nan' and str(row['MillwoodsM']).find(search_for) != -1:
            ground = 'Millwoods'
            match = row['MillwoodsM']
        elif str(row['MillwoodsE']) != 'nan' and str(row['MillwoodsE']).find(search_for) != -1:
            ground = 'Millwoods'
            match = row['MillwoodsE']
        elif str(row['StAlbertM']) != 'nan' and str(row['StAlbertM']).find(search_for) != -1:
            ground = 'StAlbert'
            match = row['StAlbertM']
        elif str(row['StAlbertE']) != 'nan' and str(row['StAlbertE']).find(search_for) != -1:
            ground = 'StAlbert'
            match = row['StAlbertE']
        elif str(row['CastledownsM']) != 'nan' and str(row['CastledownsM']).find(search_for) != -1:
            ground = 'Castledowns'
            match = row['CastledownsM']
        elif str(row['CastledownsE']) != 'nan' and str(row['CastledownsE']).find(search_for) != -1:
            ground = 'Castledowns'
            match = row['CastledownsE']
        elif (str(row['Red Deer']) != 'nan' and str(row['Red Deer']) != "") and str(row['Red Deer']).find(search_for) != -1:
            ground = 'Red Deer'
            match = row['Red Deer']
        else:
            ground = ''
            match = ''

        print(str(date)+ ' - ' + str(row['Day']) + ' - ' +ground+' - '+match)

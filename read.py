from bs4 import BeautifulSoup
import urllib.request as urllib2
import pandas as pd
from datetime import datetime

url = "http://www.cricketedmonton.com/season-2018/fixtures/"
text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text, "html.parser")


div = soup.find('div', attrs={'class':'entry-content'})
link = div.a.get('href')

# print(link)
xls = pd.ExcelFile(link, header=None)
# print(xls.sheet_names)

# load the sheet
schedule = xls.parse('Schedule')
schedule.columns = ['date', 'day', 'victoria_park_m', 'victoria_park_e', 'millwoods_m', 'millwoods_e', 'st_albert_m', 'st_albert_e', 'castledowns_m', 'castledowns_e', 'red_deer', 'out_of_city_events', '', 'premier_division', 't20_premier_division']


for index, row in schedule.iterrows():
    if str(row["date"]) != 'NaT':
        this_date = str(row["date"])
        date = datetime.strptime(this_date, '%Y-%m-%d %H:%M:%S').date()
        search_for = 'CHA'
        ground = ''
        match = ''

        today = datetime.now().strftime('%Y-%m-%d')

        if str(row['victoria_park_m']) != 'nan' and str(row['victoria_park_m']).find(search_for) != -1:
            ground = 'Victoria Park'
            match = row['victoria_park_m']
        elif str(row['victoria_park_e']) != 'nan' and str(row['victoria_park_e']).find(search_for) != -1:
            ground = 'Victoria Park'
            match = row['victoria_park_e']
        elif str(row['millwoods_m']) != 'nan' and str(row['millwoods_m']).find(search_for) != -1:
            ground = 'Millwoods'
            match = row['millwoods_m']
        elif str(row['millwoods_e']) != 'nan' and str(row['millwoods_e']).find(search_for) != -1:
            ground = 'Millwoods'
            match = row['millwoods_e']
        elif str(row['st_albert_m']) != 'nan' and str(row['st_albert_m']).find(search_for) != -1:
            ground = 'St.Albert'
            match = row['st_albert_m']
        elif str(row['st_albert_e']) != 'nan' and str(row['st_albert_e']).find(search_for) != -1:
            ground = 'St.Albert'
            match = row['st_albert_e']
        elif str(row['castledowns_m']) != 'nan' and str(row['castledowns_m']).find(search_for) != -1:
            ground = 'Castledowns'
            match = row['castledowns_m']
        elif str(row['castledowns_e']) != 'nan' and str(row['castledowns_e']).find(search_for) != -1:
            ground = 'Castledowns'
            match = row['castledowns_e']
        elif (str(row['red_deer']) != 'nan' and str(row['red_deer']) != "") and str(row['red_deer']).find(search_for) != -1:
            ground = 'Red Deer'
            match = row['red_deer']
        else:
            ground = ''
            match = ''

        print(str(date)+ ' - ' + str(row['day']) + ' - ' +ground+' - '+match)

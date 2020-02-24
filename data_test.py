from bs4 import BeautifulSoup
import requests

URL = "http://mlb.mlb.com/stats/sortable.jsp?c_id=mlb#elem=%5Bobject+Object%5D&tab_level=child&click_text=Sortable+Player+hitting&game_type='S'&season=2019&season_type=ANY&league_code='MLB'&sectionType=sp&statType=hitting&page=1&ts=1582502541691&playerType=QUALIFIER&sportCode='mlb'&split=&team_id=&active_sw=&position=&page_type=SortablePlayer&sortOrder='desc'&sortColumn=avg&results=&perPage=50&timeframe=&last_x_days=&extended=0"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
batting_avg = results.find_all('td', class_='dg-obp')

for bat in batting_avg:
    print(bat, end='\n'*2)

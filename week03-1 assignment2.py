import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

teams = soup.select('#regularTeamRecordList_table > tr')
for team in teams:
    rank = team.select_one('th > strong').text
    name = team.select_one('td.tm > div > span').text
    if rank is not None and name is not None:
        print(rank, name)
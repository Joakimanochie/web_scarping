from bs4 import BeautifulSoup
import requests

req = requests.get('https://www.ycombinator.com/topcompanies')
soup = BeautifulSoup(req.content, 'lxml')

companies = soup.find_all('tr', class_="top-company-row")
for company in companies:
    c_name = company.find('a', class_="company-name").span
    rank = company.find('td', class_="rank")
    over_view = company.find('td', class_="company-overview")
    batch = company.find('td', class_="small-batch")
    location = company.find('td', class_="headquarters")
    print(f'''
    Company Name: {c_name.text}
    Rank: {rank.text}
    Description: {over_view.text}
    Batch: {batch.text}
    Company locations: {location.text}
    ''')

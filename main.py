import requests
from bs4 import BeautifulSoup
import smtplib

NFL_URL = 'https://www.nfl.com/'
MY_EMAIL = MY_EMAIL
MY_PASSWORD = MY_PASSWORD
MY_TEAM = 'Broncos'

nfl_page = requests.get(NFL_URL)
soup = BeautifulSoup(nfl_page.text, 'html.parser')

headlines = soup.find_all('span', class_='nfl-o-headlinestack__item-text')
headline_list = [headline.text for headline in headlines]


for headline in headline_list:
    if MY_TEAM in headline:

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject: BRONCOS HEADLINE\n\n{headline}\n{NFL_URL}news"
                # I tried with the full message here, but wasn't working, I think that there is a limit.
            )


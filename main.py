from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
app = FastAPI()


@app.get("/")
async def home():
    return ("Welcome to LeetCode API. Read the github docs for more details")


@app.get('/{username}')
async def getData(username: str):
    url = f'https://leetcode.com/{username}/'
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        # name =
        data = {'username': soup.find(
            'div', class_='text-label-1 dark:text-dark-label-1 break-all text-base font-semibold').text,
            'rank': soup.find('span', class_='ttext-label-1 dark:text-dark-label-1 font-medium').text,


        }
        return data

    else:
        return ("User not found")

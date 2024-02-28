from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
app = FastAPI()


@app.get("/")
async def home():
    return ("Welcome to Instagram API. Read the github docs for more details")


@app.get('/getUserdata/{username}')
async def getData(username: str):
    url = f'https://leetcode.com/{username}/'
    page = requests.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')

        

    else:
        return ("User not found")

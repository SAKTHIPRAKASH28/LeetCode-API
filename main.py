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
        languages = soup.find_all(
            'div', class_='flex items-center justify-between text-xs text-label-1 dark:text-dark-label-1')
        language_wise_solved = {}
        for language in languages:
            language_wise_solved[language.find(
                'span', class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate').text] = language.find('span', 'text-xs font-medium text-label-1 dark:text-dark-label-1').text

        data = {'username': soup.find(
            'div', class_='text-label-1 dark:text-dark-label-1 break-all text-base font-semibold').text,
            'rank': soup.find('span', class_='ttext-label-1 dark:text-dark-label-1 font-medium').text,
            'language_wise_problems_solved': language_wise_solved,
            'solved_count': {'easy'}



        }
        return data

    else:
        return ("User not found")

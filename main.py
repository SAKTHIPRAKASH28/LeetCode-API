from os import getenv
import uvicorn
from typing import Optional
from fastapi import FastAPI
from bs4 import BeautifulSoup
import httpx
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(title="Leet Code Scraper",
              description="A web scraper for getting user details and progress from LeetCode.", contact={"name": "Sakthi Prakash", "email": "sakthiprakash403@gmail.com", "url": "https://github.com/SAKTHIPRAKASH28/LeetCode-API"}, version="0.0.1")

# CORS (Cross-Origin Resource Sharing) middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this based on your CORS requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return RedirectResponse("/docs")


@app.get('/{username}')
async def getData(username: str, query: Optional[str] = None):
    url = f'https://leetcode.com/{username}/'
    async with httpx.AsyncClient() as client:
        page = await client.get(url)

    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        languages = soup.find_all(
            'div', class_='flex items-center justify-between text-xs text-label-1 dark:text-dark-label-1')
        problems_count = {}
        language_wise_solved = {}
        for language in languages:
            language_wise_solved[language.find(
                'span', class_='inline-flex items-center px-2 whitespace-nowrap text-xs leading-6 rounded-full text-label-3 dark:text-dark-label-3 bg-fill-3 dark:bg-dark-fill-3 notranslate').text] = int(language.find('span', 'text-xs font-medium text-label-1 dark:text-dark-label-1').text)

        problems = soup.find_all('div', class_='flex w-full items-end text-xs')
        for prob in problems:
            problems_count[prob.find('div', class_='w-[53px] text-label-3 dark:text-dark-label-3').text] = int(prob.find(
                'span', class_='mr-[5px] text-base font-medium leading-[20px] text-label-1 dark:text-dark-label-1').text)

        data = {'username': soup.find(
            'div', class_='text-label-1 dark:text-dark-label-1 break-all text-base font-semibold').text,
            'rank': int(soup.find('span', class_='ttext-label-1 dark:text-dark-label-1 font-medium').text.replace(',', '')),
            'language_wise_problems_solved': language_wise_solved,
            'solved_count': problems_count,



        }
        if not query:
            return data
        return {query: data[query]}

    else:
        return {"error": f"No user with the user name {username} found!"}


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

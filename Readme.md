# LeetCode-API with FastAPI

## Overview

Welcome to the LeetCode-API built with FastAPI! This API allows you to retrieve user-specific data from LeetCode profiles, including language-wise problems solved and overall problem-solving statistics.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/SAKTHIPRAKASH28/LeetCode-API.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Home Route

- **GET /:**
  - Description: Displays a welcome message and provides information about accessing the LeetCode-API and documentation.
  - Example: [http://localhost:8000/](http://localhost:8000/)

### User Data Route

- **GET /{username}:**
  - Description: Retrieves LeetCode user-specific data based on the provided username.
  - Parameters:
    - `username`: The LeetCode username for which you want to fetch data.
  - Example: [http://localhost:8000/{username}](http://localhost:8000/{username})

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): A Python library for pulling data out of HTML and XML files.
- [Requests](https://docs.python-requests.org/en/latest/): A simple HTTP library for Python.

## Running the Application

```bash
uvicorn main:app --reload
```

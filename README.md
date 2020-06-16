<h1 align="center">Flask Server for Twitter Harvesting (FSTH)</h1>

<div align="center">

![Python version](https://img.shields.io/badge/python-3.7+-blue.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

A small Python project to pull data from Twitter using Flask webserver and SQLite database. 

## Table of contents

1. [Introduction](#introduction)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Next](#next)
1. [Contributing](#contributing)


## Introduction

This roject is based on the following technology stack Python, Flask (SQLAlchemy, Marshmallow) and SQLite. The harvester fetches posts from Twitter and saves them in the database. This project can be used for collecting large data sets in a short time period. It might be helpful for data analysis/visualization projects.

The maximum number of gathered Tweets can't exceed 1% of the global number of tweets (throughput). During the data harvesting, some rate limits might be exceeded or other connection errors might appear, thus you can set the waiting time between calls if any errors appear using the `ERROR_WAIT_TIME` variable. The default value is set to 60 seconds.


## Installation

Download the repository and enter the main directory with the `Pipfile` and then execute the below commands:

```bash
pipenv install
pipenv shell
```

The next step is to initialize the database. Execute the below commands (stay in the main directory of the project):

```bash
cd app
python
```

```python
from app.app import db
db.create_all()
quit()
```

In the app directory, you should see an initialized database i.e. `db.sqlite`.

### Environment variables

Create `.env` file in the main directory of the project and add the below necessary variables. The first four variables are credentials to your developer Twitter account.

- `CONSUMER_KEY`
- `CONSUMER_SECRET`
- `ACCESS_KEY`
- `ACCESS_SECRET`
- `KEYWORDS` example value `bitcoin,gold`

Configurable variables (not necessary to configure):
- `POST_API_URL` (default value: `http://127.0.0.1:5000/tweet`)

The value might differ based on Flask PORT and endpoint name.

- `ERROR_WAIT_TIME` (default value: `60`)

The measure is based on seconds. You can increase/decrease the value based on your own preferences.

## Usage

After doing all the above steps you should run the flask server and the twitter harvester package. 

### running Flask server

To do that enter the `app` directory using the open terminal and run the below commands:

```bash
python app.py
```

### running Twitter harvester

Open one more terminal window, navigate to the project directory and execute the below commands:

```bash
pipenv shell
cd twitter
python main.py
```

### checking gathered Tweets

Open Postman or other API/REST development tool and create a GET request using `http://127.0.0.1:5000/tweets` endpoint.

Here is an example chunk of returned results:

```markup
[
  {
    "created_at": "2020-06-13 19:56:41",
    "id": 1,
    "source": "Twitter for iPhone",
    "tweet": "https://twitter.com/statuses/1271894280471146496",
    "tweet_id": 1271894280471146496,
    "tweet_url": "b'RT @JanetWintsbit: Full List of 2020 #Ethereum $ETH Partnerships, Integrations'",
    "user": "fcknarbn"
  },
  {
    "created_at": "2020-06-13 19:56:43",
    "id": 2,
    "source": "Twitter Web App",
    "tweet": "https://twitter.com/statuses/1271894287760764928",
    "tweet_id": 1271894287760764928,
    "tweet_url": "b'dPi just looking sexy and getting more functionality.'",
    "user": "carsenjk"
  }
]
```

## Next
- add tests
- data cleaning before inserting into the database
- adding another webserver for data gathering from other sources like Google Trends/currency markets etc.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

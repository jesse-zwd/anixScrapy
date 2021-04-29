# AniX - Stream Animes

This is the backend repository of AniX built with scrapy framework. 

## Spiders

| name                                           | description                  |
| ---------------------------------------------- | ---------------------------- |
| [animes](anixScrapy/spiders/animes.py)               | fetch animes                 |
| [anime](anixScrapy/spiders/anime.py)                 | fetch a single anime         |
| [search_animes](anixScrapy/spiders/search_animes.py) | search animes                |
| [stream](anixScrapy/spiders/stream.py)               | fetch mp4 link for a episode |

## Running Locally

- Clone this repo to your local machine and navigate to the root directory

- Run the following commands to start the http server

	```bash
	create a virtual env

	pip install -r requirements.txt # installing dependencies

	scrapyrt # start the http server
	```
- By default, the http server will listening for requests at port 9080

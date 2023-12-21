# Day 45 - Movies and Hacker News Scrapper

## main_hackernews.py:
This Python script uses the BeautifulSoup library to scrape information from the "Hacker News" website (https://news.ycombinator.com/).  
It fetches the HTML content of the webpage using the requests library, and then parses the HTML using BeautifulSoup.
The script extracts data about articles, including their titles, links, and votes.
The script then prints the title, link, and number of votes for the article with the highest number of votes.

## main_top100movies.py:
This Python script uses BeautifulSoup to scrape movie titles from a specified URL representing a web archive of an Empire Online page listing the "best movies" (https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").  
It retrieves the HTML content using the requests library, parses it with BeautifulSoup, and extracts movie titles from elements with the tag name "h3" and the class "title".  
The script then writes the movie titles in reverse order to a text file named "movies.txt".

In summary, both scripts demonstrate the use of BeautifulSoup for web scraping in Python, extracting specific information from HTML elements on different websites. The first script focuses on Hacker News articles and their votes, while the second script deals with movie titles from an Empire Online page.
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_titles = []
article_links = []
for article in articles:
    title = article.find("a").getText()
    article_titles.append(title)
    link = article.find("a").get("href")
    article_links.append(link)

article_votes = []
for article in soup.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_votes.append(0)
    else:
        article_votes.append(int(article.span.find(class_="score").getText().split()[0]))

largest_votes_idx = article_votes.index(max(article_votes))

print(article_votes[largest_votes_idx])
print(article_titles[largest_votes_idx])
print(article_links[largest_votes_idx])



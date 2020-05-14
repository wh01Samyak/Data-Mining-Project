import requests
import json
import csv

def get_article_urls(data):
    urls = []
    for post in data:
        urls.append(post["url"])

    return urls

# extract info about the news post like date, headline/title, article url, score
# ignore the rest 
def extract_rnews_post_data(response_data):
    articles_data = []
    for i in range(len(response_data)):
        articles_data.append({
            'date_posted': response_data[i]["created_utc"],
            'reddit_title': response_data[i]["title"],
            'score': response_data[i]["score"],
            'url': response_data[i]["url"]
        })

    return articles_data

def request_posts():
    response = requests.get("https://api.pushshift.io/reddit/search/submission/?sort_type=score&subreddit=news&size=25")
    response_data = response.json()["data"]
    
    posts_data = extract_rnews_post_data(response_data)

    return get_article_urls(posts_data)

def main():
    request_posts()

if __name__ == "__main__":
    main()
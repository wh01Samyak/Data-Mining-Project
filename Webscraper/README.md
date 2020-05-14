Currently going to be using Scrappy.

It will use the pushshift api to get the urls. The crawler gets the title tag of the top 25 articles of all time in r/news.

<strong> To run crawler </strong>

```
scrapy crawl articles
```

<strong> Terminal command to create data.csv file with the headlines of the posts: </strong>

```
scrapy crawl articles -o data.csv
```

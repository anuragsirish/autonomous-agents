# filename: fetch_nvidia_news.py

import feedparser
import pytz
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Yahoo finance RSS url for Nvidia
yahoo_finance_rss_url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=NVDA&region=US&lang=en-US'

# Parse the RSS feed
feed = feedparser.parse(yahoo_finance_rss_url)

# Calculate the date a month ago (with timezone information)
a_month_ago = datetime.now(pytz.utc) - relativedelta(months=1)

# Filter and print articles from the past month
for entry in feed.entries:
    published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z')
    if published_date > a_month_ago:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published Date: {entry.published}")
        print("\n")
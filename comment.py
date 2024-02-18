import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_facebook_post_comments(post_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Make a request to get the HTML content of the Facebook post
    response = requests.get(post_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract comments from the HTML
    comments = [comment.text for comment in soup.find_all('span', class_='UFICommentBody')]

    return comments

# Replace 'your_post_url' with the URL of the Facebook post you want to scrape comments from
post_url = 'https://www.facebook.com/100087236305356/videos/learn-art-of-dying-from-bhismauttarayan-makarsakranti-cyberzeel/277025088399815/'
comments = scrape_facebook_post_comments(post_url)

# Create a DataFrame from the comments list
df = pd.DataFrame({'Comments': comments})

# Save the DataFrame to a CSV file
df.to_csv("facebook_comment.csv", index=False)

print("Comments saved to facebook_comments.csv")


# url: "https://www.amazon.com/HP-24mh-FHD-Monitor-Built/dp/B08BF4CZSV/ref=lp_16225007011_1_1"

# importing required library
import request
from bs4 import BeautifulSoup
import lxml

# requested url
url =  "https://www.amazon.com/HP-24mh-FHD-Monitor-Built/dp/B08BF4CZSV/ref=lp_16225007011_1_1"

#  find user agent and language.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Accept-Language": "en",

}
# get the request data
r = request.get(url, headers=headers)


# make beautifulSoup object and passing url text data with lxml parser.
soup = BeautifulSoup(r.text, "lxml")
print(soup.prettify())
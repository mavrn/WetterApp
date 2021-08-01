from bs4 import BeautifulSoup
import requests


def get_content_from_url(url):
    return BeautifulSoup(requests.get(url).content, "html.parser")

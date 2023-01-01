from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


class FromBaseURL(object):
    def __init__(self, base_url: str):
        self.base_url = base_url

        self.__github_urls = []
        self.__prepare_github_urls()

        self.urls = []
        self.__prepare_urls()

    def __prepare_urls(self):
        r = requests.get(self.base_url)
        soup = BeautifulSoup(r.content, "html.parser")

    def __prepare_github_urls(self):
        urls = [
            "topics",
            "features",
            "enterprise",
            "_graphql",
            "sponsors",
            "explore",
            "search"
        ]

        for i in range(len(urls)):
            urls[i] = "/{}/".format(urls[i])

        for url in urls:
            self.__github_urls.append("/{}/".format(url))

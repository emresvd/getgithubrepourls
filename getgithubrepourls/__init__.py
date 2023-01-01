from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


class RepoUrls(object):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.urls = []
        self.__github_urls = []
        self.__prepare_github_urls()
        self.__prepare_urls()

    def __prepare_urls(self):
        pass

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
            
        print(urls)

if __name__ == "__main__":
    repo_urls = RepoUrls("https://github.com/topics/python")

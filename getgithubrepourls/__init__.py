from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


class FromBaseURL(object):
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

        self.__github_urls = []
        self.urls = []

        self.__prepare_github_urls()
        self.__prepare_urls()

    def __prepare_urls(self):
        r = requests.get(self.base_url)
        soup = BeautifulSoup(r.content, "html.parser")

        for i in soup.prettify().splitlines():
            for j in i.split('"'):
                if j.startswith("http"):
                    new_url = j
                elif j.startswith("/"):
                    new_url = urljoin(self.base_url, j)
                else:
                    continue

                if self.__is_repo_url(new_url) and not new_url in self.urls:
                    self.urls.append(new_url)

    def __prepare_github_urls(self) -> None:
        urls = [
            "topics",
            "features",
            "enterprise",
            "_graphql",
            "sponsors",
            "explore",
            "search",
            "marketplace",
            "codespaces",
            "pricing",
            "collections",
            "settings",
            "contact",
        ]

        for url in urls:
            self.__github_urls.append("/{}/".format(url))

    def __is_repo_url(self, url: str) -> bool:
        if not url.startswith("https://github.com/"):
            return False

        if not url.count("/") == 4:
            return False

        for github_url in self.__github_urls:
            if github_url in url:
                return False

        return True


class TopicUrls(object):
    def __init__(self) -> None:
        self.urls = []
        self.__prepare_urls(
            [
                "https://github.com/topics",
                "https://github.com/explore",
            ]
        )

    def __prepare_urls(self, urls) -> None:
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")

            for i in soup.prettify().splitlines():
                for j in i.split('"'):
                    if j.startswith("/"):
                        new_url = urljoin(url, j)
                    else:
                        continue

                    if "/topics/" in new_url and not new_url in self.urls:
                        self.urls.append(new_url)


class CollectionUrls(object):
    def __init__(self) -> None:
        self.urls = []
        self.__prepare_urls(
            [
                "https://github.com/collections",
            ]
        )

    def __prepare_urls(self, urls) -> None:
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")

            for i in soup.prettify().splitlines():
                for j in i.split('"'):
                    if j.startswith("/"):
                        new_url = urljoin(url, j)
                    else:
                        continue

                    if "/collections/" in new_url and not new_url in self.urls:
                        self.urls.append(new_url)


class FromExplore(FromBaseURL):
    def __init__(self) -> None:
        super().__init__("https://github.com/explore")


class FromCollections(CollectionUrls):
    def __init__(self) -> None:
        super().__init__()
        self.collection_urls = self.urls
        self.urls = []
        self.__prepare_urls_()

    def __prepare_urls_(self) -> None:
        for url in self.collection_urls:
            fromBaseURL = FromBaseURL(url)
            self.urls += fromBaseURL.urls


class FromTopics(TopicUrls):
    def __init__(self) -> None:
        super().__init__()
        self.topic_urls = self.urls
        self.urls = []
        self.__prepare_urls_()

    def __prepare_urls_(self) -> None:
        for url in self.topic_urls:
            fromBaseURL = FromBaseURL(url)
            self.urls += fromBaseURL.urls


class FromUser(FromBaseURL):
    def __init__(self, username: str) -> None:
        super().__init__("https://github.com/{}?tab=repositories".format(username))


class UserUrls(object):
    def __init__(self) -> None:
        self.urls = []
        self.__prepare_urls(
            [
                "",
            ]
        )

    def __prepare_urls(self, urls) -> None:
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")

            for i in soup.prettify().splitlines():
                for j in i.split('"'):
                    if j.startswith("/"):
                        new_url = urljoin(url, j)
                    else:
                        continue

                    if new_url.count("/") == 3 and not new_url in self.urls:
                        self.urls.append(new_url)

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

class RepoUrls(object):
    def __init__(self, base_url:str):
        self.base_url = base_url
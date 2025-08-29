from functools import cached_property

import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class WebPage:
    def __init__(self, url):
        self.url = url

    def __str__(self):
        return f"🌐 {self.url}"

    @cached_property
    def html(self):
        response = requests.get(self.url, timeout=120, verify=False)
        if response.status_code == 200:
            return response.text
        raise ValueError(
            f"[{self}] Failed to fetch HTML: {response.status_code}"
        )

    @cached_property
    def soup(self):

        return BeautifulSoup(self.html, "html.parser")

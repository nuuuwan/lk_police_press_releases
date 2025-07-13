import os
import tempfile
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from utils import File, Hash, Log

log = Log('WebPage')


class WebPage:
    def __init__(self, url):
        self.url = url

    @property
    def hash(self):
        return Hash.md5(self.url)[:8]

    @property
    def temp_html_path(self):
        return os.path.join(tempfile.gettempdir(), f'{self.hash}')

    @property
    def html_content_hot(self):
        response = requests.get(self.url, verify=False)
        log.debug(f'🌐 {self.url} {response.status_code}')
        return response.text

    @property
    def html_content(self):
        if not os.path.exists(self.temp_html_path):
            html_content = self.html_content_hot
            log.debug(f'Wrote ➡️ {self.temp_html_path}')
            File(self.temp_html_path).write(html_content)
        else:
            log.debug(f'Read ⬅️ {self.temp_html_path}')
            html_content = File(self.temp_html_path).read()
        return html_content

    @property
    def base_url(self):
        parsed_url = urlparse(self.url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}"

    @property
    def soup(self):
        return BeautifulSoup(self.html_content, 'html.parser')

    def gen_neighbours(self):
        a_list = self.soup.find_all('a')
        url_set = set()
        for a in a_list:
            url = a.get('href')
            if self.base_url not in url:
                continue
            if url not in url_set:
                url_set.add(url)
                yield WebPage(url)

    def gen_pdfs(self):
        for page in self.gen_neighbours():
            if page.url.endswith('.pdf'):
                yield page

    def gen_pdfs_recursive(self):  # noqa: C901
        queue = [self]
        visited = set()
        while queue:
            current_page = queue.pop(0)
            log.debug(f'🕷️ Visiting: {current_page.url}')
            visited.add(current_page.url)
            pdf_set = set()
            for pdf_page in current_page.gen_pdfs():
                if pdf_page.url not in pdf_set:
                    pdf_set.add(pdf_page.url)
                    yield pdf_page

            for neighbour in current_page.gen_neighbours():
                if (
                    not neighbour.url.endswith('.pdf')
                    and neighbour.url not in visited
                ):
                    queue.append(neighbour)
        log.debug('🛑 All PDF pages have been visited.')

    def download_binary(self, binary_path):
        response = requests.get(self.url, verify=False)
        if response.status_code == 200:
            with open(binary_path, 'wb') as f:
                f.write(response.content)
            file_size_k = len(response.content) / 1000
            log.debug(f'Wrote {binary_path} ({file_size_k:.1f} KB)')
        else:
            log.error(
                f'Failed to download {self.url} - {response.status_code}'
            )

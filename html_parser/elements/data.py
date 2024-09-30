from bs4 import BeautifulSoup

from html_parser.elements.folder import HTMLFolders

from typing import List


class HTMLFolderData(HTMLFolders):
    data = []
    url = {}
    keys = ['loc', 'lastmod', 'changefreq', 'priority']

    def find_element(self, folder, key: str) -> None:
        element = folder.find('span', string=lambda text: text and key in text)
        if element:
            self.url[key] = element.find_next_sibling('span').text

    def get(self) -> List[dict]:
        folders = self.folders()
        for folder in folders:
            for key in self.keys:
                self.find_element(
                    folder=folder,
                    key=key
                )
            self.data.append(self.url)
        return self.data

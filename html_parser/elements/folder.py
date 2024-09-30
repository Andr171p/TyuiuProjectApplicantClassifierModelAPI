from bs4 import BeautifulSoup

from typing import List


class HTMLFolders:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.__soup = soup

    def folders(self) -> List[str]:
        folders = self.__soup.find_all(
            name='div',
            attrs={
                'class': 'folder'
            }
        )
        return folders

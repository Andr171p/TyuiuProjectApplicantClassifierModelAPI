from bs4 import BeautifulSoup


class HTMLSoup:
    def __init__(self, html: str) -> None:
        self.__html = html

    def soup(self) -> BeautifulSoup:
        soup = BeautifulSoup(
            self.__html,
            features="html.parser"
        )
        return soup

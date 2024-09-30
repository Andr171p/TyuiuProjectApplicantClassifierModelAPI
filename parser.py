from webdriver.session import ChromeSession

from html_parser.soup import HTMLSoup
from html_parser.elements.data import HTMLFolderData


class Parser(ChromeSession):
    def parse(self) -> dict:
        self.open(url="https://quackr.io/sitemap.xml")
        html = self.html()
        self.close()
        soup = HTMLSoup(html=html).soup()
        data = HTMLFolderData(soup=soup).get()
        return data


parser = Parser()
data = parser.parse()
print(data)
import time

from webdriver.driver import ChromeWebDriver

from loguru import logger


class ChromeSession(ChromeWebDriver):
    @classmethod
    def open(cls, url: str, timeout: int = 5) -> None:
        cls.driver.get(url=url)
        time.sleep(timeout)
        logger.info("Страница успешно открыта...")

    @classmethod
    def wait(cls, timeout: int = 5) -> None:
        cls.driver.implicitly_wait(timeout)

    @classmethod
    def html(cls) -> str:
        element = cls.driver.find_element(by="xpath", value="//*")
        html = element.get_attribute("outerHTML")
        return html

    @classmethod
    def close(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

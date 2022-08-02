import telegraph as _tgph
from typing import Optional, Any


class Postman:
    def __init__(self, header: str, post: str, username: str = 'Anonymous', author_name: str = None,
                 author_url: str = None, ):
        self.__postman = _tgph.Telegraph()
        self.__postman.create_account(short_name=username, author_name=author_name, author_url=author_url)
        self.__post = post
        self.__post_header = header
        self.__pages: list = []
        self.__last_page: None | dict = None

    def publish(self) -> Optional[Any]:
        self.__last_page = self.__postman.create_page(title=self.__post_header, html_content=self.__post)
        self.__pages.append(self.__last_page)
        return self.__last_page

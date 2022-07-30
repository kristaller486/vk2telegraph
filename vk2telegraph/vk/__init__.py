import bs4 as _bs4
from . import backends as _backend
from copy import copy as _copy
# from loguru import logger as _logger
# import sys as _sys

# logger.add(sys.stderr)
# TODO обертывать ссылки в посте в тег <a>


class _Cleaner: # TODO: fix this
    def __init__(self, article: _bs4.BeautifulSoup):
        self.__html: _bs4.BeautifulSoup = _copy(article)
        self.__clean_html: str = self.__clean()

    @property
    def content(self):
        return self.__clean_html

    def __clean(self) -> str:
        html = _copy(self.__html)
        article = self.__html.find(class_='article')
        self.__process_images(article, self.__extract_hd_images(article))
        self.__remove_spans(article)
        self.__remove_divs(article)
        header: _bs4.BeautifulSoup = article.find('h1')
        header.decompose()
        result: str = ''
        for tag in article.contents:
            result += str(tag)
        result = self.__clean_html_symbols(result)
        return result

    def __remove_spans(self, article: _bs4.BeautifulSoup) -> None:
        for span in article.find_all('span'):
            span.decompose() # delete <span/>'s

    def __remove_divs(self, article: _bs4.BeautifulSoup) -> None:
        for div in article.find_all('div'): # delete all <div/>'s
            div.decompose()

    def __process_images(self, article, images: list):
            figures: list = article.find_all('figure')
            assert len(figures) == len(images), 'Figures or images list not valid :('
            for i, figure in enumerate(figures):
                figure.img.decompose()
                figure.append(_bs4.BeautifulSoup(f'<img src={images[i]} />', 'html.parser'))
            for figure, image in zip(figures, images):
                figure.div.replaceWith(image)

    def __extract_hd_images(self, article: _bs4.BeautifulSoup) -> list:
        """
        Extract high resolution images from data-sizes attr of div.
        """
        #TODO: Docs!
        size_divs: list[_bs4.BeautifulSoup] = article.find_all(class_='article_object_sizer_wrap')
        images: list[str] = []
        for div in size_divs:
            size = div.attrs['data-sizes']
            size = size.split(',"')[-1]
            size = size.replace('\\/', '/')
            size = size.replace('[', '')
            size = size.replace(']', '')
            size = size.replace('{', '')
            size = size.replace('}', '')
            size = size.split(',')
            size[0] = size[0].split(':"')[1]
            size[0] = size[0].replace('"', '')
            images.append(size[0])
        return images

    def __clean_html_symbols(self, html: str) -> str:
        """Fix src url (src="https://img.img/q=111&amp;w=222" -> src="https://img.img/q=111&w=222")"""
        return html.replace('&amp;', '&')


class VKPost:
    def __init__(self, url: str):
        html_post = _backend.get(url)
        self.__content: str = html_post
        self.__html = _bs4.BeautifulSoup(self.__content, 'html.parser')
        self.__header: str = self.__extract_header()
        self.__cleaner = _Cleaner(self.__html)
        self.__clean_content = self.__cleaner.content

    @property
    def dirty_content(self):
        """
        HTML content from VK post. Contain classes, divs and other dirt
        """
        return self.__content

    @property
    def clear_content(self):
        """
        Clear HTML content adapted for use in Telegra.ph
        """
        return self.__clean_content

    @property
    def content(self):
        """
        Same as clear_content
        """
        return self.__clean_content

    @property
    def header(self):
        return self.__header

    def __clean(self) -> str: # TODO: Refractor!
        """
        Removes from html all unnecessary
        """

    def __extract_header(self) -> str:
        """
        Extract header from html post
        """
        html = _copy(self.__html)
        article = html.find(class_='article')
        header = article.find('h1')
        return header.text

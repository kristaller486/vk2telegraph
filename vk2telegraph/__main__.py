import warnings
from fire import Fire
from .vk import VKPost
from .tgph import Postman


def go(url, author_name=None, author_url=None, force=False):
    if force:
        warnings.warn('Force mod is enabled, errors may occur')
    post = VKPost(url, force=force)
    postman = Postman(header=post.header, post=post.content, author_name=author_name, author_url=author_url)
    telegraph_page = postman.publish()
    telegraph_page_url = telegraph_page['url']
    return telegraph_page_url


if __name__ == '__main__':
    Fire(go)

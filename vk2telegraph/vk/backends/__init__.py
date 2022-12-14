import requests as _requests
import fake_useragent as _fake_useragent


def _is_valid_url(url: str) -> bool:
    if 'vk.com/@' in url:
        return True
    return False


def get(url: str, force: bool) -> str:
    user_agent = _fake_useragent.UserAgent()
    if not _is_valid_url(url) and not force:
        raise ValueError('URL "{url}" not contain VK article')
    request = _requests.get(url, headers={'User-Agent': user_agent.random})
    assert request.status_code == 200, f'Error, status code not 200, but {request.status_code}'
    post = request.text
    return post

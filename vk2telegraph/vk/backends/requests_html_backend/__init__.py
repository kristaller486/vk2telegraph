import requests as _rq

def _is_valid_url(url: str) -> bool:
    if 'vk.com/@' not in url:
        return False
    return True
    
def get(url: str) -> str:
    if not _is_valid_url(url):
        raise ValueError('URL "{url}" not contain VK article')
    with _rq.Session() as session:
        post = session.get(url)
    return post.text
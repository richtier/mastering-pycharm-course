from typing import List
import urllib.parse
import requests


# TODO: Make faster by using @functools.lru_cache() ?
def search(text: str) -> List[str]:
    url = build_url(text)
    response = perform_search(url)
    return convert_results(response)


def build_url(text):
    # format is https://search.talkpython.fm/api/search?q=SEARCH

    encoded = urllib.parse.urlencode({'q': text})
    return 'https://search.talkpython.fm/api/search?{}'.format(encoded)


def perform_search(url):
    resp = requests.get(url)
    resp.raise_for_status()

    return resp


def convert_results(response):
    data = response.json()
    return [
        d.get('description')
        for d in data.get('results')
    ]

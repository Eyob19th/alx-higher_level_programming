#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status and displays the body of the response.
"""

import urllib.request


def fetch_status(url: str) -> str:
    """
    Fetches the status of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        The response body as a string.
    """
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        return body.strip()


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    body = fetch_status(url)
    print('- type: {}'.format(type(body)))
    print('- content: {}'.format(body))

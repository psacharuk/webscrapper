import requests
from requests.exceptions import ConnectionError, MissingSchema, InvalidSchema

def get_page(url):
    url = prepare_url(url)
    error_info = None
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.url, response.text, error_info
    except ConnectionError as error:
        error_info = str(error)
    except MissingSchema as error:
        error_info = str(error)
    except InvalidSchema as error:
        error_info = str(error)
    return None, None, error_info

def prepare_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = f"http://{url}"
    return url
import requests


class HTTP:
    @classmethod
    def http_get(cls, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return False
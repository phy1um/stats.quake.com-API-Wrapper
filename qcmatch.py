import requests
from api import api_path
from types import SimpleNamespace


class QCMatch(object):

    @staticmethod
    def from_id(uuid):
        query = requests.get(api_path("Player/Games", {"id": uuid}))
        if query.status_code != 200:
            raise Exception("Failed to get API resource")
        else:
            data = query.json()
            return QCMatch(data)

    def __init__(self, data):
        self.model = SimpleNamespace(**data)
    
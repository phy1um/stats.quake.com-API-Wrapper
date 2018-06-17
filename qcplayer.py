import requests
from api import api_path
from types import SimpleNamespace
from qcrating import QCRating


class QCPlayer(object):
    @staticmethod
    def exists(name):
        query = requests.get(api_path("Player/Search", {"term": name}))
        if query.status_code != 200:
            raise Exception("Could not get API resource")
        else:
            data = query.json()
            for match in data:
                if match["entityName"] == name:
                    return True
            return False

    @staticmethod
    def from_name(name):
        query = requests.get(api_path("Player/Stats", {"name": name}))
        if query.status_code != 200:
            raise Exception("Could not get API resource")
        data = query.json()
        return QCPlayer(data)

    def __init__(self, model):
        self.model = SimpleNamespace(**model)

    def get_rank_data(self, mode):
        return QCRating(mode, self.model.playerRatings[mode])

    def get_rank(self, mode):
        return self.model.playerRatings[mode]["rating"]

    def get_icon(self):
        return self.model.namePlateId

    def get_nameplate(self):
        return self.model.iconId

    def get_level(self):
        return self.model.playerLevelState["level"]

    def get_experience(self):
        return self.model.playerLevelState["exp"]

    def iterate_matches(self):
        for m in self.model.matches:
            yield SimpleNamespace(**m)

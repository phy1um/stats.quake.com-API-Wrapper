import requests
from api import api_path
from types import SimpleNamespace


class QCMatch(object):
    """Data for a single match, identified by UUID and optionally player name
    TODO: Document fields...
    """

    @staticmethod
    def from_id(uuid):
        """Make QCMatch from an id
        Args:
            uuid: identifier of game (obtained from Player/MatchSummary)
        
        Returns:
            QCMatch object for given uuid

        Raises:
            Exception: on request failure (catch-all)
        """
        query = requests.get(api_path("Player/Games", {"id": uuid}))
        if query.status_code != 200:
            # what kind of exception should this be???
            raise Exception("Failed to get API resource")
        if query.headers["content-type"] == "text/html":
            # no match with ID exists
            raise ValueError("Invalid match ID: {}".format(uuid))
        else:
            data = query.json()
            return QCMatch(data)

    def __init__(self, data):
        """Make a namespace from json data for QC match data
        Do not call this directly, use the static from_id() instead!
        """
        self.model = SimpleNamespace(**data)

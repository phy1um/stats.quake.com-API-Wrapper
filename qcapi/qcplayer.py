import requests
from .api import api_path
from types import SimpleNamespace
from .qcrating import QCRating


class QCPlayer(object):
    """Represents QC player data
    TODO: document fields!
    """

    @staticmethod
    def exists(name):
        """Test existence of player from name

        Args:
            name: name of player to test
        
        Returns:
            True if player with name exists else False

        Raises:
            Exception: on failed request (status code != 200)
            JSONDecodeError: could not get valid JSON from request (can
             indicate issues on stats.quake.com)
        """
        query = requests.get(api_path("Player/Search", {"term": name}))
        if query.status_code != 200:
            raise Exception("Could not get API resource")
        else:
            data = query.json()
            for match in data:
                # resource has array of matches _containing_ given name, we
                #  test for an exact match
                if match["entityName"] == name:
                    return True
            return False

    @staticmethod
    def from_name(name):
        """Make a player object from name

        Args:
            name: name of player

        Returns:
            QCPlayer object for name

        Raises:
            Exception: on failed request
            ValueError: no player with name exists
            JSONDecodeError: could not get valid JSON from response
        """
        query = requests.get(api_path("Player/Stats", {"name": name}))
        if query.status_code != 200:
            raise Exception("Could not get API resource")
        if query.headers["content-type"] == "text/html":
            raise ValueError("No player with name known")
        data = query.json()
        return QCPlayer(data)

    def __init__(self, model):
        self.model = SimpleNamespace(**model)

    def get_rank_data(self, mode):
        """Get player rating data for a specific mode

        Args:
            mode: code for game mode (eg duel, tdm)

        Returns:
            QCRating data for mode
        """
        return QCRating(mode, self.model.playerRatings[mode])

    def get_rank_value(self, mode):
        """Get single rating number for player in mode

        Args:
            mode: code for game mode (eg duel, tdm)

        Returns:
            Numeric rating "elo" value
        """
        return self.model.playerRatings[mode]["rating"]

    def get_icon_name(self):
        """Get player's icon name
        """
        return self.model.namePlateId

    def get_nameplate_name(self):
        return self.model.iconId

    def get_level(self):
        """Get player's numeric profile level
        """
        return self.model.playerLevelState["level"]

    def get_experience(self):
        return self.model.playerLevelState["exp"]

    def iterate_matches(self):
        """Get iterator for match summaries
        """
        for m in self.model.matches:
            yield SimpleNamespace(**m)

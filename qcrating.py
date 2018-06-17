from types import SimpleNamespace


class QCRating(object):
    def __init__(self, mode, d):
        self.model = SimpleNamespace(**d)
        self.mode = mode

    def get_rating(self):
        return self.model.rating

    def get_deviation(self):
        return self.model.deviation

    def get_update_time(self):
        return self.model.lastUpdated

    def iterate_history(self):
        for m in self.model.history:
            yield SimpleNamespace(**m)

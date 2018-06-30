import requests
from api import api_path

"""functions for getting requests streams of image data
this can be wrapped using BytesIO(request.content), and this BytesIO object can
be opened easily in PIL, or manually processed
"""

base = "https://stats.quake.com/{}/{}.{}"


def _get_resource_bytes(path, name, ext):
    return requests.get(base.format(path, name, ext))


def get_icon_bytes(name):
    return _get_resource_bytes("icons", name, "png")


def get_weapon_icon_bytes(name):
    return _get_resource_bytes("weapons", name, "png")


def get_nameplate_bytes(name):
    return _get_resource_bytes("nameplates", name, "png")


def get_champion_portrait_bytes(name):
    return _get_resource_bytes("champions", name, "png")


def get_map_portrait_bytes(name):
    return _get_resource_bytes("maps", name, "jpg")


def get_medal_bytes(name):
    return _get_resource_bytes("medals", name, "png")

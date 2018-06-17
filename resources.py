import requests
from api import api_path


def _get_resource_bytes(path, name):
    return requests.get(api_path("{}/{}.png".format(path, name)))


def get_icon_bytes(name):
    return _get_resource_bytes("icons", name)


def get_weapon_icon_bytes(name):
    return _get_resource_bytes("weapons", name)


def get_nameplate_bytes(name):
    return _get_resource_bytes("nameplates", name)


def get_champion_portrait_bytes(name):
    return _get_resource_bytes("champions", name)


def get_map_portrait_bytes(name):
    return _get_resource_bytes("maps", name)


def get_medal_bytes(name):
    return _get_resource_bytes("medals", name)


champion_names = ["NYX", "SCALEBEARER", "ANARKI", "SLASH", "CLUTCH",
                  "GALENA", "RANGER", "VISOR", "SORLAG", "BJ", "DOOM", "KEEL", 
                  "STROGG"]

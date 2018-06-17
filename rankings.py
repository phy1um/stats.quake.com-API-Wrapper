
_table = {
    2100: "Elite_01",
    2025: "Diamond_05",
    1950: "Diamond_04",
    1875: "Diamond_03",
    1800: "Diamond_02",
    1725: "Diamond_01",
    1650: "Gold_05",
    1575: "Gold_04",
    1500: "Gold_03",
    1425: "Gold_02",
    1350: "Gold_01",
    1275: "Silver_05",
    1200: "Silver_04",
    1125: "Silver_03",
    1050: "Silver_02",
    975: "Silver_01",
    900: "Bronze_05",
    825: "Bronze_04",
    750: "Bronze_03",
    675: "Bronze_02",
    0: "Bronze_01"
}

def get_rank_name(rank):
        for value in _table:
            if rank >= value:
                return _table[value]
        return "Zero_01"



base_url = "https://stats.quake.com/api/v2/"


def api_path(path, query_dict=None):
    query = ""
    if query_dict is not None:
        query_arr = []
        for key in query_dict:
            query_arr.append("{}:{}".format(key, query_dict[key]))
        query = "?" + "&".join(query_arr)
    return "{}{}{}".format(base_url, path, query)

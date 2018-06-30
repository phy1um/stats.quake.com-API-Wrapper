
"""=== Quake Champions API wrapper ===
api.py: base wrapper for getting API paths
"""

# using API version 2
base_url = "https://stats.quake.com/api/v2/"


def api_path(path, query_dict=None):
    """Turn a relative API path into a full resource URL

    Args:
        path: This is the relative path, eg /Resource/Path
        query_dict(optional): key:value pairs are appended to the URL a query

    Returns:
        A string URL that can be used to make QC API requests.
    """
    query = ""
    if query_dict is not None:
        query_arr = []
        for key in query_dict:
            query_arr.append("{}={}".format(key, query_dict[key]))
        query = "?" + "&".join(query_arr)
    return "{}{}{}".format(base_url, path, query)

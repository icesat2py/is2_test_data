import earthaccess as ea

'''
FILE PURPOSE:
obtain a single granule of each data product
'''

"""
Tasks:
- set up credentials in GH repo
- figure out how to get an ATL11 file
- see if QL products are available via earthaccess (or icepyx); currently no results from either, even with virtually no bounds
- create script to get vars from file (use icepyx Vars module) and output to a reference file
- from icepyx, get the vars from the file created herein

then...
- set up an action to run this on a cron every so often
    - include a check for changes in version/file to avoid downloading when the file hasn't changed?


"""

######## Product parameters to get #######
# ATL01, ATL02, ATL04 are not included
products = [
            "ATL03",
            "ATL06",
            "ATL07",
            # # "ATL07QL",
            # "ATL08",
            # "ATL09",
            # # "ATL09QL",
            # "ATL10",
            # # "ATL11",
            # "ATL12",
            # "ATL13",
            # "ATL14",
            # "ATL15",
            # "ATL16",
            # "ATL17",
            # "ATL19",
            # "ATL20",
            # "ATL21",
            # "ATL23",
            ]


def download_single_product(product, spatial, temporal):
    """
    Download data for a single product
    """

    query = ea.search_data(
    short_name=product,
    bounding_box=tuple(spatial),
    temporal=tuple(temporal),
    count=1
    )

    print(product)
    print(len(query))

    ea.login(strategy="netrc")
    ea.download(query, "./data")
    

def get_data():
    
    spatial = [-55, 68, -48, 71]
    temporal = ['2019-02-20','2019-02-28']

    for prod in products:
        download_single_product(prod, spatial, temporal)


if __name__ == '__main__':
    get_data()

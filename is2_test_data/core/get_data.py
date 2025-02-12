import icepyx as ipx

'''
FILE PURPOSE:
obtain a single granule of each data product
'''

"""
Tasks:
- set up credentials in GH repo
- fill in space/time for each product
- switch to earthaccess?
- download only first granule
- create script to get vars from file (use icepyx Vars module) and output to a reference file
- from icepyx, get the vars from the file created herein

then...
- set up an action to run this on a cron every so often
    - include a check for changes in version/file to avoid downloading when the file hasn't changed?


"""

######## Product parameters to get #######
# key=product_shortname; values=tuple([spatial],[temporal])
# ATL01, ATL02, ATL04 are not included
product_params = {
    # "ATL03" : (),
    "ATL06" : ([-55, 68, -48, 71],['2019-02-20','2019-02-28']),
    # "ATL07" : (),
    # "ATL07QL" : (),
    # "ATL08" : (),
    # "ATL09" : (),
    # "ATL09QL" : (),
    # "ATL10" : (),
    # "ATL11" : ([-28.0, 62.0, -10.0, 68.0], []), #tracks=["1358"]),  # Get one specific track only; region is Iceland
    # "ATL12" : (),
    # "ATL13" : (),
    # "ATL14" : (),
    "ATL15" : ([-17.25, 80.7, -16.0, 81.0], ['2018-09-15', '2023-03-02']),
    # "ATL16" : (),
    # "ATL17" : (),
    # "ATL19" : (),
    # "ATL20" : (),
    # "ATL21" : (),
    # "ATL23" : (),
}


def download_single_product(product, spatial, temporal):
    """
    Download data for a single product

    Args:
        product (str): _description_
        spatial (_type_): _description_
        temporal (_type_): _description_
    """

    query = ipx.Query(
    product,
    spatial,
    temporal
    )

    print(product)
    print(len(query.avail_granules()))
    
    #TODO: only download the first granule
    #TODO: consider using earthaccess directly?

    # query.download_granules("./data", subset=False)


def get_data():

    for prod,params in product_params:
        download_single_product(prod, params[0], params[1])

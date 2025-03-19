import earthaccess as ea
import is2_data_ops
'''
FILE PURPOSE:
obtain a single granule of each data product
'''

"""
Tasks:
- figure out how to get an ATL11 file
- set up reference script with the list of products (currently prod_list.py, see icepyx url file)
X- add in functionality to update the vars dicts whenever a new file is run for that product
- docstrings and run code
- add typing

- from icepyx, get the vars from the file created herein


open as issues for future work:
- set up an action to run this on a cron every so often
- check for changes in version/file to avoid downloading when the file hasn't changed
- make sure that no data gets saved, but we can download a granule and use it to get vars or do test as needed
- provide variables info for QL products (currently they're not available via icepyx or earthaccess)

"""

ops = is2_data_ops.IS2_DataOps()
ops.update_vars_dict()


# ######## Product parameters to get #######
# # ATL01, ATL02, ATL04 are not included
# products = [
#             "ATL03",
#             "ATL06",
#             "ATL07",
#             # # "ATL07QL",
#             # "ATL08",
#             # "ATL09",
#             # # "ATL09QL",
#             # "ATL10",
#             # # "ATL11",
#             # "ATL12",
#             # "ATL13",
#             # "ATL14",
#             # "ATL15",
#             # "ATL16",
#             # "ATL17",
#             # "ATL19",
#             # "ATL20",
#             # "ATL21",
#             # "ATL23",
#             ]


# def download_single_product(product, spatial, temporal):
#     """
#     Download data for a single product
#     """

#     query = ea.search_data(
#     short_name=product,
#     bounding_box=tuple(spatial),
#     temporal=tuple(temporal),
#     count=1
#     )

#     print(product)
#     print(len(query))

#     ea.login(strategy="netrc")
#     ea.download(query, "./is2_test_data/data")
    

# def get_data():
    
#     spatial = [-55, 68, -48, 71]
#     temporal = ['2019-02-20','2019-02-28']

#     for prod in products:
#         download_single_product(prod, spatial, temporal)


# if __name__ == '__main__':
#     get_data()

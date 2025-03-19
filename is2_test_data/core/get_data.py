import is2_data_ops

"""
Tasks:
- figure out how to get an ATL11 file
- run code
- from icepyx, get the vars from the file created herein


open as issues for future work:
- set up an action to run this on a cron every so often
- check for changes in version/file to avoid downloading when the file hasn't changed
- make sure that no data gets saved, but we can download a granule and use it to get vars or do test as needed
- provide variables info for QL products (currently they're not available via icepyx or earthaccess)
- set up reference script with the list of products (versus manually hard-coding)?

"""

ops = is2_data_ops.IS2_DataOps()
ops.update_vars_dict()


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
    # "ATL09QL" : ([-180,-90, 180,90],['2018-09-15', '2025-03-02']),
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
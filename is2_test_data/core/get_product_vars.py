import is2_data_ops

"""
Simply run this script, with no products specified in the first line,
to create/update the json of variables for all data products.
If only certain products need updating, first modify the first line
to list the products you want updated.

Tasks:
- figure out how to get an ATL11 file


"""
# get all products (except QLs, which don't work)
# ops = is2_data_ops.IS2_DataOps()

# get a list of specific products
ops = is2_data_ops.IS2_DataOps(products=["ATL11"])

# update the product dictionary for all products specified above
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
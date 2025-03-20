import is2_data_ops

"""
Simply run this script, with no products specified in the first line,
to create/update the json of variables for all data products.
If only certain products need updating, first modify the first line
to list the products you want updated.

"""
# get all products (except QLs, which don't work)
ops = is2_data_ops.IS2_DataOps()

# get a list of specific products
# ops = is2_data_ops.IS2_DataOps(products=["ATL11"])

# update the product dictionary for all products specified above
ops.update_vars_dict()
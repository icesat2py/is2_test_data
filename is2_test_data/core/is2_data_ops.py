"""
ICESat-2 data operations
"""
import json
import pathlib

import earthaccess as ea
import icepyx as ipx
from icepyx.core.types import (
    ICESat2ProductShortName,
)


class IS2_DataOps:
    """
    Data object to navigate ICESat-2 products for variable lists and testing.

    Parameters
    ----------  
    products : List(string)
        ICESat-2 data product IDs, also known as "short name" (e.g. ATL03).
        Available data products can be found at: https://nsidc.org/data/icesat-2/data-sets

    Returns
    -------
    IS2_DataOps object

    Examples
    --------
    For a single product
    >>> IS2_DataOps(products=["ATL12"]) # doctest: +SKIP

    Operating on all ICESat-2 products
    >>> IS2_DataOps() # doctest: +SKIP

    """

    # ----------------------------------------------------------------------
    # Constructors

    def __init__(
        self,
        products: ICESat2ProductShortName = None,
        
    ):

        # set up the data paths
        self.jsonfile = pathlib.PosixPath(__file__).parent.joinpath("../data/is2variables.json").resolve()
        self.data_path = pathlib.PosixPath(__file__).parent.joinpath("../data/").resolve()

        # read in the existing dict of variables
        try:
            self.open_vars_json()
        except FileNotFoundError:
            self.vars_dict = {}

        if products is None:
            ######## Products to get #######
            # ATL01, ATL02, ATL04, and QLs are not included
            self.products = [
                "ATL03",
                "ATL06",
                "ATL07",
                # "ATL07QL",
                "ATL08",
                "ATL09",
                # "ATL09QL",
                "ATL10",
                # "ATL11",
                "ATL12",
                "ATL13",
                "ATL14",
                "ATL15",
                "ATL16",
                "ATL17",
                "ATL19",
                "ATL20",
                "ATL21",
                "ATL23",
                ]
        else:
            self.products = products


    
    def open_vars_json(self) -> None:
        """
        opens the json containing products and the list of variables for each,
        reading it into a dictionary
        """

        with self.jsonfile.open('r') as json_file:
            self.vars_dict = json.load(json_file)


    def save_vars_json(self) -> None:
        """
        saves the current `vars_dict` attribute to the data/is2variables.json file
        """

        with self.jsonfile.open('w') as json_file:
            json.dump(self.vars_dict, json_file)


    def download_single_product(
        self, 
        prod: ICESat2ProductShortName, 
        spatial: list[float | int], 
        temporal: list[str]
        ) -> None:
        """
        Download data for a single product using earthaccess

        Parameters
        ----------
        prod : string
            ICESat-2 data product ID, also known as "short name" (e.g. ATL03).
            Available data products can be found at: https://nsidc.org/data/icesat-2/data-sets

        spatial : list of floats
            The spatial extent as a list of coordinates in decimal degrees of [lower-left-longitude,
            lower-left-latitute, upper-right-longitude, upper-right-latitude]

        temporal: list of strings
            A list containing the string representation for the start and end dates formatted as "YYYY-MM-DD"

        Examples
        --------
        >>> IS2_DataOps(prod="ATL07", spatial=[-55, 68, -48, 71], temporal=['2019-02-20','2019-02-28']) # doctest: +SKIP
        downloads a single ATL07 granule
        """

        ea.login() # this HAS to be first, even though search doesn't need auth

        query = ea.search_data(
        short_name=prod,
        bounding_box=tuple(spatial),
        temporal=tuple(temporal),
        count=1
        )

        ea.download(query, self.data_path)
        

    def get_granule(self, prod: ICESat2ProductShortName) -> None:
        """
        Provide spatial and temporal parameters and call download function for the specified product

        Parameters
        ----------
        prod : string
            ICESat-2 data product ID, also known as "short name" (e.g. ATL03).
            Available data products can be found at: https://nsidc.org/data/icesat-2/data-sets

        """
        spatial = [-55, 68, -48, 71]
        temporal = ['2019-02-20','2019-02-28']

        self.download_single_product(prod, spatial, temporal)


    def get_vars(self, prod: ICESat2ProductShortName) -> list:
        """
        Get all available variables from granule using icepyx

        Parameters
        ----------
        prod : string
            ICESat-2 data product ID, also known as "short name" (e.g. ATL03).
            Available data products can be found at: https://nsidc.org/data/icesat-2/data-sets

        Returns
        -------
        available_variables : list
            List of strings of all available groups/paths and variables for that product.
        """

        #regex string format to combine path and product
        granule_path = ipx.core.read._parse_source(f"{self.data_path!s}/*{prod!s}*")
        print(granule_path)
        vars = ipx.Variables(path=granule_path[0])

        return vars.avail()


    def update_vars_dict(self) -> None:
        for prod in self.products:
            self.get_granule(prod)
            vars_list = self.get_vars(prod)
            if vars_list is not None:
                self.vars_dict[prod] = vars_list
        
        self.save_vars_json()
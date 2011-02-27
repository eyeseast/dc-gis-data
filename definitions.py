"""
Configuration describing the shapefiles to be loaded.
"""
from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

import utils

# This SHAPEFILES dictionary is a sample. You should delete (or comment out)
# the first entry if you don't care about neighborhoods in Chicago.
SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    #'Neighborhoods': {
    #    # Path to a shapefile, relative to /data
    #    'file': 'neighborhoods/Neighboorhoods.shp',
    #    # Generic singular name for an boundary of from this set
    #    'singular': 'Neighborhood',
    #    # Should the singular name come first when creating canonical identifiers for this set?
    #    # (e.g. True in this case would result in "Neighborhood South Austin" rather than "South Austin Neighborhood")
    #    'kind_first': False,
    #    # Function which each feature wall be passed to in order to extract its "external_id" property
    #    # The utils module contains several generic functions for doing this
    #    'ider': utils.simple_namer(['PRI_NEIGH_']),
    #    # Function which each feature will be passed to in order to extract its "name" property
    #    'namer': utils.simple_namer(['PRI_NEIGH']),
    #    # Authority that is responsible for the accuracy of this data
    #    'authority': 'City of Chicago',
    #    # Geographic extents which the boundary set encompasses
    #    'domain': 'Chicago',
    #    # Last time the source was checked for new data
    #    'last_updated': date(2010, 12, 12),
    #    # A url to the source of the data
    #    'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
    #    # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
    #    'notes': '',
    #    # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
    #    'encoding': ''
        # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
        # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
        #'srid': ''
    #},
    
    'Wards': {
        'file': 'Ward02Ply/Ward02Ply.shp',
        'singular': 'Ward',
        'kind_first': True,
        'ider': utils.simple_namer(['WARD_ID']),
        'namer': utils.simple_namer(['WARD_ID']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': 'http://data.dc.gov/Metadata.aspx?id=126',
        'notes': '',
        'encoding': '',
    },
    
    'Neighborhood Clusters': {
        'file': 'NbhClusPly/NbhClusPly.shp',
        'singular': 'Neighborhood Cluster',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NBH_NAMES']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': '',
        'notes': '',
        'encoding': '',
    },
    
    'ANC Districts': {
        'file': 'ANC02Ply/ANC02Ply.shp',
        'singular': 'ANC District',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': '',
        'notes': '',
        'encoding': '',
    },
    
    'Quadrants': {
        'file': 'DcQuadPly/DcQuadPly.shp',
        'singular': 'Quadrant',
        'kind_first': False,
        'ider': utils.simple_namer(['GIS_ID']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': '',
        'notes': '',
        'encoding': '',
    },
    
    'Census Block Groups': {
        'file': 'BlockGroupPly/BlockGroupPly.shp',
        'singular': 'Census Block Group',
        'kind_first': False,
        'ider': utils.simple_namer(['BLKGRP']),
        'namer': utils.simple_namer(['BLKGRP']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': '',
        'notes': '',
        'encoding': '',
    },
    
    'Census Tracts': {
        'file': 'TractPly/TractPly.shp',
        'singular': 'Census Tract',
        'kind_first': False,
        'ider': utils.simple_namer(['TRACT']),
        'namer': utils.simple_namer(['TRACT']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': '',
        'notes': '',
        'encoding': '',
    },
    
    'No Fly Zones': {
        'file': 'NoFlyZonePly/NoFlyZonePly.shp',
        'singular': 'No Fly Zone',
        'kind_first': False,
        'ider': utils.simple_namer(['NAME']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'DC Office of the Chief Technology Officer',
        'domain': 'Washington, DC',
        'last_updated': date(2011, 2, 26),
        'href': '',
        'notes': '',
        'encoding': '',
    },
    
}
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mguelcher
#
# Created:     05/12/2018
# Copyright:   (c) mguelcher 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
... mxd = arcpy.mapping.MapDocument("CURRENT")
... ###############Variables##################
... layerOne = "Inlets_6"
... layerTwo = "Manholes_6"
... layerThree = "Pipes_6"
... queryOne = "Muni = 'Girard Borough'"
... queryTwo = "Muni = 'Girard Borough'"
... queryThree = "Muni = 'Girard Borough'"
... ##########################################
... for lyr in arcpy.mapping.ListLayers(mxd):
...     if lyr.name == layerOne:
...         lyr.definitionQuery = queryOne
...     if lyr.name == layerTwo:
...         lyr.definitionQuery = queryTwo
...     if lyr.name == layerThree:
...         lyr.definitionQuery = queryThree

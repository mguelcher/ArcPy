#-------------------------------------------------------------------------------
# Name:        Print Number of Intersecting Features
# Purpose:     Prints number of features in the target layer that intersect each
#              feature of the source layer.
#
# Author:      mguelcher
#
# Created:     30/11/2018
# Copyright:   (c) mguelcher 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Rows in tuple returned in same order as listed in parameters
#with csr[0] being the first row in the tuple and the first field parameter.

import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")

##############Variables######################################
srcLyr = "Floodzone Parcels"
trgtLyr = "Floodzone Buildings"
fieldOne = 'Index'
fieldTwo = 'TaxPin'
csrParam = [fieldOne, fieldTwo]
csr = arcpy.da.SearchCursor(srcLyr, csrParam)
############################################################

for lyr in arcpy.mapping.ListLayers(mxd):
     if lyr.name == srcLyr:
         with csr as cursor:
            for row in cursor:
                lyr.definitionQuery = fieldTwo + "=" + "'" + str(csr[1]) + "'"
                arcpy.SelectLayerByLocation_management(trgtLyr,"INTERSECT",srcLyr)
                print str(csr[0]) + ',' + str(csr[1]) + ',' + str(arcpy.GetCount_management(trgtLyr)) + ','

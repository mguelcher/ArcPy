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
mxd = arcpy.mapping.MapDocument("CURRENT")
Bndry = "Watersheds"
inlet = "Inlets_11_1_1_1_6_1_2_1_1_10_1_1_1_1_1_1"
manhole = "Manholes_11_1_1_1_6_1_2_1_1_10_1_1_1_1_1_1"
outfall = "Outfalls_11_1_1_1_6_1_2_1_1_10_1_1_1_1_1_1"
asblts = "Asbuilt_Extent_11_1_1_1_6_1_2_1_1_10_1_1_1_1_1_1"
pipes = "Pipes_11_1_1_1_6_1_2_1_1_10_1_1_1_1_1_1"
fields = 'NAME'
csr = arcpy.da.SearchCursor(Bndry, fields)
for lyr in arcpy.mapping.ListLayers(mxd):
     if lyr.name == Bndry:
        print "Watershed1 " + "Watershed2 " + "Watershed3" + "Pipe-feet " + "Outfalls " + "As-builts " + "Inlets/Manholes"
        with csr as cursor:
            for row in cursor:
                lyr.definitionQuery = 'NAME = ' + "'" + str(csr[0]) + "'"
                #Get inlet count
                arcpy.SelectLayerByLocation_management(inlet,"INTERSECT",Bndry)
                inletResult = arcpy.GetCount_management(inlet)
                inletCount = int(inletResult.getOutput(0))
                #Get manhole count
                arcpy.SelectLayerByLocation_management(manhole,"INTERSECT",Bndry)
                manholeResult = arcpy.GetCount_management(manhole)
                manholeCount = int(manholeResult.getOutput(0))

                inltMnhlCnt = inletCount + manholeCount

                #Get outfall count
                arcpy.SelectLayerByLocation_management(outfall,"INTERSECT",Bndry)
                outfallCount = arcpy.GetCount_management(outfall)
                #Get as-built count
                arcpy.SelectLayerByLocation_management(asblts,"INTERSECT",Bndry)
                asbltsCount = arcpy.GetCount_management(asblts)
                #Get pipe-feet count
                    #No variable for the pipes field LengthFt as it's refd only twice and very short
                arcpy.SelectLayerByLocation_management(pipes,"INTERSECT",Bndry)
                arcpy.CalculateField_management(pipes, "LengthFt","!shape.length@feet!","PYTHON_9.3","#")
                pipeFtCnt = 0
                csr2 = arcpy.da.SearchCursor(pipes, "LengthFt")
                with csr2 as cursor:
                    for row in cursor:
                        pipeFtCnt = pipeFtCnt + csr2[0]

                #Print Results
                print str(csr[0]) + " " + str(pipeFtCnt) + " " + str(outfallCount) + " " + str(asbltsCount) + " " + str(inltMnhlCnt)
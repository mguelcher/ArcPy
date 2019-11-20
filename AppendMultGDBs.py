#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mguelcher
#
# Created:     28/05/2019
# Copyright:   (c) mguelcher 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
from arcpy import env
##Destination GDB
GDBD="C:\Users\mguelcher\Documents\ArcGIS\AppendTest\Final.gdb"
##List of Origin GDB
GDBS=["C:\Users\mguelcher\Documents\ArcGIS\AppendTest\NEWEST.gdb","C:\Users\mguelcher\Documents\ArcGIS\AppendTest\NEW.gdb","C:\Users\mguelcher\Documents\ArcGIS\AppendTest\NEWEST.gdb"]#,"...","<inputGDBN>"]
##Set Environment
arcpy.env.workspace=GDBD
##Get List of FDS
#FDS=arcpy.ListDatasets()
##Get List of Root Feature Classes
ROOTFCS=arcpy.ListFeatureClasses()

##Append elements in Root Feature Classes
for fcr in ROOTFCS:
    appendinput=[]
    for FCI in GDBS:
        appendinput.append(FCI+"/"+fcr)
    ##print appendinput
    arcpy.Append_management(appendinput,GDBD+'/'+fcr,"TEST")

##Append elements of Feature Classes inside Feature Datasets
#for FD in FDS:
    #for FC in arcpy.ListFeatureClasses("*","",FD):
        #appendinput2=[]
        #for FCI2 in GDBS:
                #appendinput2.append(FCI2+"/"+FC)
        ##print appendinput2
        #arcpy.Append_management(appendinput2,GDBD+'/'+FC,"TEST")

print "Done."
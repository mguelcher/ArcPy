#-------------------------------------------------------------------------------
# Name:        module1
# Purpose: writes number of repeats per value of a given field to a new fields
#
# Author:      panda (stack exchange)
#
# Created:     04/01/2019
# Copyright:
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
... mxd = arcpy.mapping.MapDocument("CURRENT")
... infeature="Pipes_7"
... field_in="created_date"
... field_out="COUNT_"+field_in
... #create the field for the count values
... arcpy.AddField_management(infeature,field_out,"SHORT")
... #creating the list with all the values in the field, including duplicates
... lista=[]
... cursor1=arcpy.SearchCursor(infeature)
... for row in cursor1:
...     i=row.getValue(field_in)
...     lista.append(i)
... del cursor1, row
... #updating the count field with the number on occurrences of field_in values
... #in the previously created list
... cursor2=arcpy.UpdateCursor(infeature)
... for row in cursor2:
...     i=row.getValue(field_in)
...     occ=lista.count(i)
...     row.setValue(field_out,occ)
...     cursor2.updateRow(row)
... del cursor2, row
... print ("Done.")
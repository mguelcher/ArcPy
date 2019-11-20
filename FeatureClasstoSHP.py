# Name: FeatureClassToShapefile_Example2.py
# Description: Use FeatureClassToGeodatabase to copy feature classes
#  to shapefiles

# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "\\ecfs01\Planning Shared\MSAP\GIS\Data\Geodatabases and Shapefiles\IncompatibilityFix"

# Set local variables
inFeatures = ["Outfalls", "Manholes", "Inlets", "Pipes", "Easements", "Culverts", "Channels", "Riprap", "Retention_Ponds",]
outLocation = r"C:\Users\mguelcher\Documents\ArcGIS\IncompatibilityFix"

# Execute FeatureClassToGeodatabase
arcpy.FeatureClassToShapefile_conversion(inFeatures, outLocation)

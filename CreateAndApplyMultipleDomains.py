# Name: MakeDomain.py
# Description: Create an attribute domain to constrain pipe material values. This is probably not the most efficient way to
# add domains at this scale but it's the best I can do

# Import system modules
import arcpy

# Set the workspace (to avoid having to type in the full path to the data
# every time)
arcpy.env.workspace = "C:\Users\mguelcher\Documents\ArcGIS"

# Set local parameters
gdb = "PythonDomainTest.gdb"



#Create Text Coded Value Domains
domainList = ["EASEMENT TYPE", "IMAGERY_TYPE", "LOCATED", "LOCATION SOURCE", "MS4 MUNICIPALITIES",
              "OWNERSHIP", "PIPES TYPE"]

for domain in domainList:


    if domain == domainList[0]:

        domName = domain

        inFeatures = "PythonDomainTest.gdb\Easements"
        inField = "TYPE"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {"DRN":"Drainage Easement", "SAN": "Sanitary Easement", "OTH": "Other", "UTIL": "Utility"}

        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary

        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

         #Process: Constrain the material value of distribution mains
        arcpy.AssignDomainToField_management(inFeatures, inField, domName)


    elif domain == domainList[1]:

        domName = domain

        inFeatures1 = "PythonDomainTest.gdb\Inlets"
        inFeatures2 = "PythonDomainTest.gdb\Manholes"
        inField = "Imagery_Type"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {"STV": "Streetview", "AER": "Aerials"}

        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary

        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

        # Process: Constrain the material value of distribution mains
        arcpy.AssignDomainToField_management(inFeatures1, inField, domName)
        arcpy.AssignDomainToField_management(inFeatures2, inField, domName)

    elif domain == domainList[2]:

        domName = domain

        inFeatures1 = "PythonDomainTest.gdb\Inlets"
        inFeatures2 = "PythonDomainTest.gdb\Manholes"
        inField = "LOCATED"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {"Y": "Yes", "N": "No"}

        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary

        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

         # Process: Constrain the material value of distribution mains

        arcpy.AssignDomainToField_management(inFeatures1, inField, domName)
        arcpy.AssignDomainToField_management(inFeatures2, inField, domName)


    elif domain == domainList[3]:

        domName = domain

        inFeatures1 = "PythonDomainTest.gdb\Inlets"
        inFeatures2 = "PythonDomainTest.gdb\Manholes"
        inField = "LOCATION_SOURCE"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {"ASB": "As-built Only", "IMG": "Imagery Only", "ABIM": "Both As-built and Imagery", "FLD": "Field"}

        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary

        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

        # Process: Constrain the material value of distribution mains

        arcpy.AssignDomainToField_management(inFeatures1, inField, domName)
        arcpy.AssignDomainToField_management(inFeatures2, inField, domName)


    elif domain == domainList[4]:

        domName = domain

        inFeatures = "PythonDomainTest.gdb\Pipes"
        inField = "Muni"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {"ERIE CITY": "ERIE CITY", "FAIRVIEW TWP": "FAIRVIEW TWP", "GIRARD BORO": "GIRARD BORO",
                   "GIRARD TWP": "GIRARD TWP", "HARBORCREEK TWP": "HARBORCREEK TWP", "LAKE CITY BORO": "LAKE CITY BORO",
                   "MCKEAN TWP": "MCKEAN TWP", "MILLCREEK TWP": "MILLCREEK TWP", "SUMMIT TWP": "SUMMIT TWP",
                   "WESLEYVILLE BORO": "WESLEYVILLE BORO", "UNION CITY BORO": "UNION CITY BORO"}


        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary


        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

        arcpy.AssignDomainToField_management(inFeatures, inField, domName)



    elif domain == domainList[5]:

        domName = domain

        inFeatures = "PythonDomainTest.gdb\Pipes"
        inField = "OWNERSHIP"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {"Private": "Private", "Municipal": "Municipal", "State": "State", "Federal": "Federal"}


        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary


        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

        arcpy.AssignDomainToField_management(inFeatures, inField, domName)


    elif domain == domainList[6]:

        domName = domain

        inFeatures = "PythonDomainTest.gdb\Pipes"
        inField = "TYPE"

        # Process: Create the coded value domain

        arcpy.CreateDomain_management(gdb, domName, "Created using python", "TEXT", "CODED")

        # Store all the domain values in a dictionary with the domain code as the "key"
        # and the domain description as the "value" (domDict[code])

        domDict = {'CI': 'CI', 'CLAY': 'CLAY', 'CMP': 'CMP', 'CONC': 'CONC', 'CPP': 'CPP', 'DIP': 'DIP',
                   'DNA': 'DATA NOT AVAILABLE', 'DST': 'DST', 'HDPE': 'HDPE', 'HIQ': 'HIQ', 'LF': 'LF',
                   'PCMP': 'PCMP', 'PVC': 'PVC', 'RCP': 'RCP', 'SC': 'SC', 'SPIRAL RIB': 'SPIRAL RIB',
                   'STEEL': 'STEEL', 'TILE': 'TILE', 'VC': 'VC', 'VIT': 'VIT'}


        # Process: Add valid material types to the domain
        # use a for loop to cycle through all the domain codes in the dictionary

        for code in domDict:
            arcpy.AddCodedValueToDomain_management(gdb, domain, code, domDict[code])

        arcpy.AssignDomainToField_management(inFeatures, inField, domName)





#Create Integer Coded Value Domain
domName = "PIPES_SIZE"

inFeatures = "PythonDomainTest.gdb\Pipes"
inField = "DIAMETER"

arcpy.CreateDomain_management(gdb, domName, "Created using python", "LONG", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key"
# and the domain description as the "value" (domDict[code])

domDict = {-1: 'Other, Arch', 0: 'Unknown', 4: '4"', 6: '6"', 8: '8"', 9: '9"', 10: '10"', 12: '12"', 14: '14"',
           15: '15"', 16: '16"', 18: '18"', 19: '19"', 20:'20"', 21: '21"', 22: '22"', 24: '24"',
           26: '26"', 27: '27"', 30: '30"', 33: '33"', 36: '36"', 39: '39"', 42: '42"', 45: '45"',
           48: '48"', 54: '54"', 57: '57"', 60: '60"', 66: '66"', 72: '72"', 78: '78"'}

for code in domDict:
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])


arcpy.AssignDomainToField_management(inFeatures, inField, domName)

print("Domain application successful!")
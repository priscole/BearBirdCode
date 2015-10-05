#import essential modules
import arcpy
import os
#set workspace
arcpy.env.workspace = r'C:\Student\PYTH\Running_scripts\Wilson.gdb'

#set variables for later use in functions and methods
#such as for listing feature classes
fc_list = arcpy.ListFeatureClass()

#opening print statement
print "Feature Classes in: " os.path.basename(arcpy.env.workspace)

#print out feature classes available in the workspace
for name in fc_list:
	print name

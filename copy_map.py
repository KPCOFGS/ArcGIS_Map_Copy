from arcgis.gis import GIS
import getpass

print("Please enter the source username")
src_user = input("> ")
print("Please enter the source password")
src_pass = sfcsdc
# Source GIS, URL stays the same
src_gis = GIS("https://www.arcgis.com", src_user, src_pass)

# Destination GIS, URL stays the same
dest_gis = GIS("https://www.arcgis.com", dest_user, dest_pass)

# ID of the map you want to copy
map_id = mapID

# Search for the map in the source GIS
src_item = src_gis.content.get(map_id)

# Copy the map to the destination GIS
dest_item = dest_gis.content.clone_items(items=[src_item])

print("Map copied successfully.")

from arcgis.gis import GIS

# Source GIS, URL stays the same
src_gis = GIS("https://www.arcgis.com", "SOURCE_ACCOUNT", "SOURCE_PASSWORD")

# Destination GIS, URL stays the same
dest_gis = GIS("https://www.arcgis.com", "DESTINATION_ACCOUNT", "DESTINATION_PASSWORD")

# ID of the map you want to copy
map_id = "MAP_ID"

# Search for the map in the source GIS
src_item = src_gis.content.get(map_id)

# Copy the map to the destination GIS
dest_item = dest_gis.content.clone_items(items=[src_item])

print("Map copied successfully.")

from arcgis.gis import GIS
import getpass

def create_gis_connection(account_label):
    print(f"---- {account_label} GIS Account ----")
    print("Please enter the ArcGIS Online organization URL.")
    print("For standard accounts, use: https://www.arcgis.com")
    print("For organizational accounts, use: https://your_org.maps.arcgis.com")
    url = input("> ").strip()

    print(f"Select the authentication method for the {account_label} account:")
    print("1. Username and Password")
    print("2. OAuth 2.0 (for SSO accounts)")
    print("3. ArcGIS Pro Authentication (uses the active portal in ArcGIS Pro)")
    auth_method = input("> ").strip()

    if auth_method == '1':
        # Username and Password authentication
        print(f"Please enter the {account_label} username:")
        username = input("> ").strip()
        print(f"Please enter the {account_label} password:")
        password = getpass.getpass("> ")
        try:
            gis = GIS(url, username, password)
            print(f"Logged in as: {gis.users.me.username}\n")
            return gis
        except Exception as e:
            print(f"\nFailed to log in to {url} with the provided credentials.")
            print(f"Error: {e}")
            exit()
    elif auth_method == '2':
        # OAuth 2.0 authentication
        print(f"Please enter the {account_label} client_id:")
        client_id = input("> ").strip()
        try:
            gis = GIS(url, client_id=client_id)
            print(f"Logged in as: {gis.users.me.username}\n")
            return gis
        except Exception as e:
            print(f"\nFailed to log in to {url} using OAuth 2.0 authentication.")
            print(f"Error: {e}")
            exit()
    elif auth_method == '3':
        # ArcGIS Pro authentication
        try:
            gis = GIS("pro")
            print(f"Logged in as: {gis.users.me.username}\n")
            return gis
        except Exception as e:
            print("\nFailed to log in using ArcGIS Pro authentication.")
            print(f"Error: {e}")
            exit()
    else:
        print("Invalid authentication method selected.")
        exit()

# Create source GIS connection
src_gis = create_gis_connection("Source")

# Create destination GIS connection
dest_gis = create_gis_connection("Destination")

print("Please enter the map ID to copy:")
map_id = input("> ").strip()

# Get the item from the source GIS
src_item = src_gis.content.get(map_id)

# Ensure the item exists
if src_item is None:
    print("\nThe specified map ID does not exist in the source GIS.")
    exit()

# Copy the map to the destination GIS
try:
    dest_item = dest_gis.content.clone_items(items=[src_item])
    print("\nMap copied successfully.")
except Exception as e:
    print(f"\nFailed to copy the map. Error: {e}")

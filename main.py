from google_images_search import GoogleImagesSearch
import json 

with open("keys.json", "r") as file:
    keys = json.load(file)


# Google API credentials
api_key = keys['api_key']
cx = keys['project_cx']

# Initialize GoogleImagesSearch object
gis = GoogleImagesSearch(api_key, cx)

with open("items.json", "r") as file:
    items = json.load(file)

fails = {
    "values": []
    }


#Could add minecraft wiki to it

for item in items["values"]:
    _search_params = {
        'q': item + ' item',
    }
    # Search and get the first image
    gis.search(search_params=_search_params, path_to_dir=f'C:/Users/hayde/Downloads/Random shit/imgs/', custom_image_name=_search_params['q'][10:])

    # Get the URL of the first image
    if len(gis.results()) == 0:
        print("Image Failed To Find: ", _search_params['q'])
        fails["values"].append(_search_params['q'])


with open("fails.json", "w") as file:
    json.dump(fails, file)
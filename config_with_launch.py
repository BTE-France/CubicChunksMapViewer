import json
import sys


def poiFilter(poi):
	if poi['id'] == 'poi':
		return poi['name']


location_file = sys.argv[3]
id = location_file.replace(".json", "")
with open(f"./locations/{location_file}", "r", encoding="utf-8") as file_json:
	json_dict = json.load(file_json)
worlds[json_dict["name"]] = f"./worlds/{id}"
print(f"Starting rendering for the {id} config file")
render = {}
render["world"] = json_dict["name"]
render["title"] = json_dict["name"]
render["manualpois"] = []
for marker_json in json_dict["markers"]:
	marker = {}
	marker["id"] = "poi"
	marker["x"] = marker_json["x"]
	marker["y"] = marker_json["y"] + 1040
	marker["z"] = marker_json["z"]
	marker["name"] = marker_json["name"]
	render["manualpois"].append(marker)
render["BTEcrop"] = []
for location_json in json_dict["locations"]:
	crop = (
		location_json["x_min"],
		location_json["z_min"],
		location_json["x_max"],
		location_json["z_max"]
	)
	render["BTEcrop"].append(crop)
render["markers"] = [dict(name="POIs", filterFunction=poiFilter, checked=True)]
render["rendermode"] = normal
render["showspawn"] = False
renders[id] = render

outputdir = "./outputs/ParisLyon"

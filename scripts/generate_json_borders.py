"""
Generate the coordinates of the borders of the French territory in the BTE projection.
The geographical data comes from https://github.com/gregoiredavid/france-geojson/blob/master/metropole-version-simplifiee.geojson
"""

import requests
import json

IN_PATH = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/metropole-version-simplifiee.geojson"
OUT_PATH = "./bte_france/borders.json"

borders_json = requests.get(IN_PATH).json()
out_borders = []
for _border in borders_json["geometry"]["coordinates"]:
    border = _border[0]  # Exclude "holes" within each border coordinates list

    in_coords = [f"geopos={lat},{lon}" for (lon, lat) in border]
    in_coords = [in_coords[i:i + 150] for i in range(0, len(in_coords), 150)]  # Split all the input coordinates into a list of lists of size 150

    out_coords = []
    for in_coord in in_coords:
        out_json = requests.get("https://smybteapi.thesmyler.fr/projection/fromGeo?" + "&".join(in_coord)).json()
        print(f"Borders generated: {out_json['success']}/{out_json['total']}")
        out_coords.extend([[int(x), int(y)] for (x, y) in out_json["mc_positions"]])  # Convert to int
    out_borders.append(out_coords)

with open(OUT_PATH, "w") as f:
    json.dump(out_borders, f, indent=2)

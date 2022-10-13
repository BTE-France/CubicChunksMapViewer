"""
Generate the coordinates of the borders of the French territory and its regions in the BTE projection.
The geographical data comes from https://github.com/gregoiredavid/france-geojson.
"""

import requests
import json


def convert_borders_to_mc(border: list[tuple[float, float]]) -> list[tuple[int, int]]:
    in_coords = [f"geopos={lat},{lon}" for (lon, lat) in border]
    in_coords = [in_coords[i:i + 150] for i in range(0, len(in_coords), 150)]  # Split all the input coordinates into a list of lists of size 150

    out_coords = []
    for in_coord in in_coords:
        out_json = requests.get("https://smybteapi.thesmyler.fr/projection/fromGeo?" + "&".join(in_coord)).json()
        print(f"Borders generated: {out_json['success']}/{out_json['total']}")
        out_coords.extend([[int(x), int(y)] for (x, y) in out_json["mc_positions"]])  # Convert to int

    return out_coords


def generate_national_borders():
    IN_PATH = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/metropole-version-simplifiee.geojson"
    OUT_PATH = "./bte_france/national_borders.json"

    print("Generating national borders...")
    borders_json = requests.get(IN_PATH).json()
    out_borders = []
    for _border in borders_json["geometry"]["coordinates"]:
        border = _border[0]  # Exclude "holes" within each border coordinates list
        out_borders.append(convert_borders_to_mc(border))

    with open(OUT_PATH, "w") as f:
        json.dump(out_borders, f, indent=2)


def generate_regional_borders():
    IN_PATH = "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-version-simplifiee.geojson"
    OUT_PATH = "./bte_france/regional_borders.json"

    print("Generating regional borders...")
    borders_json = requests.get(IN_PATH).json()
    out_borders = []
    for feature in borders_json["features"]:
        if feature["geometry"]["type"] == "Polygon":
            border = feature["geometry"]["coordinates"][0]
            out_borders.append(convert_borders_to_mc(border))

        elif feature["geometry"]["type"] == "MultiPolygon":
            for _border in feature["geometry"]["coordinates"]:
                border = _border[0]  # Exclude "holes" within each border coordinates list
                out_borders.append(convert_borders_to_mc(border))

    with open(OUT_PATH, "w") as f:
        json.dump(out_borders, f, indent=2)


if __name__ == "__main__":
    generate_national_borders()
    generate_regional_borders()

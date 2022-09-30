# BTE France Map Viewer

This project aims to create a web version of some locations of the BTE France Minecraft server.

The project uses a forked version of the [CubicChunks Overviewer](https://github.com/tossowski/CubicChunksMapViewer) and contains all images and data necessary to generate the map.

## Usage

To generate the map: ``python3 overviewer.py --config=config.py --forcerender``

To generate the markers: ``python3 overviewer.py --config=config.py --genpoi --skip-players --skip-scan``
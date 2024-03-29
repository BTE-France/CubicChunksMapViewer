from ..classes import Marker, Region, SquareLocation, Type

REGION = Region(
    id="stpm",
    name="Saint-Pierre-et-Miquelon",
    prefecture=Marker(name="Saint-Pierre-et-Miquelon - Saint-Pierre", x=-7473298, y=2, z=-7275856),
    locations=[
        SquareLocation(x1=-7473528, z1=-7275940, x2=-7473050, z2=-7276689),  # St-Pierre
        SquareLocation(x1=-7473852, z1=-7276865, x2=-7473244, z2=-7277554),
    ],
    markers=[
        Marker(name="Port de Saint-Pierre", x=-7473195, y=3, z=-7276375, type=Type.PORT),
    ]
)

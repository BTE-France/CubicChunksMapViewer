from ..classes import Region, Marker, SquareLocation, Type

REGION = Region(
    id="na",
    name="Nouvelle-Aquitaine",
    prefecture=Marker(name="Nouvelle-Aquitaine - Bordeaux", x=2473266, y=10, z=-4688410),
    locations=[
        SquareLocation(x1=2646513, z1=-4650065, x2=2647240, z2=-4650686)
    ],
    markers=[
        Marker(name="Turenne", x=2646857, y=278, z=-4650324, type=Type.VILLAGE),
    ]
)

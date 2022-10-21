from ..classes import Region, Marker, SquareLocation, Type

REGION = Region(
    id="cvdl",
    name="Centre-Val de Loire",
    prefecture=Marker(name="Centre-Val de Loire - Orléans", x=2782036, y=113, z=-4954558),
    locations=[
        SquareLocation(x1=2696748, z1=-4912707, x2=2697185, z2=-4913086),  # Chenonceau
        SquareLocation(x1=2670762, z1=-4931052, x2=2671150, z2=-4930662),  # Tours
        SquareLocation(x1=2670708, z1=-4926068, x2=2670926, z2=-4926401),
    ],
    markers=[
        Marker(name="Château de Chenonceau", x=2696968, y=54, z=-4912847, type=Type.CASTLE),
        Marker(name="Tours", x=2671000, y=52, z=-4930854, type=Type.CITY),
        Marker(name="Campus de Grandmont", x=2670790, y=86, z=-4926246, type=Type.BUILDING),
    ]
)

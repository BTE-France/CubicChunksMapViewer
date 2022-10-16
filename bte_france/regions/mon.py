from ..classes import Region, SquareLocation, Marker, Type

REGION = Region(
    id="mon",
    name="Monaco",
    prefecture=Marker(name="Monaco", x=3056394, y=26, z=-4355485),
    locations=[
        SquareLocation(x1=3056586, z1=-4355023, x2=3057804, z2=-4356325)
    ],
    markers=[
        Marker(name="Monte-Carlo", x=3057333, y=42, z=-4355815, type=Type.CITY),
        Marker(name="Port de Monaco", x=3056826, y=2, z=-4355418, type=Type.PORT)
    ]
)

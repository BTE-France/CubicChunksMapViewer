from ..classes import Region, SquareLocation, Marker

REGION = Region(
    id="mon",
    name="Monaco",
    locations=[
        SquareLocation(x1=3056586, z1=-4355023, x2=3057804, z2=-4356325)
    ],
    markers=[
        Marker(name="Monte-Carlo", x=3057333, y=42, z=-4355815),
        Marker(name="Port de Monaco", x=3056826, y=2, z=-4355418)
    ]
)

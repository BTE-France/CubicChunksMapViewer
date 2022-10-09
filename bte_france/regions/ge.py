from ..classes import Region, Marker, SquareLocation

REGION = Region(
    id="ge",
    name="Grand Est",
    locations=[
        SquareLocation(x1=3129934, z1=-4924887, x2=3130802, z2=-4925289),
        SquareLocation(x1=3130378, z1=-4925260, x2=3130771, z2=-4925863),
        SquareLocation(x1=3191234, z1=-4844378, x2=3191933, z2=-4845139),
    ],
    markers=[
        Marker(name="Azelot", x=3130304, y=287, z=-4925138),
        Marker(name="Turckheim", x=3191785, y=239, z=-4844447),
    ]
)

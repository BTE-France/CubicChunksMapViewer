from ..classes import Region, Marker, Type, SquareLocation

REGION = Region(
    id="guy",
    name="Guyane",
    prefecture=Marker(name="Guyane - Cayenne", x=-5637733, y=1, z=-1238916),
    locations=[
        SquareLocation(x1=-5681649, z1=-1281500, x2=-5681221, z2=-1281122),  # Centre Spatial
    ],
    markers=[
        Marker(name="Centre Spatial Guyanais", x=-5681450, y=11, z=-1281324, type=Type.BUILDING),
    ]
)

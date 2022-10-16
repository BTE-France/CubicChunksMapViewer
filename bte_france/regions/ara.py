from ..classes import Region, SquareLocation, Marker, Type

REGION = Region(
    id="ara",
    name="Auvergne-Rhône-Alpes",
    prefecture=Marker(name="Auvergne-Rhône-Alpes - Lyon", x=2923530, y=167, z=-4642334),
    locations=[
        SquareLocation(x1=2922851, z1=-4642981, x2=2923138, z2=-4643310),
        SquareLocation(x1=2924238, z1=-4642690, x2=2924748, z2=-4642979)
    ],
    markers=[
        Marker(name="Basilique de Fourvière", x=2922918, y=295, z=-4643104, type=Type.CHURCH),
        Marker(name="Lyon 6ème", x=2924473, y=168, z=-4642747, type=Type.CITY)
    ]
)

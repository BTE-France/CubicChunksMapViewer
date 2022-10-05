from ..classes import Region, SquareLocation, Marker

REGION = Region(
    id="ara",
    name="Auvergne-Rhône-Alpes",
    locations=[
        SquareLocation(x1=2922851, z1=-4642981, x2=2923138, z2=-4643310),
        SquareLocation(x1=2924238, z1=-4642690, x2=2924748, z2=-4642979)
    ],
    markers=[
        Marker(name="Fourvière", x=2922918, y=295, z=-4643104),
        Marker(name="Pont Lafayette", x=2924379, y=170, z=-4642780)
    ]
)

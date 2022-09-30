from ..classes import Region, Location, Marker

REGION = Region(
    id="ara",
    name="Auvergne-Rhône-Alpes",
    locations=[
        Location(x_min=2922851, z_min=-4642981, x_max=2923138, z_max=-4643310),
        Location(x_min=2924238, z_min=-4642690, x_max=2924748, z_max=-4642979)
    ],
    markers=[
        Marker(name="Fourvière", x=2922918, y=295, z=-4643104),
        Marker(name="Pont Lafayette", x=2924379, y=170, z=-4642780)
    ]
)

from ..classes import Region, Location, Marker

REGION = Region(
    id="idf",
    name="Île-de-France",
    locations=[
        Location(x_min=2849552, z_min=-5051837, x_max=2849676, z_max=-5052252),
        Location(x_min=2850569, z_min=-5050991, x_max=2850700, z_max=-5050334),
        Location(x_min=2847249, z_min=-5051504, x_max=2847738, z_max=-5051219)
    ],
    markers=[
        Marker(name="Tour Eiffel", x=2847518, y=64, z=-5051401),
        Marker(name="Palais de l'Elysée", x=2849653, y=33, z=-5052111),
        Marker(name="Notre-Dame", x=2851417, y=64, z=-5049353),
        Marker(name="Musée du Louvre", x=2850640, y=36, z=-5050645),
    ]
)

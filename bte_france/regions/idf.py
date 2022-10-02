from ..classes import Region, RoundLocation, SquareLocation, Marker

REGION = Region(
    id="idf",
    name="Île-de-France",
    locations=[
        RoundLocation(x=2847555, z=-5051327, radius=600),
        RoundLocation(x=2849653, z=-5052111, radius=300),
        RoundLocation(x=2851417, z=-5049353, radius=600),
        RoundLocation(x=2850640, z=-5050645, radius=600)
    ],
    markers=[
        Marker(name="Tour Eiffel", x=2847555, y=34, z=-5051327),
        Marker(name="Palais de l'Elysée", x=2849653, y=33, z=-5052111),
        Marker(name="Notre-Dame", x=2851417, y=64, z=-5049353),
        Marker(name="Musée du Louvre", x=2850640, y=36, z=-5050645),
    ]
)

from ..classes import Region, Marker, RoundLocation, Type

REGION = Region(
    id="paca",
    name="Provence-Alpes-Côte d'Azur",
    prefecture=Marker(name="Provence-Alpes-Côte d'Azur - Marseille", x=2878068, y=16, z=-4358366),
    locations=[
        RoundLocation(x=2959930, z=-4344971, radius=150),
    ],
    markers=[
        Marker(name="Le Vieux Cannet", x=2959930, y=244, z=-4344971, type=Type.VILLAGE),
    ]
)

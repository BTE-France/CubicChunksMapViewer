from ..classes import Region, Marker, RoundLocation, Type

REGION = Region(
    id="occ",
    name="Occitanie",
    prefecture=Marker(name="Occitanie - Toulouse", x=2579836, y=143, z=-4496947),
    locations=[
        RoundLocation(x=2738325, z=-4478999, radius=200),
    ],
    markers=[
        Marker(name="La Couvertoirade", x=2738325, y=774, z=-4478999, type=Type.VILLAGE),
    ]
)

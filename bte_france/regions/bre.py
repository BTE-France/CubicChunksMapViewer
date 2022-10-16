from ..classes import Region, Marker, RoundLocation, Type

REGION = Region(
    id="bre",
    name="Bretagne",
    prefecture=Marker(name="Bretagne - Rennes", x=2525750, y=43, z=-5074617),
    locations=[
        RoundLocation(x=2311330, z=-5187845, radius=300),
    ],
    markers=[
        Marker(name="Pointe de Saint-Mathieu", x=2311330, y=26, z=-5187845, type=Type.VILLAGE),
    ]
)

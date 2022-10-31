from ..classes import Region, Marker, SquareLocation, Type

REGION = Region(
    id="reu",
    name="La Réunion",
    prefecture=Marker(name="La Réunion - Saint-Denis", x=10619889, y=7, z=3133503),
    locations=[
        SquareLocation(x1=10617478, z1=3133919, x2=10617879, z2=3134450),  # St-Denis
    ],
    markers=[
        Marker(name="Saint-Denis", x=10617565, y=6, z=3134138, type=Type.CITY),
    ]
)

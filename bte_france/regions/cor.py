from ..classes import Region, Marker, RoundLocation, Type, SquareLocation

REGION = Region(
    id="cor",
    name="Corse",
    prefecture=Marker(name="Corse - Ajaccio", x=3104281, y=4, z=-4125277),
    locations=[
        RoundLocation(x=3126374, z=-4195242, radius=300),  # Calvi
        SquareLocation(x1=3139913, z1=-4163125, x2=3140324, z2=-4162675),  # Calacuccia
        SquareLocation(x1=3186005, z1=-4192663, x2=3186561, z2=-4193211),  # Bastia
        SquareLocation(x1=3186356, z1=-4193450, x2=3187166, z2=-4194227),
    ],
    markers=[
        Marker(name="Citadelle de Calvi", x=3126378, y=62, z=-4195249, type=Type.CASTLE),
        Marker(name="Barrage de Calacuccia", x=3140059, y=793, z=-4162883, type=Type.BUILDING),
        Marker(name="Citadelle de Bastia", x=3186359, y=18, z=-4192856, type=Type.CASTLE),
        Marker(name="Port de Bastia", x=3186693, y=2, z=-4193851, type=Type.PORT),
    ]
)

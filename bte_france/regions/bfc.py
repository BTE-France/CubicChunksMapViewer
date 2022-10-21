from ..classes import Region, Marker, SquareLocation, Type

REGION = Region(
    id="bfc",
    name="Bourgogne-Franche-Comté",
    prefecture=Marker(name="Bourgogne-Franche-Comté - Dijon", x=2995679, y=249, z=-4811020),
    locations=[
        SquareLocation(x1=2836941, z1=-4845530, x2=2837534, z2=-4845867),  # Charité
        SquareLocation(x1=2947583, z1=-4847537, x2=2948309, z2=-4847177),  # Semur
    ],
    markers=[
        Marker(name="La Charité-sur-Loire", x=2837378, y=172, z=-4845675, type=Type.VILLAGE),
        Marker(name="Semur-en-Auxois", x=2948097, y=278, z=-4847413, type=Type.VILLAGE),
    ]
)

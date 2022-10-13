from ..classes import Region, Marker, SquareLocation, RoundLocation

REGION = Region(
    id="ge",
    name="Grand Est",
    locations=[
        SquareLocation(x1=3129934, z1=-4924887, x2=3130802, z2=-4925289),  # Azelot
        SquareLocation(x1=3130378, z1=-4925260, x2=3130771, z2=-4925863),
        SquareLocation(x1=3191234, z1=-4844378, x2=3191933, z2=-4845139),  # Turckheim
        RoundLocation(x=3191894, z=-4846043, radius=300),  # Niedermorschwihr
        RoundLocation(x=3188937, z=-4829419, radius=600),  # Rouffach
        RoundLocation(x=3244185, z=-4890006, radius=600),  # Strasbourg
        RoundLocation(x=3167418, z=-4832093, radius=800),  # Markstein
        SquareLocation(x1=3144677, z1=-4986910, x2=3144946, z2=-4987125),  # Metz
        SquareLocation(x1=3147446, z1=-4982705, x2=3148024, z2=-4983259),  # Metz Technopôle
    ],
    markers=[
        Marker(name="Azelot", x=3130304, y=287, z=-4925138),
        Marker(name="Turckheim", x=3191785, y=239, z=-4844447),
        Marker(name="Niedermorschwihr", x=3191894, y=311, z=-4846043),
        Marker(name="Rouffach", x=3189001, y=204, z=-4829341),
        Marker(name="Cathédrale Notre Dame de Strasbourg", x=3244183, y=143, z=-4890011),
        Marker(name="Station du Markstein", x=3167482, y=1191, z=-4831814),
        Marker(name="Cathédrale de Metz", x=3144764, y=178, z=-4986987),
        Marker(name="Metz Technopôle", x=3147873, y=213, z=-4982774),
    ]
)

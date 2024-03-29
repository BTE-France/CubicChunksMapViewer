from ..classes import Marker, Region, RoundLocation, SquareLocation, Type

REGION = Region(
    id="ge",
    name="Grand Est",
    prefecture=Marker(name="Grand Est - Strasbourg", x=3244262, y=144, z=-4889987),
    locations=[
        SquareLocation(x1=3129934, z1=-4924887, x2=3130802, z2=-4925289),  # Azelot
        SquareLocation(x1=3130378, z1=-4925260, x2=3130771, z2=-4925863),
        SquareLocation(x1=3191234, z1=-4844378, x2=3191933, z2=-4845139),  # Turckheim
        RoundLocation(x=3191894, z=-4846043, radius=300),  # Niedermorschwihr
        RoundLocation(x=3188937, z=-4829419, radius=600),  # Rouffach
        RoundLocation(x=3244185, z=-4890006, radius=900),  # Strasbourg
        SquareLocation(x1=3243541, z1=-4891001, x2=3243884, z2=-4890591),
        SquareLocation(x1=3245908, z1=-4891657, x2=3246357, z2=-4890972),
        RoundLocation(x=3167418, z=-4832093, radius=800),  # Markstein
        SquareLocation(x1=3144677, z1=-4986910, x2=3144946, z2=-4987125),  # Metz
        SquareLocation(x1=3147446, z1=-4982705, x2=3148024, z2=-4983259),  # Metz Technopôle
        SquareLocation(x1=2952377, z1=-4972058, x2=2952701, z2=-4972475),  # Mery
        RoundLocation(x=2997541, z=-4926888, radius=250),  # Nigloland
    ],
    markers=[
        Marker(name="Azelot", x=3130304, y=287, z=-4925138, type=Type.VILLAGE),
        Marker(name="Turckheim", x=3191785, y=239, z=-4844447, type=Type.VILLAGE),
        Marker(name="Niedermorschwihr", x=3191894, y=311, z=-4846043, type=Type.VILLAGE),
        Marker(name="Rouffach", x=3189001, y=204, z=-4829341, type=Type.VILLAGE),
        Marker(name="Cathédrale Notre Dame de Strasbourg", x=3244183, y=143, z=-4890011, type=Type.CHURCH),
        Marker(name="Place des Halles", x=3243754, y=152, z=-4890795, type=Type.BUILDING),
        Marker(name="Parlement Européen", x=3246044, y=142, z=-4891389, type=Type.MONUMENT),
        Marker(name="Station du Markstein", x=3167482, y=1191, z=-4831814, type=Type.BUILDING),
        Marker(name="Cathédrale de Metz", x=3144764, y=178, z=-4986987, type=Type.CHURCH),
        Marker(name="Metz Technopôle", x=3147873, y=213, z=-4982774, type=Type.BUILDING),
        Marker(name="Méry-sur-Seine", x=2952515, y=83, z=-4972188, type=Type.VILLAGE),
        Marker(name="Nigloland", x=2997561, y=157, z=-4926900, type=Type.BUILDING),
    ]
)

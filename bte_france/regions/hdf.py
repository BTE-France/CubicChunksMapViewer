from ..classes import Region, Marker, RoundLocation, SquareLocation, Type

REGION = Region(
    id="hdf",
    name="Hauts-de-France",
    prefecture=Marker(name="Hauts-de-France - Lille", x=2971442, y=28, z=-5232818),
    locations=[
        RoundLocation(x=2916708, z=-5089081, radius=400),  # Pierrefonds
        RoundLocation(x=2854106, z=-5121173, radius=400),  # Beauvais
        SquareLocation(x1=2939734, z1=-5296477, x2=2939945, z2=-5296947),  # Dunkerque
        SquareLocation(x1=2888865, z1=-5166498, x2=2889264, z2=-5166095),  # Amiens
        SquareLocation(x1=2887654, z1=-5168164, x2=2888302, z2=-5167167),
        RoundLocation(x=2841165, z=-5138319, radius=600),  # Gerberoy
        SquareLocation(x1=2874314, z1=-5083877, x2=2875048, z2=-5084541),  # Chantilly
    ],
    markers=[
        Marker(name="Pierrefonds", x=2916708, y=111, z=-5089081, type=Type.CASTLE),
        Marker(name="Cathédrale Saint-Pierre", x=2854077, y=70, z=-5121133, type=Type.CHURCH),
        Marker(name="Dunkerque", x=2939838, y=8, z=-5296701, type=Type.CITY),
        Marker(name="Lycée Robert de Luzarches - Amiens", x=2889096, y=45, z=-5166192, type=Type.CITY),
        Marker(name="Cathédrale Notre-Dame d'Amiens", x=2888025, y=33, z=-5167801, type=Type.CHURCH),
        Marker(name="Palais de Justice d'Amiens", x=2887953, y=37, z=-5167561, type=Type.MONUMENT),
        Marker(name="Gerberoy", x=2841103, y=178, z=-5138391, type=Type.VILLAGE),
        Marker(name="Château de Chantilly", x=2874585, y=49, z=-5084120, type=Type.CASTLE),
    ]
)

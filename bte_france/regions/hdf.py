from ..classes import Region, Marker, RoundLocation, SquareLocation

REGION = Region(
    id="hdf",
    name="Hauts-de-France",
    locations=[
        RoundLocation(x=2916708, z=-5089081, radius=250),  # Pierrefonds
        RoundLocation(x=2854106, z=-5121173, radius=250),  # Beauvais
        SquareLocation(x1=2939734, z1=-5296477, x2=2939945, z2=-5296947),  # Dunkerque
        SquareLocation(x1=2888865, z1=-5166498, x2=2889264, z2=-5166095),  # Amiens
        SquareLocation(x1=2887654, z1=-5168164, x2=2888302, z2=-5167167),
    ],
    markers=[
        Marker(name="Pierrefonds", x=2916708, y=111, z=-5089081),
        Marker(name="Cathédrale Saint-Pierre", x=2854077, y=70, z=-5121133),
        Marker(name="Dunkerque", x=2939838, y=8, z=-5296701),
        Marker(name="Lycée Robert de Luzarches - Amiens", x=2889096, y=45, z=-5166192),
        Marker(name="Cathédrale Notre-Dame d'Amiens", x=2888025, y=33, z=-5167801),
        Marker(name="Palais de Justice d'Amiens", x=2887953, y=37, z=-5167561),
    ]
)

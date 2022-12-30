from ..classes import Region, SquareLocation, Marker, Type, RoundLocation

REGION = Region(
    id="ara",
    name="Auvergne-Rhône-Alpes",
    prefecture=Marker(name="Auvergne-Rhône-Alpes - Lyon", x=2923530, y=167, z=-4642334),
    locations=[
        SquareLocation(x1=2920692, z1=-4639426, x2=2924652, z2=-4643769),  # Lyon
        SquareLocation(x1=2924652, z1=-4643769, x2=2925139, z2=-4641040),
        SquareLocation(x1=2920354, z1=-4638486, x2=2920768, z2=-4638193),  # Oullins
        RoundLocation(x=2917639, z=-4636085, radius=400),  # St-Genis
        SquareLocation(x1=2931241, z1=-4637465, x2=2930392, z2=-4635153),  # Aéroport Bron
        SquareLocation(x1=2921680, z1=-4627459, x2=2922238, z2=-4627947),  # St-Symphorien
        SquareLocation(x1=2927907, z1=-4654776, x2=2928406, z2=-4654425),  # Neuville
        RoundLocation(x=3056929, z=-4595208, radius=500),  # Beaufort
        SquareLocation(x1=3021907, z1=-4589160, x2=3022266, z2=-4589404),  # Miolans
        RoundLocation(x=2884328, z=-4622132, radius=300),  # Sorbiers
        SquareLocation(x1=2789527, z1=-4689008, x2=2790492, z2=-4689497),  # Clermont
        SquareLocation(x1=2897442, z1=-4556314, x2=2897908, z2=-4556754),  # Arena45
    ],
    markers=[
        Marker(name="Basilique de Fourvière", x=2922918, y=295, z=-4643104, type=Type.CHURCH),
        Marker(name="Lyon 6ème", x=2924473, y=168, z=-4642747, type=Type.CITY),
        Marker(name="Hôtel de Ville", x=2924205, y=170, z=-4643339, type=Type.MONUMENT),
        Marker(name="Pont Kœnig", x=2922540, y=171, z=-4644174, type=Type.BUILDING),
        Marker(name="Tour Part-Dieu", x=2925298, y=175, z=-4642162, type=Type.BUILDING),
        Marker(name="La Guillotière", x=2924513, y=166, z=-4641342, type=Type.CITY),
        Marker(name="Musée des Confluences", x=2921452, y=166, z=-4639848, type=Type.MONUMENT),
        Marker(name="Oullins", x=2920577, y=164, z=-4638323, type=Type.CITY),
        Marker(name="Lycée René Descartes - Saint-Genis-Laval", x=2917534, y=230, z=-4636162, type=Type.BUILDING),
        Marker(name="Aéroport de Lyon-Bron", x=2930805, y=199, z=-4636703, type=Type.BUILDING),
        Marker(name="Saint-Symphorien-d'Ozon", x=2921991, y=178, z=-4627755, type=Type.CITY),
        Marker(name="Lycée Notre Dame de Bellegarde - Neuville-sur-Saône", x=2928273, y=179, z=-4654573, type=Type.BUILDING),
        Marker(name="Beaufort-sur-Doron", x=3056961, y=735, z=-4595334, type=Type.VILLAGE),
        Marker(name="Château de Miolans", x=3022104, y=538, z=-4589286, type=Type.CASTLE),
        Marker(name="Sorbiers", x=2884352, y=561, z=-4622241, type=Type.VILLAGE),
        Marker(name="Cathédrale Notre-Dame-de-l'Assomption", x=2789935, y=403, z=-4689369, type=Type.CHURCH),
        Marker(name="Circuit Arena45", x=2897705, y=114, z=-4556464, type=Type.BUILDING),
    ]
)

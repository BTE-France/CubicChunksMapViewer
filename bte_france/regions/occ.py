from ..classes import Region, Marker, RoundLocation, Type, SquareLocation

REGION = Region(
    id="occ",
    name="Occitanie",
    prefecture=Marker(name="Occitanie - Toulouse", x=2579836, y=143, z=-4496947),
    locations=[
        RoundLocation(x=2738325, z=-4478999, radius=200),  # La Couvertoirade
        SquareLocation(x1=2457563, z1=-4485681, x2=2458074, z2=-4485238),  # Vielle-Adour
        RoundLocation(x=2590113, z=-4582903, radius=200),  # Montcuq
        SquareLocation(x1=2611489, z1=-4588454, x2=2611811, z2=-4587964),  # Cahors
        SquareLocation(x1=2721191, z1=-4503846, x2=2721864, z2=-4506432),  # Millau
        SquareLocation(x1=2727932, z1=-4410422, x2=2728746, z2=-4409682),  # Agde
        SquareLocation(x1=2729451, z1=-4408856, x2=2730183, z2=-4408033),
        RoundLocation(x=2724071, z=-4411071, radius=200),  # Vias
        SquareLocation(x1=2749138, z1=-4413423, x2=2750014, z2=-4412473),  # Sète
        SquareLocation(x1=2767480, z1=-4434090, x2=2767702, z2=-4434284),  # Montpellier
        SquareLocation(x1=2771932, z1=-4430868, x2=2772962, z2=-4430161),
        SquareLocation(x1=2783230, z1=-4470373, x2=2783873, z2=-4469376),  # St-Hippo
        RoundLocation(x=2672252, z=-4332243, radius=100),  # Phare Cap Béar
        SquareLocation(x1=2568456, z1=-4517327, x2=2568755, z2=-4517578),  # Larra
        RoundLocation(x=2770240, z=-4467122, radius=300),  # Agonès
    ],
    markers=[
        Marker(name="La Couvertoirade", x=2738325, y=774, z=-4478999, type=Type.VILLAGE),
        Marker(name="Vielle-Adour", x=2457906, y=417, z=-4485547, type=Type.VILLAGE),
        Marker(name="Montcuq", x=2590121, y=202, z=-4582890, type=Type.VILLAGE),
        Marker(name="Pont Valentré", x=2611575, y=111, z=-4588266, type=Type.MONUMENT),
        Marker(name="Viaduc de Millau", x=2721543, y=631, z=-4505400, type=Type.MONUMENT),
        Marker(name="Agde", x=2728256, y=7, z=-4409872, type=Type.CITY),
        Marker(name="Agde - Les Portes du Littoral", x=2729728, y=9, z=-4408448, type=Type.CITY),
        Marker(name="Vias", x=2724038, y=9, z=-4411102, type=Type.VILLAGE),
        Marker(name="Sète", x=2749347, y=5, z=-4413263, type=Type.CITY),
        Marker(name="Pierresvives", x=2767627, y=52, z=-4434161, type=Type.BUILDING),
        Marker(name="Esplanade de l'Europe", x=2772650, y=14, z=-4430430, type=Type.MONUMENT),
        Marker(name="Place du Nombre d'Or", x=2772062, y=21, z=-4430689, type=Type.MONUMENT),
        Marker(name="Saint-Hippolyte-du-Fort", x=2783583, y=158, z=-4469778, type=Type.VILLAGE),
        Marker(name="Phare du Cap Béar", x=2672252, y=56, z=-4332243, type=Type.LIGHTHOUSE),
        Marker(name="Larra", x=2568626, y=162, z=-4517443, type=Type.VILLAGE),
        Marker(name="Agonès", x=2770311, y=159, z=-4467083, type=Type.VILLAGE),
    ]
)

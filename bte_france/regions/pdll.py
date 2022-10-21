from ..classes import Region, Marker, SquareLocation, Type, RoundLocation

REGION = Region(
    id="pdll",
    name="Pays de la Loire",
    prefecture=Marker(name="Pays de la Loire - Nantes", x=2497741, y=15, z=-4973388),
    locations=[
        SquareLocation(x1=2591208, z1=-4926828, x2=2592287, z2=-4925960),  # Le Puy
        SquareLocation(x1=2497561, z1=-4973011, x2=2497932, z2=-4973920),  # Nantes
        SquareLocation(x1=2495613, z1=-4972300, x2=2496379, z2=-4973028),
        SquareLocation(x1=2451568, z1=-4997630, x2=2452456, z2=-4998524),  # St Nazaire
        SquareLocation(x1=2581987, z1=-4972914, x2=2582351, z2=-4973290),  # Angers
        SquareLocation(x1=2581304, z1=-4972455, x2=2581756, z2=-4972657),
        RoundLocation(x=2577173, z=-4976652, radius=500),
        SquareLocation(x1=2608511, z1=-4936273, x2=2609170, z2=-4936708),  # Saumur
        SquareLocation(x1=2657688, z1=-5004923, x2=2658549, z2=-5005791),  # Le Mans
        RoundLocation(x=2421231, z=-5013242, radius=100),  # Phare Four
    ],
    markers=[
        Marker(name="Le Puy-Notre-Dame", x=2591934, y=97, z=-4926277, type=Type.VILLAGE),
        Marker(name="Château des ducs de Bretagne", x=2497784, y=10, z=-4973225, type=Type.CASTLE),
        Marker(name="Cathédrale Saint-Pierre-et-Saint-Paul de Nantes", x=2497722, y=18, z=-4973495, type=Type.CHURCH),
        Marker(name="Nantes - Les Machines", x=2496217, y=8, z=-4972694, type=Type.CITY),
        Marker(name="Saint-Nazaire", x=2451811, y=7, z=-4997916, type=Type.CITY),
        Marker(name="Angers", x=2582143, y=44, z=-4973104, type=Type.CITY),
        Marker(name="Gare d'Angers Saint-Laud", x=2581544, y=44, z=-4972565, type=Type.BUILDING),
        Marker(name="L'Atoll Angers", x=2577172, y=45, z=-4976648, type=Type.BUILDING),
        Marker(name="Château de Saumur", x=2608845, y=65, z=-4936440, type=Type.CASTLE),
        Marker(name="Circuit des 24 Heures du Mans", x=2658043, y=67, z=-5005435, type=Type.BUILDING),
        Marker(name="Phare du plateau du Four", x=2421231, y=0, z=-5013242, type=Type.LIGHTHOUSE),
    ]
)

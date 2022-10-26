from ..classes import Region, Marker, SquareLocation, Type, RoundLocation

REGION = Region(
    id="pdll",
    name="Pays de la Loire",
    prefecture=Marker(name="Pays de la Loire - Nantes", x=2497741, y=15, z=-4973388),
    locations=[
        SquareLocation(x1=2591208, z1=-4926828, x2=2592287, z2=-4925960),  # Le Puy
        SquareLocation(x1=2497561, z1=-4973011, x2=2497932, z2=-4973920),  # Nantes
        SquareLocation(x1=2495613, z1=-4972300, x2=2496379, z2=-4973028),
        SquareLocation(x1=2498261, z1=-4972684, x2=2498657, z2=-4971976),
        SquareLocation(x1=2496920, z1=-4973408, x2=2497726, z2=-4972861),
        SquareLocation(x1=2451568, z1=-4997630, x2=2452456, z2=-4998524),  # St Nazaire
        SquareLocation(x1=2451063, z1=-4998638, x2=2451346, z2=-4998229),
        SquareLocation(x1=2581987, z1=-4972914, x2=2582351, z2=-4973290),  # Angers
        SquareLocation(x1=2581304, z1=-4972455, x2=2581756, z2=-4972657),
        RoundLocation(x=2577173, z=-4976652, radius=500),
        SquareLocation(x1=2608511, z1=-4936273, x2=2609170, z2=-4936708),  # Saumur
        SquareLocation(x1=2657688, z1=-5004923, x2=2658549, z2=-5005791),  # Le Mans
        RoundLocation(x=2421231, z=-5013242, radius=100),  # Phare Four
        SquareLocation(x1=2614885, z1=-4924918, x2=2615357, z2=-4924500),  # Fontevraud
        RoundLocation(x=2437730, z=-5010409, radius=200),  # Guérande
    ],
    markers=[
        Marker(name="Le Puy-Notre-Dame", x=2591934, y=97, z=-4926277, type=Type.VILLAGE),
        Marker(name="Château des ducs de Bretagne", x=2497784, y=10, z=-4973225, type=Type.CASTLE),
        Marker(name="Cathédrale Saint-Pierre-et-Saint-Paul de Nantes", x=2497722, y=18, z=-4973495, type=Type.CHURCH),
        Marker(name="Préfecture de Nantes", x=2497704, y=12, z=-4973766, type=Type.MONUMENT),
        Marker(name="Nantes - Les Machines", x=2496217, y=8, z=-4972694, type=Type.MONUMENT),
        Marker(name="Stade Marcel Saupin", x=2498437, y=8, z=-4972545, type=Type.BUILDING),
        Marker(name="Palais des Sports", x=2498540, y=8, z=-4972187, type=Type.MONUMENT),
        Marker(name="Place Royale", x=2497026, y=8, z=-4973293, type=Type.CITY),
        Marker(name="Saint-Nazaire", x=2451811, y=7, z=-4997916, type=Type.CITY),
        Marker(name="Hôtel de Ville de Saint-Nazaire", x=2451151, y=12, z=-4998462, type=Type.MONUMENT),
        Marker(name="Angers", x=2582143, y=44, z=-4973104, type=Type.CITY),
        Marker(name="Gare d'Angers Saint-Laud", x=2581544, y=44, z=-4972565, type=Type.BUILDING),
        Marker(name="L'Atoll Angers", x=2577172, y=45, z=-4976648, type=Type.BUILDING),
        Marker(name="Château de Saumur", x=2608845, y=65, z=-4936440, type=Type.CASTLE),
        Marker(name="Circuit des 24 Heures du Mans", x=2658043, y=67, z=-5005435, type=Type.BUILDING),
        Marker(name="Phare du plateau du Four", x=2421231, y=0, z=-5013242, type=Type.LIGHTHOUSE),
        Marker(name="Fontevraud-l'Abbaye", x=2615089, y=81, z=-4924793, type=Type.VILLAGE),
        Marker(name="Guérande", x=2437730, y=49, z=-5010409, type=Type.VILLAGE),
    ]
)

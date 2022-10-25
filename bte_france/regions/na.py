from ..classes import Region, Marker, SquareLocation, Type, RoundLocation

REGION = Region(
    id="na",
    name="Nouvelle-Aquitaine",
    prefecture=Marker(name="Nouvelle-Aquitaine - Bordeaux", x=2473266, y=10, z=-4688410),
    locations=[
        SquareLocation(x1=2646513, z1=-4650065, x2=2647240, z2=-4650686),  # Turenne
        SquareLocation(x1=2612346, z1=-4853008, x2=2612644, z2=-4853477),  # Poitiers
        RoundLocation(x=2459389, z=-4856612, radius=100),  # Phare Chanchardon
        RoundLocation(x=2459334, z=-4842318, radius=100),  # Phare Chassiron
        RoundLocation(x=2480500, z=-4845528, radius=100),  # Phare bout du monde
        RoundLocation(x=2458060, z=-4785697, radius=100),  # Phare Cordouan
        RoundLocation(x=2472105, z=-4831564, radius=150),  # Fort Boyard
        SquareLocation(x1=2477484, z1=-4720905, x2=2478325, z2=-4721802),  # Blaye
        SquareLocation(x1=2500576, z1=-4686660, x2=2501087, z2=-4686183),  # Libourne
        SquareLocation(x1=2473652, z1=-4685553, x2=2474097, z2=-4684994),  # Bordeaux
        SquareLocation(x1=2472842, z1=-4685594, x2=2473957, z2=-4685991),
        SquareLocation(x1=2472287, z1=-4688007, x2=2472797, z2=-4687589),
        SquareLocation(x1=2473241, z1=-4688066, x2=2473487, z2=-4687677),
        SquareLocation(x1=2475261, z1=-4688902, x2=2475837, z2=-4689671),
    ],
    markers=[
        Marker(name="Turenne", x=2646857, y=278, z=-4650324, type=Type.VILLAGE),
        Marker(name="Lycée Polyvalent Nelson Mandela", x=2612489, y=121, z=-4853242, type=Type.BUILDING),
        Marker(name="Phare de Chanchardon", x=2459389, y=2, z=-4856612, type=Type.LIGHTHOUSE),
        Marker(name="Phare de Chassiron", x=2459334, y=9, z=-4842318, type=Type.LIGHTHOUSE),
        Marker(name="Phare du bout du monde", x=2480500, y=0, z=-4845528, type=Type.LIGHTHOUSE),
        Marker(name="Phare de Cordouan", x=2458060, y=0, z=-4785697, type=Type.LIGHTHOUSE),
        Marker(name="Fort-Boyard", x=2472105, y=0, z=-4831564, type=Type.MONUMENT),
        Marker(name="Blaye", x=2477715, y=6, z=-4721235, type=Type.VILLAGE),
        Marker(name="Libourne", x=2500856, y=8, z=-4686357, type=Type.VILLAGE),
        Marker(name="Bordeaux - Belcier", x=2473892, y=4, z=-4685351, type=Type.CITY),
        Marker(name="Gare Saint-Jean", x=2473693, y=12, z=-4685787, type=Type.BUILDING),
        Marker(name="Église du Sacré-Cœur", x=2473066, y=14, z=-4685628, type=Type.CHURCH),
        Marker(name="Tour Pey Berland", x=2472663, y=10, z=-4687641, type=Type.MONUMENT),
        Marker(name="Hôtel de ville de Bordeaux", x=2472473, y=8, z=-4687766, type=Type.MONUMENT),
        Marker(name="Place de la Bourse", x=2473371, y=7, z=-4687882, type=Type.MONUMENT),
        Marker(name="La Cité du Vin", x=2475708, y=7, z=-4689500, type=Type.BUILDING),
        Marker(name="Pont Jacques Chaban Delmas", x=2475411, y=66, z=-4689172, type=Type.BUILDING),
    ]
)

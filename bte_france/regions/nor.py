from ..classes import Region, Marker, SquareLocation, Type, RoundLocation

REGION = Region(
    id="nor",
    name="Normandie",
    prefecture=Marker(name="Normandie - Rouen", x=2782322, y=17, z=-5147287),
    locations=[
        SquareLocation(x1=2559770, z1=-5127021, x2=2560416, z2=-5127673),  # Mt St Michel
        SquareLocation(x1=2718799, z1=-5167056, x2=2719221, z2=-5167581),  # Honfleur
        SquareLocation(x1=2783420, z1=-5144968, x2=2784474, z2=-5144228),  # Bonsecours
        SquareLocation(x1=2782275, z1=-5147286, x2=2782564, z2=-5147050),  # Rouen
        SquareLocation(x1=2778857, z1=-5148826, x2=2780644, z2=-5148178),
        SquareLocation(x1=2707702, z1=-5136114, x2=2708011, z2=-5135866),  # Lisieux
        SquareLocation(x1=2572144, z1=-5128990, x2=2572514, z2=-5129262),  # Avranches
        RoundLocation(x=2678349, z=-5164436, radius=100),  # Phare Ouistreham
    ],
    markers=[
        Marker(name="Le Mont-Saint-Michel", x=2559924, y=6, z=-5127366, type=Type.MONUMENT),
        Marker(name="Honfleur", x=2718947, y=3, z=-5167362, type=Type.CITY),
        Marker(name="Bonsecours", x=2783910, y=145, z=-5144618, type=Type.CITY),
        Marker(name="Cathédrale Notre-Dame de Rouen", x=2782355, y=15, z=-5147234, type=Type.CHURCH),
        Marker(name="Pont Gustave Flaubert", x=2780304, y=15, z=-5148370, type=Type.MONUMENT),
        Marker(name="Grand Port Maritime de Rouen", x=2779705, y=6, z=-5148671, type=Type.PORT),
        Marker(name="Basilique Sainte-Thérèse de Lisieux", x=2707791, y=85, z=-5136009, type=Type.CHURCH),
        Marker(name="Lycée Notre Dame de la Providence", x=2572263, y=60, z=-5129183, type=Type.BUILDING),
        Marker(name="Phare de Ouistreham", x=2678349, y=6, z=-5164436, type=Type.LIGHTHOUSE),
    ]
)

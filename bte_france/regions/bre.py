from ..classes import Region, Marker, RoundLocation, Type, SquareLocation

REGION = Region(
    id="bre",
    name="Bretagne",
    prefecture=Marker(name="Bretagne - Rennes", x=2525750, y=43, z=-5074617),
    locations=[
        RoundLocation(x=2311330, z=-5187845, radius=600),  # Pointe St-Mathieu
        SquareLocation(x1=2333630, z1=-5187632, x2=2334077, z2=-5186819),  # Brest
        SquareLocation(x1=2333001, z1=-5184878, x2=2333890, z2=-5185774),
        RoundLocation(x=2344495, z=-5131762, radius=400),  # Quimper
        SquareLocation(x1=2522429, z1=-5142653, x2=2523303, z2=-5143494),  # St-Malo
        SquareLocation(x1=2523310, z1=-5143028, x2=2523960, z2=-5144054),
    ],
    markers=[
        Marker(name="Pointe de Saint-Mathieu", x=2311330, y=26, z=-5187845, type=Type.VILLAGE),
        Marker(name="Université de Bretagne-Occidentale", x=2333865, y=47, z=-5187356, type=Type.CITY),
        Marker(name="Château de Brest", x=2333440, y=26, z=-5185117, type=Type.CASTLE),
        Marker(name="Tour Tanguy", x=2333262, y=7, z=-5185384, type=Type.MONUMENT),
        Marker(name="Quimper", x=2344498, y=7, z=-5131833, type=Type.CITY),
        Marker(name="Fort National", x=2523626, y=18, z=-5143827, type=Type.CASTLE),
        Marker(name="Hôtel de Ville", x=2523518, y=6, z=-5143446, type=Type.MONUMENT),
        Marker(name="Port de Saint-Malo", x=2523505, y=8, z=-5143108, type=Type.PORT),
    ]
)

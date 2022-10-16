from ..classes import Region, RoundLocation, SquareLocation, Marker, Type

REGION = Region(
    id="idf",
    name="Île-de-France",
    prefecture=Marker(name="Île-de-France - Paris", x=2850830, y=34, z=-5050173),
    locations=[
        RoundLocation(x=2850640, z=-5050645, radius=5700),  # Paris
        SquareLocation(x1=2846066, z1=-5055718, x2=2846742, z2=-5056132),  # Ile de la Grande Jatte
        SquareLocation(x1=2844142, z1=-5056766, x2=2845959, z2=-5055519),  # La Defense
        SquareLocation(x1=2885734, z1=-5040156, x2=2886111, z2=-5040388),  # Disneyland
        RoundLocation(x=2883576, z=-5040745, radius=700),
    ],
    markers=[
        Marker(name="Tour Eiffel", x=2847555, y=34, z=-5051327, type=Type.MONUMENT),
        Marker(name="Palais de l'Elysée", x=2849653, y=33, z=-5052111, type=Type.MONUMENT),
        Marker(name="Notre Dame de Paris", x=2851417, y=64, z=-5049353, type=Type.CHURCH),
        Marker(name="Musée du Louvre", x=2850640, y=36, z=-5050645, type=Type.MONUMENT),
        Marker(name="Île de la Grande Jatte", x=2846460, y=31, z=-5055962, type=Type.CITY),
        Marker(name="La Défense", x=2844652, y=65, z=-5056569, type=Type.CITY),
        Marker(name="Arc de Triomphe", x=2848253, y=58, z=-5053020, type=Type.MONUMENT),
        Marker(name="Avenue Kléber", x=2847965, y=59, z=-5052819, type=Type.CITY),
        Marker(name="Grand Palais", x=2849150, y=33, z=-5051763, type=Type.MONUMENT),
        Marker(name="Basilique Sainte-Clotilde", x=2849424, y=34, z=-5050754, type=Type.CHURCH),
        Marker(name="Gare Saint-Lazare", x=2850588, y=35, z=-5052503, type=Type.BUILDING),
        Marker(name="Gare du Nord", x=2852831, y=53, z=-5052227, type=Type.BUILDING),
        Marker(name="Mairie de Levallois-Perret", x=2848427, y=32, z=-5055378, type=Type.BUILDING),
        Marker(name="Sacré-Cœur", x=2852215, y=122, z=-5053223, type=Type.CHURCH),
        Marker(name="Gare de Lyon", x=2852844, y=38, z=-5047856, type=Type.BUILDING),
        Marker(name="Radio France", x=2846177, y=33, z=-5050999, type=Type.BUILDING),
        Marker(name="Dream Castle", x=2885909, y=120, z=-5040262, type=Type.BUILDING),
        Marker(name="Disneyland Paris", x=2883678, y=121, z=-5040777, type=Type.BUILDING),
    ]
)

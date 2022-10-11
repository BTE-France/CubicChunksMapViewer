from ..classes import Region, RoundLocation, SquareLocation, Marker

REGION = Region(
    id="idf",
    name="Île-de-France",
    locations=[
        RoundLocation(x=2850640, z=-5050645, radius=5700),  # Paris
        SquareLocation(x1=2846066, z1=-5055718, x2=2846742, z2=-5056132),  # Ile de la Grande Jatte
        SquareLocation(x1=2844142, z1=-5056766, x2=2845959, z2=-5055519),  # La Defense
        SquareLocation(x1=2885734, z1=-5040156, x2=2886111, z2=-5040388),  # Disneyland
        RoundLocation(x=2883576, z=-5040745, radius=500),
    ],
    markers=[
        Marker(name="Tour Eiffel", x=2847555, y=34, z=-5051327),
        Marker(name="Palais de l'Elysée", x=2849653, y=33, z=-5052111),
        Marker(name="Notre Dame de Paris", x=2851417, y=64, z=-5049353),
        Marker(name="Musée du Louvre", x=2850640, y=36, z=-5050645),
        Marker(name="Île de la Grande Jatte", x=2846460, y=31, z=-5055962),
        Marker(name="La Défense", x=2844652, y=65, z=-5056569),
        Marker(name="Arc de Triomphe", x=2848253, y=58, z=-5053020),
        Marker(name="Avenue Kléber", x=2847965, y=59, z=-5052819),
        Marker(name="Grand Palais", x=2849150, y=33, z=-5051763),
        Marker(name="Basilique Sainte-Clotilde", x=2849424, y=34, z=-5050754),
        Marker(name="Gare Saint-Lazare", x=2850588, y=35, z=-5052503),
        Marker(name="Gare du Nord", x=2852831, y=53, z=-5052227),
        Marker(name="Mairie de Levallois-Perret", x=2848427, y=32, z=-5055378),
        Marker(name="Sacré-Cœur", x=2852215, y=122, z=-5053223),
        Marker(name="Gare de Lyon", x=2852844, y=38, z=-5047856),
        Marker(name="Radio France", x=2846177, y=33, z=-5050999),
        Marker(name="Dream Castle", x=2885909, y=120, z=-5040262),
        Marker(name="Disneyland Paris", x=2883678, y=121, z=-5040777),
    ]
)

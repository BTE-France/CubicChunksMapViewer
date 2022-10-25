from ..classes import Region, Marker, RoundLocation, Type, SquareLocation

REGION = Region(
    id="paca",
    name="Provence-Alpes-Côte d'Azur",
    prefecture=Marker(name="Provence-Alpes-Côte d'Azur - Marseille", x=2878068, y=16, z=-4358366),
    locations=[
        RoundLocation(x=2959930, z=-4344971, radius=150),  # Cannet
        SquareLocation(x1=2874116, z1=-4357575, x2=2874474, z2=-4357353),  # If
        SquareLocation(x1=2877586, z1=-4358832, x2=2878555, z2=-4358017),  # Marseille
        RoundLocation(x=2985779, z=-4336791, radius=300),  # Bergerie
        SquareLocation(x1=3048429, z1=-4354537, x2=3048888, z2=-4354985),  # Beaulieu
        SquareLocation(x1=3064376, z1=-4357745, x2=3065013, z2=-4358214),  # Menton
    ],
    markers=[
        Marker(name="Le Vieux Cannet", x=2959930, y=244, z=-4344971, type=Type.VILLAGE),
        Marker(name="Île d'If", x=2874271, y=18, z=-4357455, type=Type.BUILDING),
        Marker(name="Hôtel de Ville Pavillon Daviel", x=2878357, y=1, z=-4358097, type=Type.MONUMENT),
        Marker(name="Cathédrale La Major", x=2878038, y=12, z=-4358556, type=Type.CHURCH),
        Marker(name="Domaine de la Bergerie", x=2985684, y=31, z=-4336770, type=Type.BUILDING),
        Marker(name="Beaulieu-sur-Mer", x=3048648, y=23, z=-4354782, type=Type.VILLAGE),
        Marker(name="Menton", x=3064502, y=6, z=-4357987, type=Type.CITY),
        Marker(name="Basilique Saint-Michel Archange de Menton", x=3064918, y=33, z=-4358089, type=Type.CHURCH),
    ]
)

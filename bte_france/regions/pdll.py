from ..classes import Region, Marker, SquareLocation

REGION = Region(
    id="pdll",
    name="Pays de la Loire",
    locations=[
        SquareLocation(x1=2591208, z1=-4926828, x2=2592287, z2=-4925960),
        SquareLocation(x1=2497561, z1=-4973011, x2=2497932, z2=-4973920)
    ],
    markers=[
        Marker(name="Le Puy-Notre-Dame", x=2591934, y=97, z=-4926277),
        Marker(name="Château des ducs de Bretagne", x=2497784, y=10, z=-4973225),
        Marker(name="Cathédrale Saint-Pierre-et-Saint-Paul de Nantes", x=2497722, y=18, z=-4973495),
    ]
)

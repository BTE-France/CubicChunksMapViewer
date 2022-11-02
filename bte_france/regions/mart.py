from ..classes import Region, Marker, Type, SquareLocation

REGION = Region(
    id="mart",
    name="Martinique",
    prefecture=Marker(name="Martinique - Fort-de-France", x=-6442384, y=11, z=-2543145),
    locations=[
        SquareLocation(x1=-6443253, z1=-2542734, x2=-6442863, z2=-2543299),  # Fort-de-France
        SquareLocation(x1=-6444802, z1=-2543499, x2=-6444377, z2=-2543198),
    ],
    markers=[
        Marker(name="Tour Lumina", x=-6443093, y=10, z=-2543199, type=Type.BUILDING),
        Marker(name="Lycée Bellevue", x=-6444619, y=25, z=-2543330, type=Type.BUILDING),
    ]
)

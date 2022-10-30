from .classes import World

WORLDS = [
    World(
        id="france",
        name="France",
        regions=[
            "ara",
            "bfc",
            "bre",
            "cor",
            "cvdl",
            "ge",
            "hdf",
            "idf",
            "mon",
            "na",
            "nor",
            "occ",
            "paca",
            "pdll",
        ],
        center=(2793842, -4798093),
        minzoom=6
    ), World(
        id="martinique_guadeloupe",
        name="Martinique & Guadeloupe",
        regions=[
            "mart",
            "guad"
        ],
        center=(-6446904, -2636302),
        minzoom=8
    ), World(
        id="guyane",
        name="Guyane Française",
        regions=[
            "guy",
        ],
        center=(-5768334, -1109518),
        minzoom=7
    ), World(
        id="reunion",
        name="Île de la Réunion",
        regions=[
            "reu",
        ],
        center=(10647026, 3149170),
        minzoom=10
    ),
]

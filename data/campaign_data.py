import fileinput

monthly_10_items = [
    1126,  # Beastmen's Seal
    1127,  # Kindred's Seal
    2955,  # Kindred's Crest
    2956,  # High Kindred's Crest
    2957,  # Sacred Kindred's Crest
    1857,  # Cordial Invite
    2306,  # Martial Ball Invite
    5364,  # Training Grounds Key
    2487,  # Mercenary Camp Entry Slip
    5741,  # Flask Of Pest Repellent
    3557,  # Athena Orb
    5113,  # Cracked Nut
    3541,  # Seasoning Stone
    3543,  # Fossilized Fang
    3542,  # Fossilized Bone
    5724,  # Pungent Powder
    6535,  # Pungent Powder II
]

monthly_100_items = [
    8734,  # Mog Kupon I - S1
    8966,  # Eudaemon Blade
    8967,  # Eudaemon Cape
    8968,  # Eudaemon Ring
    8969,  # Eudaemon Sash
    8970,  # Eudaemon Shield
    17006,  # Drill Calamary
    17007,  # Dwarf Pugil
]

monthly_750_items = [
    3339,  # Honey Wine
    3341,  # Beastly Shank
    3343,  # Blue Pondweed
]
monthly_1000_items = [
    6499,  # Mog Patio Plans
    26164,  # Caliber Ring
    26165,  # Facility Ring
]

monthly_1500_items = [
    3340,  # Sweet Tea
    3342,  # Savory Shank
    3344,  # Red Pondweed
]

rotation_a_300_items = [
    3721,  # Frayed Pouch (B)
    5855,  # Frayed Pouch (A)
    5856,  # Frayed Pouch (G)
    5857,  # Frayed Pouch (D)
    5858,  # Frayed Pouch (R)
    5946,  # Frayed Sack (D)
    5947,  # Frayed Sack (L)
    4064,  # Rem's Tale Ch.1
    4065,  # Rem's Tale Ch.2
    4066,  # Rem's Tale Ch.3
    4067,  # Rem's Tale Ch.4
    4068,  # Rem's Tale Ch.5
]

rotation_a_1000_items = [
    4069,  # Copy Of Rem's Tale, Chapter 6
    4070,  # Copy Of Rem's Tale, Chapter 7
    4071,  # Copy Of Rem's Tale, Chapter 8
    4072,  # Copy Of Rem's Tale, Chapter 9
    4073,  # Copy Of Rem's Tale, Chapter 10
]

data = {
    99: {
        'year': 2021,
        'month': 9,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6413,  # Astral Cube
                    3705,  # Far East Hearth
                    4567,  # Moon Carrot
                    4568,  # Moon Ball
                ],
            300: [
                    10064,  # ♪Hyppogryph
                    10056,  # ♪Crawler
                    3721,  # Iroha Statue
                    25670,  # Rarab Cap
                    25675,  # White Rarab Cap
                    20578,  # Wind Knife
                    23753,  # Sandogasa
            ] + rotation_a_300_items,
            500: [
                    23800,  # Cancrine Apron
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
            ] + monthly_750_items,
            1000:
                monthly_1000_items +
                rotation_a_1000_items,
            1500: monthly_1500_items,
        },
    },
    100: {
        'year': 2021,
        'month': 10,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    26946,  # Pupil's Shirt
                    26964,  # Pupil's Camisa
                    27281,  # Pupil's Trousers
                    27455,  # Pupil's Shoes
                ],
            300: [
                    3726,  # Aphmau Statue
                    10050,  # ♪Tiger companion
                    3651,  # Harvest Pastry
                    25713,  # Track Shirt
                    27325,  # Track Pants
                    25586,  # Kakai Cap
                    21820,  # Lost Sickle
                    3739,  # Autumn Tree
                    54,  # Chocobo Commode
                ],
            500: [
                    3749,  # Chemistry Set
                ],
            750: [
                    3885,  # Melodious Plans
                    3886,  # Timbre Case Kit
                    3887,  # Musichinery Kit
            ] +
            monthly_750_items + [
                    6576,  # Turkey with Rolanberry Sauce
            ],
            1000:
                monthly_1000_items + [
                    3640,  # Rol. Delightaru
                    3714,  # White Clematis
                    3715,  # Pink Clematis
                    3717,  # Birch Tree
                ],
            1500: monthly_1500_items,
        },
    },
    101: {
        'year': 2021,
        'month': 11,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6413,  # Astral Cube
                    9891,  # Zinnia Orb
                    20713,  # Excalipoor
                    6008,  # Copse Candy
                    10850,  # Leech Belt
                    10851,  # Slime Belt
                ],
            300: [
                    10069,  # ♪Goobbue
                    10051,  # ♪Crab
                    10053,  # ♪Bomb
                    10058,  # ♪Beetle
                    10384,  # Cumulus Masque
                    20666,  # Blizzard Brand
                    25658,  # Wyrm. Masque +1
                    25757,  # Wyrmking Suit +1
                    10073,  # ♪Dhalmel
                    10076,  # ♪Golden Bomb
                ],
            500: [
                    10079,  # ♪Iron Giant
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
                ] + monthly_750_items + [
                    1873,  # Brigand's Chart
                    1874,  # Pirate's Chart
                ],
            1000:
                monthly_1000_items + [
                    6486,  # Frayed Sack (Pel)
                    6487,  # Frayed Sack (Fer)
                    6488,  # Frayed Sack (Tau)
                    6542,  # Worn Sack (SS+2)
                    6544,  # Worn Sack (LS+2)
                    6546,  # Worn Sack (DS+2)
                    6548,  # Worn Sack (ST+2)
                    6550,  # Worn Sack (LT+2)
                    6552,  # Worn Sack (DT+2)
                    6554,  # Worn Sack (SD+2)
                    6556,  # Worn Sack (LD+2)
                    6558,  # Worn Sack (DD+2)
                    6560,  # Worn Sack (SO+2)
                    6562,  # Worn Sack (LO+2)
                    6564,  # Worn Sack (DO+2)
                ],
            1500:
                monthly_1500_items + [
                    8720,  # Maliya. Coral Orb
                    8722,  # Hepatizon Ingot
                    8724,  # Beryllium Ingot
                    8726,  # Exalted Lumber
                    8728,  # Sif's Macrame
                    28653,  # Mundus Shield
                ],
        },
    },
    102: {
        'year': 2021,
        'month': 12,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    10112,  # Cipher: Zeid
                    10113,  # Cipher: Lion
                    10118,  # Cipher: Naja
                    10120,  # Cipher: Lehko
                    10124,  # Cipher: Luzaf
                    10125,  # Cipher: Najelith
                    10129,  # Cipher: Domina
                    10134,  # Cipher: S. Sibyl
                    10142,  # Cipher: Karaha
                    10149,  # Cipher: Areuhat
                    10136,  # Cipher: Uka
                    10141,  # Cipher: Kuyin
                    10144,  # Cipher: Abenzio
                    10145,  # Cipher: Rughadjeen
                    10150,  # Cipher: Lhe
                    10151,  # Cipher: Mayakov
                    10155,  # Cipher: Brygid
                    10156,  # Cipher: Mildaurion
                    10161,  # Cipher: Rongelouts
                    10166,  # Cipher: Robel-Akbel
                    10178,  # Cipher: Ullegore
                    10179,  # Cipher: Teodor
                    10183,  # Cipher: Darrcuiln
                ],
            300:
                rotation_a_300_items + [
                    10187,  # Cipher: Shantotto II
                ],
            500: [
                23800,  # Cancrine Apron
                3749,  # Chemistry Set
                10079,  # ♪Iron Giant
            ],
            750: [
                3885,  # Melodious Plans
                3886,  # Timbre Case Kit
                3887,  # Musichinery Kit
                ] + monthly_750_items + [
                    1873,  # Brigand's Chart
                    1874,  # Pirate's Chart
                ] + rotation_a_1000_items,
            1000:
                monthly_1000_items,
            1500:
                monthly_1500_items,
        },
    },
    103: {
        'year': 2022,
        'month': 1,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6413,  # Astral Cube
                    3705,  # Far East Hearth
                    25758,  # Rhapsody Shirt
                    27631,  # Cait Sith Guard
                ],
            300: [
                10061,  # ♪Tulfaire
                10066,  # ♪Spheroid
                10070,  # ♪Raaz
                18464,  # Ark Tachi
                18545,  # Ark Tabar
                18563,  # Ark Scythe
                18912,  # Ark Saber
                18913,  # Ark Sword
                3740,  # Model Synergy Furnace
                23790,  # Adenium Masque
                23791,  # Adenium Suit
            ],
            500: [
                    22045,  # Feline Hagoita
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
                ] + monthly_750_items + [
                    3713,  # Pot of Wards
                ],
            1000:
                monthly_1000_items + [
                    9057,  # Ayapec's Shell
                    9060,  # Ethereal Incense
                    9103,  # Vidmapire's Claw
                    9059,  # Azrael's Eye
                    9104,  # Centurio's Armor
                    9097,  # Mhuufya's Beak
                    9051,  # Camahueto's Fur
                    9031,  # Vedrfolnir's Wing
                ],
            1500:
                monthly_1500_items + [
                    3977,  # Gabbrath Horn
                    6068,  # Gabbrath Meat
                    3980,  # Bztavian Stinger
                    3981,  # Bztavian Wing
                    3978,  # Rockfin Fin
                    3979,  # Rockfin Tooth
                    4012,  # Waktza Rostrum
                    4013,  # Waktza Crest
                    4014,  # Yggdreant Bole
                    4015,  # Yggdreant Root
                    8752,  # Cehuetzi Claw
                    8753,  # Cehuetzi Ice Shard
                    8754,  # Cehuetzi Pelt
                ],
        },
    },
    104: {
        'year': 2022,
        'month': 2,
        'prizes': {
            10:
                monthly_10_items + [
                    26489,  # Troth
                ],
            100:
                monthly_100_items + [
                    21095,  # Heartbeater
                ],
            300: [
                    22124,  # Artemis's Bow
                    25677,  # Arthro's Cap
                    27765,  # Chocobo Masque
                    27911,  # Chocobo Suit
                    10074,  # ♪Doll
                    26545,  # Mithkabob Shirt
                    10078,  # ♪Wivre
                ],
            500: [
                    3751,  # Besigiled Table
                ],
            750: [
                    3885,  # Melodious Plans
                    3886,  # Timbre Case Kit
                    3887,  # Musichinery Kit
            ] + monthly_750_items + [
                    6381,  # Fisherman's Feast
            ],
            1000:
                monthly_1000_items + [
                    6486,  # Frayed Sack (Pel)
                    6487,  # Frayed Sack (Fer)
                    6488,  # Frayed Sack (Tau)
                ],
            1500:
                monthly_1500_items + [
                    3491,  # Akvan's Pennon
                    3492,  # Kaggen's Cuticle
                    3449,  # Celaeno's Cloth
                    3445,  # Hahava's Mail
                    3490,  # Pil's Tuille
                    3447,  # Voidwrought Plate
                ],
        },
    },
    105: {
        'year': 2022,
        'month': 3,
        'prizes': {
            10:
                monthly_10_items + [
                    26489,  # Troth
                    28661,  # Glinting Shield
                ],
            100:
                monthly_100_items + [
                    6413,  # Astral Cube
                    3705,  # Far East Hearth
                    3698,  # Cherry Tree
                    18879,  # Rounsey Wand
                    6537,  # Pungent Powder III
                ],
            300: [
                    25670,  # Rarab Cap
                    26693,  # Morbol Cap
                    26719,  # Sheep Cap
                    10062,  # ♪Warmachine
                    26410,  # Diamond Buckler
                    3719,  # Prishe Statue II
                    3720,  # Arciela Statue
                    3721,  # Iroha Statue
                    3722,  # Lion Statue
                    3723,  # Lilisette Statue
                    3726,  # Aphmau Statue
                    21977,  # Mutsunokami
                    3744,  # Mandragora Pot
                ],
            500: [
                    10080,  # ♪Byakko
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
                ] + monthly_750_items,
            1000:
                monthly_1000_items + [
                    6542,  # Worn Sack (SS+2)
                    6544,  # Worn Sack (LS+2)
                    6546,  # Worn Sack (DS+2)
                    6548,  # Worn Sack (ST+2)
                    6550,  # Worn Sack (LT+2)
                    6552,  # Worn Sack (DT+2)
                    6554,  # Worn Sack (SD+2)
                    6556,  # Worn Sack (LD+2)
                    6558,  # Worn Sack (DD+2)
                    6560,  # Worn Sack (SO+2)
                    6562,  # Worn Sack (LO+2)
                    6564,  # Worn Sack (DO+2)
                ],
            1500:
                monthly_1500_items,
        },
    },
    106: {
        'year': 2022,
        'month': 4,
        'prizes': {
            10:
                monthly_10_items + [
                    26489  # Troth
                ],
            100:
                monthly_100_items + [
                    27899,  # Alliance Shirt
                    28185,  # Alliance Pants
                    28324,  # Alliance Boots
                ],
            300: [
                    10050,  # ♪Tiger companion
                    10066,  # ♪Spheroid
                    10070,  # ♪Raaz
                    10074,  # ♪Doll
                    10078,  # ♪Wivre
                    22124,  # Artemis's Bow
                    25632,  # Carbie Cap
                    26717,  # Cait Sith Cap
                    25675,  # White Rarab Cap
                    26410,  # Diamond Buckler
                    3740,  # Model Synergy Furnace
                    21977,  # Mutsunokami
                    3744,  # Mandragora Pot
                    23790,  # Adenium Masque
                    23791,  # Adenium Suit
                ],
            500: [
                    22045,  # Feline Hagoita
                    3751,  # Besigiled Table
                    10080,  # ♪Byakko
                ],
            750: [
                    3885,  # Melodious Plans
                    3886,  # Timbre Case Kit
                    3887,  # Musichinery Kit
            ] + monthly_750_items + [
                    5109,  # Frayed Sack (A1)
                    5111,  # Frayed Sack (M1)
                    6264,  # Frayed Sack (H1)
            ],
            1000:
                monthly_1000_items + [
                    9277,  # Silver Voucher
                ],
            1500: monthly_1500_items
        },
    },
    107: {
        'year': 2022,
        'month': 5,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6413,   # Astral Cube
                    3705,   # Far East Hearth
                    26703,  # Lycopodium Masque
                    25639,  # Korrigan Masque
                    25715,  # Korrigan Suit
                    20713,  # Excalipoor
                    20668,  # Firetongue
                    10384,  # Cumulus Masque
                    3718,   # Ado. Tomatoes
                    10112,  # Cipher: Zeid
                    10113,  # Cipher: Lion
                    10118,  # Cipher: Naja
                    10120,  # Cipher: Lehko
                    10124,  # Cipher: Luzaf
                    10125,  # Cipher: Najelith
                    10129,  # Cipher: Domina
                    10134,  # Cipher: S. Sibyl
                    10142,  # Cipher: Karaha
                    10149,  # Cipher: Areuhat
                    10136,  # Cipher: Uka
                    10141,  # Cipher: Kuyin
                    10144,  # Cipher: Abenzio
                    10145,  # Cipher: Rughadjeen
                    10150,  # Cipher: Lhe
                    10151,  # Cipher: Mayakov
                    10155,  # Cipher: Brygid
                    10156,  # Cipher: Mildaurion
                    10161,  # Cipher: Rongelouts
                    10166,  # Cipher: Robel-Akbel
                    10178,  # Cipher: Ullegore
                    10179,  # Cipher: Teodor
                    10183,  # Cipher: Darrcuiln
                ],
            300: [
                    10187,  # Cipher: Shantotto II
                    10050,  # ♪Tiger companion
                    10051,  # ♪Crab
                    10056,  # ♪Crawler
                    10058,  # ♪Beetle
                    10060,  # ♪Magic Pot
                    10061,  # ♪Tulfaire
                    10062,  # ♪Warmachine
                    10063,  # ♪Xzomit
                    10064,  # ♪Hyppogryph
                    10066,  # ♪Spheroid
                    4064,   # Rem's Tale Ch.1
                    4065,   # Rem's Tale Ch.2
                    4066,   # Rem's Tale Ch.3
                    4067,   # Rem's Tale Ch.4
                    4068,   # Rem's Tale Ch.5
                ],
            500: [
                    10081,  # ♪Noble Chocobo
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
                ] + monthly_750_items + [
                    1873,  # Brigand's Chart
                    1874,  # Pirate's Chart
                ] + rotation_a_1000_items,
            1000:
                monthly_1000_items,
            1500:
                monthly_1500_items,
        },
    },
    108: {
        'year': 2022,
        'month': 6,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6008,   # Copse Candy
                    26738,  # Leafkin Cap
                    20532,  # Worm Feelers
                    27717,  # Worm Masque
                    1850,   # First Virtue
                    1853,   # Second Virtue
                    1856,   # Third Virtue
                    1851,   # Deed of Placidity
                    1854,   # Deed of Moder.
                    1870,   # Deed of Sensib.
                ],
            300: [
                    25652,  # Crab Cap
                    26956,  # Poroggo Coat
                    3722,   # Lion Statue
                    26524,  # Gil Nabber Shirt
                    3720,   # Arciela Statue
                    22153,  # Silver Gun
                    10068,  # ♪Coeurl
                    10069,  # ♪Goobbue
                    10070,  # ♪Raaz
                    10072,  # ♪Adamantoise
                    10073,  # ♪Dhalmel
                    10074,  # ♪Doll
                    10075,  # ♪Red Raptor
                    10076,  # ♪Golden Bomb
                    10078,  # ♪Wivre
                    10079,  # ♪Iron Giant
                    10080,  # ♪Byakko
                    4064,   # Rem's Tale Ch.1
                    4065,   # Rem's Tale Ch.2
                    4066,   # Rem's Tale Ch.3
                    4067,   # Rem's Tale Ch.4
                    4068,   # Rem's Tale Ch.5
                ],
            500: [
                    23803,  # Poroggo Cassock
                ],
            750: [
                    3885,  # Melodious Plans
                    3886,  # Timbre Case Kit
                    3887,  # Musichinery Kit
                ] + monthly_750_items + [
                ] + rotation_a_1000_items + [
                    1110,  # Black Beetle Blood
                    844,   # Phoenix Feather
                    836,   # Damascene Cloth
                    837,   # Malboro Fiber
                    1311,  # Oxblood
                    9009,  # Etched Memory
                ],
            1000:
                monthly_1000_items + [
                    15554,  # Pelican Ring
            ],
            1500:
                monthly_1500_items,
        },
    },
    109: {
        'year': 2022,
        'month': 7,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6413,   # Astral Cube
                    3705,   # Far East Hearth
                    20713,  # Excalipoor
                    18879,  # Rounsey Wand
                    21107,  # Kyuka Uchiwa
                    27757,  # Bomb Masque
                    25672,  # Snoll Masque
                    21095,  # Heartstopper
                    16120,  # Redeyes
                ],
            300: [
                    10053,  # ♪Bomb
                    10063,  # ♪Xzomit
                    21965,  # Zanmato
                    3732,   # Crimson Chest
                    3743,   # Moogle Bed
                    3748,   # Leafkin Bed
                    4064,   # Rem's Tale Ch.1
                    4065,   # Rem's Tale Ch.2
                    4066,   # Rem's Tale Ch.3
                    4067,   # Rem's Tale Ch.4
                    4068,   # Rem's Tale Ch.5
                ],
            500: [
                    3752,  # Colibri Bed
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
                ] + monthly_750_items + [
                    6381,  # Fisherman's Feast
                    4069,  # Rem's Tale Ch. 6
                    4070,  # Rem's Tale Ch. 7
                    4071,  # Rem's Tale Ch. 8
                    4072,  # Rem's Tale Ch. 9
                    4073,  # Rem's Tale Ch. 10
                    1110,  # Black Beetle Blood
                    844,   # Phoenix Feather
                    836,   # Damascene Cloth
                    837,   # Malboro Fiber
                    1311,  # Oxblood
                    9009,  # Etched Memory
                ],
            1000:
                monthly_1000_items + [
                    2932,  # Kukulkan's Fang
                    2928,  # Two-Lead Chloris Bud
                    2927,  # Glavoid Shell
                    2929,  # Helm of Briareus
                    2930,  # Carabosse's Gem
                    2962,  # Itzpapalotl's Scale
                    2963,  # Ulhuadshi's Fang
                    2965,  # Ciren-croin's Lantern
                    2964,  # Sobek's Skin
                    2966,  # Bukhis's Wing
                    2967,  # Sedna's Tusk
                    3287,  # Orthrus's Claw
                    3288,  # Dragua's Scale
                    3289,  # Apademak's Horn
                    3292,  # Azdaja's Horn
                    3290,  # Isgebind's Heart
                    3291,  # Alfrad's Fang
                    ],
            1500:
                monthly_1500_items,
        },
    },

    110: {
        'year': 2022,
        'month': 8,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    21967,  # Melon Slicer
                    10112,  # Cipher: Zeid
                    10113,  # Cipher: Lion
                    10118,  # Cipher: Naja
                    10120,  # Cipher: Lehko
                    10124,  # Cipher: Luzaf
                    10125,  # Cipher: Najelith
                    10129,  # Cipher: Domina
                    10134,  # Cipher: Star Sibyl
                    10142,  # Cipher: Karaha
                    10149,  # Cipher: Areuhat
                    10136,  # Cipher: Uka
                    10141,  # Cipher: Kuyin
                    10144,  # Cipher: Abenzio
                    10145,  # Cipher: Rughadjeen
                    10150,  # Cipher: Lhe
                    10151,  # Cipher: Mayakov
                    10155,  # Cipher: Bygid
                    10156,  # Cipher: Mildaurion
                    10161,  # Cipher: Rongelouts
                    10166,  # Cipher: Robel-Akbel
                    10178,  # Cipher: Ullegore
                    10179,  # Cipher: Teodor
                    10183,  # Cipher: Darrcuiln
                ],
            300: [
                    10187,  # Cipher: Shantotto II
                    20668,  # Firetongue
                    21965,  # Zanmato
                    21867,  # Sha Wujin's Lance
                    3722,   # Lion Statue
                    3720,   # Arciela Statue
                    3732,   # Crimson Chest
                    10068,  # ♪Coeurl
                    10072,  # ♪Adamantoise
                    22017,  # Selka Uchiwa
                    25774,  # Fancy Gilet
                    25775,  # Fancy Top
                    25838,  # Fancy Trunks
                    25839,  # Fancy Shorts
                    26514,  # Poroggo Fleece
                    3743,   # Moogle Bed
                    3718,   # Ado. Tomatoes
                    10075,  # ♪Red Raptor
                    22153,  # Silver Gun
                    3748,   # Leafkin Bed
                    ],
            500: [
                    10081,  # ♪Noble Chocobo
                    23803,  # Poroggo Cassock
                    3752,   # Colibri Bed
                ],
            750: [
                    3885,   # Meldious Plans
                    3886,   # Timbre Case Kit
                    3887,   # Musichinery Kit
                ] + monthly_750_items,
            1000:
                monthly_1000_items + [
                    6486,   # Frayed Sack(Pel)
                    6487,   # Frayed Sack(Fer)
                    6488,   # Frayed Sack(Tau)
                    ],
            1500:
                monthly_1500_items,
        },
            111: {
        'year': 2022,
        'month': 9,
        'prizes': {
            10:
                monthly_10_items,
            100:
                monthly_100_items + [
                    6413,  # Astral Cube
                    3705,  # Far East Hearth
                    4567,  # Moon Carrot
                    4568,  # Moon Ball
                    21153, # Malice Masher
                ],
            300: [
                    10064, # ♪Hippogryph
                    10056, # ♪Crawler
                    3712,  # Iroha Statue
                    25670, # Rarab Cap
                    25675, # White Rarab Cap
                    20578, # Wind Knife
                    23753, # Sandogasa
                    23800, # Cancrine Apron
                    5854,  # Frayed Pouch (B)
                    5855,  # Frayed Pouch (A)
                    5856,  # Frayed Pouch (G)
                    5857,  # Frayed Pouch (D)
                    5858,  # Frayed Pouch (R)
                    5946,  # Frayed Sack (D)
                    5947,  # Frayed Sack (L)
                    4064,  # Rem's Tale Ch.1
                    4065,  # Rem's Tale Ch.2
                    4066,  # Rem's Tale Ch.3
                    4067,  # Rem's Tale Ch.4
                    4068,  # Rem's Tale Ch.5
                    ],
            500: [
                    25911, # Denim Pants
                ],
            750: [
                    9079,  # Kitchen Brick
                    9080,  # Kitchen Stove
                    9081,  # Kitchen Plate
                ] + monthly_750_items + [
                    4069,  #Rem's Tale Ch. 6
                    4070,  #Rem's Tale Ch. 7
                    4071,  #Rem's Tale Ch. 8
                    4072,  #Rem's Tale Ch. 9
                    4073,  #Rem's Tale Ch. 10
                    ],
            1000:
                monthly_1000_items,
            1500:
                monthly_1500_items,
        },
    },
    },
}


def create_file(docker, campaign_number, file):
    if docker:
        f = open("login_campaign_data.lua", "w")
    else:
        f = open(file + "/scripts/globals/events/login_campaign_data.lua", "w")

    option_id = 1

    f.write("local prizes =\n")
    f.write("{\n")
    for price in data[campaign_number]['prizes']:
        f.write("    [{0}] =\n".format(option_id))
        f.write("    {\n")
        f.write("        [\"price\"] = {0},\n".format(price))
        f.write("        [\"items\"] =\n")
        f.write("        {\n")
        count = 0
        for item_id in data[campaign_number]['prizes'][price]:
            if count < 20:
                f.write("            {0},\n".format(item_id))
                count = count + 1
            else:
                f.write("        },\n")
                f.write("    },\n")
                option_id = option_id + 4
                f.write("    [{0}] =\n".format(option_id))
                f.write("    {\n")
                f.write("        [\"price\"] = {0},\n".format(price))
                f.write("        [\"items\"] =\n")
                f.write("        {\n")
                f.write("            {0},\n".format(item_id))
                count = 1
        f.write("        },\n")
        f.write("    },\n")
        option_id = option_id + 4
    f.write("}\n")
    f.write("return prizes")


def enable_login_campaign(file):
    for line in fileinput.FileInput(file + "/settings/main.lua", inplace=True):
        if line.find("ENABLE_LOGIN_CAMPAIGN = ") != -1:
            print("    ENABLE_LOGIN_CAMPAIGN = 1,")
        else:
            print(line, end='')


def change_campaign_date(campaign_number, day, duration, file):
    for line in fileinput.FileInput(file + "/scripts/globals/events/login_campaign.lua", inplace=True):
        if line.find("loginCampaignYear = ") != -1:
            print("loginCampaignYear = " + str(data[campaign_number]['year']))
        elif line.find("loginCampaignMonth = ") != -1:
            print("loginCampaignMonth = " +
                  str(data[campaign_number]['month']))
        elif line.find("loginCampaignDay = ") != -1:
            print("loginCampaignDay = " + str(day))
        elif line.find("loginCampaignDuration = ") != -1:
            print("loginCampaignDuration = " + str(duration))
        else:
            print(line, end='')

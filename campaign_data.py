import fileinput


data = {
    2021: {
        9: {
            1: {
                10: {
                    0: 1126,  # Beastmen's Seal
                    1: 1127,  # Kindred's Seal
                    2: 2955,  # Kindred's Crest
                    3: 2956,  # High Kindred's Crest
                    4: 2957,  # Sacred Kindred's Crest
                    5: 1857,  # Cordial Invite
                    6: 2306,  # Martial Ball Invite
                    7: 5364,  # Training Grounds Key
                    8: 2487,  # Mercenary Camp Entry Slip
                    9: 5741,  # Flask Of Pest Repellent
                    10: 3557,  # Athena Orb
                    11: 5113,  # Cracked Nut
                    12: 3541,  # Seasoning Stone
                    13: 3543,  # Fossilized Fang
                    14: 3542,  # Fossilized Bone
                    15: 5724,  # Pungent Powder
                    16: 6535,  # Pungent Powder II
                },
            },
            5: {
                100: {
                    0: 8734,  # Mog Kupon I - S1
                    1: 8966,  # Eudaemon Blade
                    2: 8967,  # Eudaemon Cape
                    3: 8968,  # Eudaemon Ring
                    4: 8969,  # Eudaemon Sash
                    5: 8970,  # Eudaemon Shield
                    6: 17006,  # Drill Calamary
                    7: 17007,  # Dwarf Pugil
                    8: 6413,  # Astral Cube
                    9: 3705,  # Far East Hearth
                    10: 4567,  # Moon Carrot
                    11: 4568,  # Moon Ball
                },
            },
            9: {
                300: {
                    0: 10064,  # ♪Hyppogryph
                    1: 10056,  # ♪Crawler
                    2: 3721,  # Iroha Statue
                    3: 25670,  # Rarab Cap
                    4: 25675,  # White Rarab Cap
                    5: 20578,  # Wind Knife
                    6: 23753,  # Sandogasa
                    7: 3721,  # Frayed Pouch (B)
                    8: 5855,  # Frayed Pouch (A)
                    9: 5856,  # Frayed Pouch (G)
                    10: 5857,  # Frayed Pouch (D)
                    11: 5858,  # Frayed Pouch (R)
                    12: 5946,  # Frayed Sack (D)
                    13: 5947,  # Frayed Sack (L)
                    14: 4064,  # Rem's Tale Ch.1
                    15: 4065,  # Rem's Tale Ch.2
                    16: 4066,  # Rem's Tale Ch.3
                    17: 4067,  # Rem's Tale Ch.4
                    18: 4068,  # Rem's Tale Ch.5
                },
            },
            13: {
                500: {
                    0: 23800,  # Cancrine Apron
                },
            },
            17: {
                750: {
                    0: 9079,  # Kitchen Brick
                    1: 9080,  # Kitchen Stove
                    2: 9081,  # Kitchen Plate
                    3: 3339,  # Honey Wine
                    4: 3341,  # Beastly Shank
                    5: 3343,  # Blue Pondweed
                },
            },
            21: {
                1000: {
                    0: 6499,  # Patio Design Plans
                    1: 26165,  # Facility Ring
                    2: 26164,  # Caliber Ring
                    3: 4069,  # Copy Of Rem's Tale, Chapter 6
                    4: 4070,  # Copy Of Rem's Tale, Chapter 7
                    5: 4071,  # Copy Of Rem's Tale, Chapter 8
                    6: 4072,  # Copy Of Rem's Tale, Chapter 9
                    7: 4073,  # Copy Of Rem's Tale, Chapter 10
                },
            },
            25: {
                1500: {
                    0: 3340,  # Sweet Tea
                    1: 3342,  # Savory Shank
                    2: 3344,  # Red Pondweed
                }
            }
        },
        10: {
            1: {
                10: {
                    0: 1126,  # Beastmen's Seal
                    1: 1127,  # Kindred's Seal
                    2: 2955,  # Kindred's Crest
                    3: 2956,  # High Kindred's Crest
                    4: 2957,  # Sacred Kindred's Crest
                    5: 1857,  # Cordial Invite
                    6: 2306,  # Martial Ball Invite
                    7: 5364,  # Training Grounds Key
                    8: 2487,  # Mercenary Camp Entry Slip
                    9: 5741,  # Flask Of Pest Repellent
                    10: 3557,  # Athena Orb
                    11: 5113,  # Cracked Nut
                    12: 3541,  # Seasoning Stone
                    13: 3543,  # Fossilized Fang
                    14: 3542,  # Fossilized Bone
                    15: 5724,  # Pungent Powder
                    16: 6535,  # Pungent Powder II
                },
            },
            5: {
                100: {
                    0: 8734,  # Mog Kupon I - S1
                    1: 8966,  # Eudaemon Blade
                    2: 8967,  # Eudaemon Cape
                    3: 8968,  # Eudaemon Ring
                    4: 8969,  # Eudaemon Sash
                    5: 8970,  # Eudaemon Shield
                    6: 17006,  # Drill Calamary
                    7: 17007,  # Dwarf Pugil
                    8: 26946,  # Pupil's Shirt
                    9: 26964,  # Pupil's Camisa
                    10: 27281,  # Pupil's Trousers
                    11: 27455,  # Pupil's Shoes
                },
            },
            9: {
                300: {
                    0: 3726,  # Aphmau Statue
                    1: 10050,  # ♪Tiger companion
                    2: 3651,  # Harvest Pastry
                    3: 25713,  # Track Shirt
                    4: 27325,  # Track Pants
                    5: 25586,  # Kakai Cap
                    6: 21820,  # Lost Sickle
                    7: 3739,  # Autumn Tree
                    8: 54,  # Chocobo Commode
                },
            },
            13: {
                500: {
                    0: 3749,  # Chemistry Set
                },
            },
            17: {
                750: {
                    0: 3885,  # Melodious Plans
                    1: 3886,  # Timbre Case Kit
                    2: 3887,  # Musichinery Kit
                    3: 3339,  # Honey Wine
                    4: 3341,  # Beastly Shank
                    5: 3343,  # Blue Pondweed
                    6: 6576,  # Turkey with Rolanberry Sauce
                },
            },
            21: {
                1000: {
                    0: 6499,  # Patio Design Plans
                    1: 26164,  # Caliber Ring
                    2: 26165,  # Facility Ring
                    3: 3640,  # Rol. Delightaru
                    4: 3714,  # White Clematis
                    5: 3715,  # Pink Clematis
                    6: 3717,  # Birch Tree
                },
            },
            25: {
                1500: {
                    0: 3340,  # Sweet Tea
                    1: 3342,  # Savory Shank
                    2: 3344,  # Red Pondweed
                }
            }
        },
        11: {
            1: {
                10: {
                    0: 1126,  # Beastmen's Seal
                    1: 1127,  # Kindred's Seal
                    2: 2955,  # Kindred's Crest
                    3: 2956,  # High Kindred's Crest
                    4: 2957,  # Sacred Kindred's Crest
                    5: 1857,  # Cordial Invite
                    6: 2306,  # Martial Ball Invite
                    7: 5364,  # Training Grounds Key
                    8: 2487,  # Mercenary Camp Entry Slip
                    9: 5741,  # Flask Of Pest Repellent
                    10: 3557,  # Athena Orb
                    11: 5113,  # Cracked Nut
                    12: 3541,  # Seasoning Stone
                    13: 3543,  # Fossilized Fang
                    14: 3542,  # Fossilized Bone
                    15: 5724,  # Pungent Powder
                    16: 6535,  # Pungent Powder II
                    17: 9890,  # Tarazacum Orb
                },
            },
            5: {
                100: {
                    0: 8734,  # Mog Kupon I - S1
                    1: 8966,  # Eudaemon Blade
                    2: 8967,  # Eudaemon Cape
                    3: 8968,  # Eudaemon Ring
                    4: 8969,  # Eudaemon Sash
                    5: 8970,  # Eudaemon Shield
                    6: 17006,  # Drill Calamary
                    7: 17007,  # Dwarf Pugil
                    8: 6413,  # Astral Cube
                    9: 9891,  # Zinnia Orb
                    10: 20713,  # Excalipoor
                    11: 6008,  # Copse Candy
                    12: 10850,  # Leech Belt
                    13: 10851,  # Slime Belt
                },
            },
            9: {
                300: {
                    0: 10069,  # ♪Goobbue
                    1: 10051,  # ♪Crab
                    2: 10058,  # ♪Beetle
                    3: 10384,  # Cumulus Masque
                    4: 20666,  # Blizzard Brand
                    5: 25658,  # Wyrm. Masque +1
                    6: 25757,  # Wyrmking Suit +1
                    7: 10073,  # ♪Dhalmel
                    8: 10076,  # ♪Golden Bomb
                },
            },
            13: {
                500: {
                    0: 10079,  # ♪Iron Giant
                },
            },
            17: {
                750: {
                    0: 9079,  # Kitchen Brick
                    1: 9080,  # Kitchen Stove
                    2: 9081,  # Kitchen Plate
                    3: 3339,  # Honey Wine
                    4: 3341,  # Beastly Shank
                    5: 3343,  # Blue Pondweed
                    6: 1873,  # Brigand's Chart
                    7: 1874,  # Pirate's Chart
                },
            },
            21: {
                1000: {
                    0: 6499,  # Mog Patio Plans
                    1: 26164,  # Caliber Ring
                    2: 26165,  # Facility Ring
                    3: 6486,  # Frayed Sack (Pel)
                    4: 6487,  # Frayed Sack (Fer)
                    5: 6488,  # Frayed Sack (Tau)
                    6: 6542,  # Worn Sack (SS+2)
                    7: 6544,  # Worn Sack (LS+2)
                    8: 6546,  # Worn Sack (DS+2)
                    9: 6548,  # Worn Sack (ST+2)
                    10: 6550,  # Worn Sack (LT+2)
                    11: 6552,  # Worn Sack (DT+2)
                    12: 6554,  # Worn Sack (SD+2)
                    13: 6556,  # Worn Sack (LD+2)
                    14: 6558,  # Worn Sack (DD+2)
                    15: 6560,  # Worn Sack (SO+2)
                    16: 6562,  # Worn Sack (LO+2)
                    17: 6564,  # Worn Sack (DO+2)
                },
            },
            25: {
                1500: {
                    0: 3340,  # Sweet Tea
                    1: 3342,  # Savory Shank
                    2: 3344,  # Red Pondweed
                    3: 8720,  # Maliya. Coral Orb
                    4: 8722,  # Hepatizon Ingot
                    5: 8724,  # Beryllium Ingot
                    6: 8726,  # Exalted Lumber
                    7: 8728,  # Sif's Macrame
                    8: 28653,  # Mundus Shield
                }
            }
        },
        12: {
            1: {
                10: {
                    0: 1126,  # Beastmen's Seal
                    1: 1127,  # Kindred's Seal
                    2: 2955,  # Kindred's Crest
                    3: 2956,  # High Kindred's Crest
                    4: 2957,  # Sacred Kindred's Crest
                    5: 1857,  # Cordial Invite
                    6: 2306,  # Martial Ball Invite
                    7: 5364,  # Training Grounds Key
                    8: 2487,  # Mercenary Camp Entry Slip
                    9: 5741,  # Flask Of Pest Repellent
                    10: 3557,  # Athena Orb
                    11: 5113,  # Cracked Nut
                    12: 3541,  # Seasoning Stone
                    13: 3543,  # Fossilized Fang
                    14: 3542,  # Fossilized Bone
                    15: 5724,  # Pungent Powder
                    16: 6535,  # Pungent Powder II
                    17: 26489,  # Troth
                    18: 28661,  # Glinting Shield
                },
            },
            5: {
                100: {
                    0: 8734,  # Mog Kupon I - S1
                    1: 8966,  # Eudaemon Blade
                    2: 8967,  # Eudaemon Cape
                    3: 8968,  # Eudaemon Ring
                    4: 8969,  # Eudaemon Sash
                    5: 8970,  # Eudaemon Shield
                    6: 17006,  # Drill Calamary
                    7: 17007,  # Dwarf Pugil
                    8: 10112,  # Cipher: Zeid
                    9: 10113,  # Cipher: Lion
                    10: 10118,  # Cipher: Naja
                    11: 10120,  # Cipher: Lehko
                    12: 10124,  # Cipher: Luzaf
                    13: 10125,  # Cipher: Najelith
                    14: 10129,  # Cipher: Domina
                    15: 10134,  # Cipher: S. Sibyl
                    16: 10142,  # Cipher: Karaha
                    17: 10149,  # Cipher: Areuhat
                    18: 10136,  # Cipher: Uka
                    19: 10141,  # Cipher: Kuyin
                },
            },
            9: {
                100: {
                    0: 10144,  # Cipher: Abenzio
                    1: 10145,  # Cipher: Rughadjeen
                    2: 10150,  # Cipher: Lhe
                    3: 10151,  # Cipher: Mayakov
                    4: 10155,  # Cipher: Brygid
                    5: 10156,  # Cipher: Mildaurion
                    6: 10161,  # Cipher: Rongelouts
                    7: 10166,  # Cipher: Robel-Akbel
                    8: 10178,  # Cipher: Ullegore
                    9: 10179,  # Cipher: Teodor
                    10: 10183,  # Cipher: Darrcuiln
                },
            },
            13: {
                300: {
                    0: 5854,  # Frayed Pouch (B)
                    1: 5855,  # Frayed Pouch (A)
                    2: 5856,  # Frayed Pouch (G)
                    3: 5857,  # Frayed Pouch (D)
                    4: 5858,  # Frayed Pouch (R)
                    5: 5946,  # Frayed Sack (D)
                    6: 5947,  # Frayed Sack (L)
                    7: 4064,  # Rem's Tale Ch.1
                    8: 4065,  # Rem's Tale Ch.2
                    9: 4066,  # Rem's Tale Ch.3
                    10: 4067,  # Rem's Tale Ch.4
                    11: 4068,  # Rem's Tale Ch.5
                    12: 10187,  # Cipher: Shantotto II
                },
            },
            17: {
                500: {
                    0: 23800,  # Cancrine Apron
                    1: 3749,  # Chemistry Set
                    2: 10079,  # ♪Iron Giant
                },
            },
            21: {
                750: {
                    0: 3885,  # Melodious Plans
                    1: 3886,  # Timbre Case Kit
                    2: 3887,  # Musichinery Kit
                    3: 3339,  # Honey Wine
                    4: 3341,  # Beastly Shank
                    5: 3343,  # Blue Pondweed
                    6: 1873,  # Brigand's Chart
                    7: 1874,  # Pirate's Chart
                    8: 4069,  # Copy Of Rem's Tale, Chapter 6
                    9: 4070,  # Copy Of Rem's Tale, Chapter 7
                    10: 4071,  # Copy Of Rem's Tale, Chapter 8
                    11: 4072,  # Copy Of Rem's Tale, Chapter 9
                    12: 4073,  # Copy Of Rem's Tale, Chapter 10
                },
            },
            25: {
                1000: {
                    0: 6499,  # Patio Design Plans
                    1: 26164,  # Caliber Ring
                    2: 26165,  # Facility Ring
                }
            },
            29: {
                1500: {
                    0: 3340,  # Sweet Tea
                    1: 3342,  # Savory Shank
                    2: 3344,  # Red Pondweed
                }
            }
        }
    }
}


def create_file(year, month, file):
    f = open(file + "/scripts/globals/events/login_campaign_data.lua", "w")

    f.write("local prizes =\n")
    f.write("{\n")

    for option_id in data[year][month]:
        f.write("    [{0}] =\n".format(option_id))
        f.write("    {\n")
        for price in data[year][month][option_id]:
            f.write("        [\"price\"] = {0},\n".format(price))
            f.write("        [\"items\"] =\n")
            f.write("        {\n")
            for i in data[year][month][option_id][price]:
                f.write("            {0},\n".format(data[year][month][option_id][price][i]))
            f.write("        },\n")
        f.write("    },\n")

    f.write("}\n")
    f.write("return prizes")


def enable_login_campaign(file):
    for line in fileinput.input(file + "/scripts/settings/main.lua", True):
        print(line.replace("ENABLE_LOGIN_CAMPAIGN = 0,", "ENABLE_LOGIN_CAMPAIGN = 1,").rstrip())


def change_campaign_date(year, month, day, duration, file):
    for line in fileinput.input(file + "/scripts/globals/events/login_campaign.lua", True):
        if line.find("loginCampaignYear") != -1:
            print(line.replace("loginCampaignYear = 2021", "loginCampaignYear = " + str(year)).rstrip())
        elif line.find("loginCampaignMonth") != -1:
            print(line.replace("loginCampaignMonth = 8", "loginCampaignMonth = " + str(month)).rstrip())
        elif line.find("loginCampaignDay") != -1:
            print(line.replace("loginCampaignDay = 25", "loginCampaignDay = " + str(day)).rstrip())
        elif line.find("loginCampaignDuration") != -1:
            print(line.replace("loginCampaignDuration = 23", "loginCampaignDuration = " + str(duration)).rstrip())
        else:
            print(line.rstrip())

"""
Eastern Europe & Sovereign Aggression Sanctions.
Russian Harmful Foreign Activities EO 14024.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class SanctionedItem:
    sdn_id: int
    name: str
    sdn_type: str
    programs: List[str]
    remarks: Optional[str] = None
    dob_list: List[str] = field(default_factory=list)
    citizenships: List[str] = field(default_factory=list)
    identifications: Dict[str, str] = field(default_factory=dict)
    aliases: List[str] = field(default_factory=list)

RECORDS_EASTERN_EUROPE_SANCTIONS: Dict[int, SanctionedItem] = {
    11000: SanctionedItem(
        sdn_id=11000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11000", "LEI": "54930000011000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    11001: SanctionedItem(
        sdn_id=11001,
        name="Viktor Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11001"},
        aliases=["Ivanov, Viktor", "V. Ivanov"]
    ),
    11002: SanctionedItem(
        sdn_id=11002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11002", "LEI": "54930000011002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    11003: SanctionedItem(
        sdn_id=11003,
        name="Dmitry Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11003"},
        aliases=["Smirnov, Dmitry", "D. Smirnov"]
    ),
    11004: SanctionedItem(
        sdn_id=11004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11004", "LEI": "54930000011004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    11005: SanctionedItem(
        sdn_id=11005,
        name="Sergei Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11005"},
        aliases=["Sokolov, Sergei", "S. Sokolov"]
    ),
    11006: SanctionedItem(
        sdn_id=11006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11006", "LEI": "54930000011006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    11007: SanctionedItem(
        sdn_id=11007,
        name="Alexander Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11007"},
        aliases=["Soleimani, Alexander", "A. Soleimani"]
    ),
    11008: SanctionedItem(
        sdn_id=11008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11008", "LEI": "54930000011008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    11009: SanctionedItem(
        sdn_id=11009,
        name="Mohammad Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11009"},
        aliases=["Najafi, Mohammad", "M. Najafi"]
    ),
    11010: SanctionedItem(
        sdn_id=11010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11010", "LEI": "54930000011010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    11011: SanctionedItem(
        sdn_id=11011,
        name="Hassan Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11011"},
        aliases=["Il-sung, Hassan", "H. Il-sung"]
    ),
    11012: SanctionedItem(
        sdn_id=11012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11012", "LEI": "54930000011012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    11013: SanctionedItem(
        sdn_id=11013,
        name="Ali Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11013"},
        aliases=["Wei, Ali", "A. Wei"]
    ),
    11014: SanctionedItem(
        sdn_id=11014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11014", "LEI": "54930000011014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    11015: SanctionedItem(
        sdn_id=11015,
        name="Ahmad Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11015"},
        aliases=["Qiang, Ahmad", "A. Qiang"]
    ),
    11016: SanctionedItem(
        sdn_id=11016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11016", "LEI": "54930000011016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    11017: SanctionedItem(
        sdn_id=11017,
        name="Kim Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11017"},
        aliases=["Cabello, Kim", "K. Cabello"]
    ),
    11018: SanctionedItem(
        sdn_id=11018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11018", "LEI": "54930000011018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    11019: SanctionedItem(
        sdn_id=11019,
        name="Park Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11019"},
        aliases=["Lopez, Park", "P. Lopez"]
    ),
    11020: SanctionedItem(
        sdn_id=11020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11020", "LEI": "54930000011020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    11021: SanctionedItem(
        sdn_id=11021,
        name="Chen Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11021"},
        aliases=["Ivanov, Chen", "C. Ivanov"]
    ),
    11022: SanctionedItem(
        sdn_id=11022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11022", "LEI": "54930000011022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    11023: SanctionedItem(
        sdn_id=11023,
        name="Wang Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11023"},
        aliases=["Smirnov, Wang", "W. Smirnov"]
    ),
    11024: SanctionedItem(
        sdn_id=11024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11024", "LEI": "54930000011024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    11025: SanctionedItem(
        sdn_id=11025,
        name="Zhang Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11025"},
        aliases=["Sokolov, Zhang", "Z. Sokolov"]
    ),
    11026: SanctionedItem(
        sdn_id=11026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11026", "LEI": "54930000011026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    11027: SanctionedItem(
        sdn_id=11027,
        name="Carlos Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11027"},
        aliases=["Soleimani, Carlos", "C. Soleimani"]
    ),
    11028: SanctionedItem(
        sdn_id=11028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11028", "LEI": "54930000011028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    11029: SanctionedItem(
        sdn_id=11029,
        name="Raul Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11029"},
        aliases=["Najafi, Raul", "R. Najafi"]
    ),
    11030: SanctionedItem(
        sdn_id=11030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11030", "LEI": "54930000011030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    11031: SanctionedItem(
        sdn_id=11031,
        name="Ernesto Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11031"},
        aliases=["Il-sung, Ernesto", "E. Il-sung"]
    ),
    11032: SanctionedItem(
        sdn_id=11032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11032", "LEI": "54930000011032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    11033: SanctionedItem(
        sdn_id=11033,
        name="Ibrahim Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11033"},
        aliases=["Wei, Ibrahim", "I. Wei"]
    ),
    11034: SanctionedItem(
        sdn_id=11034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11034", "LEI": "54930000011034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    11035: SanctionedItem(
        sdn_id=11035,
        name="Tariq Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11035"},
        aliases=["Qiang, Tariq", "T. Qiang"]
    ),
    11036: SanctionedItem(
        sdn_id=11036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11036", "LEI": "54930000011036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    11037: SanctionedItem(
        sdn_id=11037,
        name="Nikolai Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11037"},
        aliases=["Cabello, Nikolai", "N. Cabello"]
    ),
    11038: SanctionedItem(
        sdn_id=11038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11038", "LEI": "54930000011038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    11039: SanctionedItem(
        sdn_id=11039,
        name="Vladimir Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11039"},
        aliases=["Lopez, Vladimir", "V. Lopez"]
    ),
    11040: SanctionedItem(
        sdn_id=11040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11040", "LEI": "54930000011040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    11041: SanctionedItem(
        sdn_id=11041,
        name="Andrei Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11041"},
        aliases=["Ivanov, Andrei", "A. Ivanov"]
    ),
    11042: SanctionedItem(
        sdn_id=11042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11042", "LEI": "54930000011042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    11043: SanctionedItem(
        sdn_id=11043,
        name="Mikhail Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11043"},
        aliases=["Smirnov, Mikhail", "M. Smirnov"]
    ),
    11044: SanctionedItem(
        sdn_id=11044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11044", "LEI": "54930000011044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    11045: SanctionedItem(
        sdn_id=11045,
        name="Reza Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11045"},
        aliases=["Sokolov, Reza", "R. Sokolov"]
    ),
    11046: SanctionedItem(
        sdn_id=11046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11046", "LEI": "54930000011046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    11047: SanctionedItem(
        sdn_id=11047,
        name="Farhad Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11047"},
        aliases=["Soleimani, Farhad", "F. Soleimani"]
    ),
    11048: SanctionedItem(
        sdn_id=11048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11048", "LEI": "54930000011048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    11049: SanctionedItem(
        sdn_id=11049,
        name="Mahmoud Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11049"},
        aliases=["Najafi, Mahmoud", "M. Najafi"]
    ),
    11050: SanctionedItem(
        sdn_id=11050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11050", "LEI": "54930000011050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    11051: SanctionedItem(
        sdn_id=11051,
        name="Slobodan Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11051"},
        aliases=["Il-sung, Slobodan", "S. Il-sung"]
    ),
    11052: SanctionedItem(
        sdn_id=11052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11052", "LEI": "54930000011052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    11053: SanctionedItem(
        sdn_id=11053,
        name="Radovan Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11053"},
        aliases=["Wei, Radovan", "R. Wei"]
    ),
    11054: SanctionedItem(
        sdn_id=11054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11054", "LEI": "54930000011054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    11055: SanctionedItem(
        sdn_id=11055,
        name="Goran Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11055"},
        aliases=["Qiang, Goran", "G. Qiang"]
    ),
    11056: SanctionedItem(
        sdn_id=11056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11056", "LEI": "54930000011056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    11057: SanctionedItem(
        sdn_id=11057,
        name="Milorad Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11057"},
        aliases=["Cabello, Milorad", "M. Cabello"]
    ),
    11058: SanctionedItem(
        sdn_id=11058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11058", "LEI": "54930000011058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    11059: SanctionedItem(
        sdn_id=11059,
        name="Jean-Pierre Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11059"},
        aliases=["Lopez, Jean-Pierre", "J. Lopez"]
    ),
    11060: SanctionedItem(
        sdn_id=11060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11060", "LEI": "54930000011060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    11061: SanctionedItem(
        sdn_id=11061,
        name="Viktor Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11061"},
        aliases=["Ivanov, Viktor", "V. Ivanov"]
    ),
    11062: SanctionedItem(
        sdn_id=11062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11062", "LEI": "54930000011062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    11063: SanctionedItem(
        sdn_id=11063,
        name="Dmitry Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11063"},
        aliases=["Smirnov, Dmitry", "D. Smirnov"]
    ),
    11064: SanctionedItem(
        sdn_id=11064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11064", "LEI": "54930000011064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    11065: SanctionedItem(
        sdn_id=11065,
        name="Sergei Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11065"},
        aliases=["Sokolov, Sergei", "S. Sokolov"]
    ),
    11066: SanctionedItem(
        sdn_id=11066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11066", "LEI": "54930000011066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    11067: SanctionedItem(
        sdn_id=11067,
        name="Alexander Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11067"},
        aliases=["Soleimani, Alexander", "A. Soleimani"]
    ),
    11068: SanctionedItem(
        sdn_id=11068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11068", "LEI": "54930000011068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    11069: SanctionedItem(
        sdn_id=11069,
        name="Mohammad Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11069"},
        aliases=["Najafi, Mohammad", "M. Najafi"]
    ),
    11070: SanctionedItem(
        sdn_id=11070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11070", "LEI": "54930000011070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    11071: SanctionedItem(
        sdn_id=11071,
        name="Hassan Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11071"},
        aliases=["Il-sung, Hassan", "H. Il-sung"]
    ),
    11072: SanctionedItem(
        sdn_id=11072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11072", "LEI": "54930000011072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    11073: SanctionedItem(
        sdn_id=11073,
        name="Ali Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11073"},
        aliases=["Wei, Ali", "A. Wei"]
    ),
    11074: SanctionedItem(
        sdn_id=11074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11074", "LEI": "54930000011074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    11075: SanctionedItem(
        sdn_id=11075,
        name="Ahmad Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11075"},
        aliases=["Qiang, Ahmad", "A. Qiang"]
    ),
    11076: SanctionedItem(
        sdn_id=11076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11076", "LEI": "54930000011076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    11077: SanctionedItem(
        sdn_id=11077,
        name="Kim Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11077"},
        aliases=["Cabello, Kim", "K. Cabello"]
    ),
    11078: SanctionedItem(
        sdn_id=11078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11078", "LEI": "54930000011078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    11079: SanctionedItem(
        sdn_id=11079,
        name="Park Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11079"},
        aliases=["Lopez, Park", "P. Lopez"]
    ),
    11080: SanctionedItem(
        sdn_id=11080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11080", "LEI": "54930000011080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    11081: SanctionedItem(
        sdn_id=11081,
        name="Chen Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11081"},
        aliases=["Ivanov, Chen", "C. Ivanov"]
    ),
    11082: SanctionedItem(
        sdn_id=11082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11082", "LEI": "54930000011082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    11083: SanctionedItem(
        sdn_id=11083,
        name="Wang Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11083"},
        aliases=["Smirnov, Wang", "W. Smirnov"]
    ),
    11084: SanctionedItem(
        sdn_id=11084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11084", "LEI": "54930000011084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    11085: SanctionedItem(
        sdn_id=11085,
        name="Zhang Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11085"},
        aliases=["Sokolov, Zhang", "Z. Sokolov"]
    ),
    11086: SanctionedItem(
        sdn_id=11086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11086", "LEI": "54930000011086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    11087: SanctionedItem(
        sdn_id=11087,
        name="Carlos Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11087"},
        aliases=["Soleimani, Carlos", "C. Soleimani"]
    ),
    11088: SanctionedItem(
        sdn_id=11088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11088", "LEI": "54930000011088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    11089: SanctionedItem(
        sdn_id=11089,
        name="Raul Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11089"},
        aliases=["Najafi, Raul", "R. Najafi"]
    ),
    11090: SanctionedItem(
        sdn_id=11090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11090", "LEI": "54930000011090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    11091: SanctionedItem(
        sdn_id=11091,
        name="Ernesto Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11091"},
        aliases=["Il-sung, Ernesto", "E. Il-sung"]
    ),
    11092: SanctionedItem(
        sdn_id=11092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11092", "LEI": "54930000011092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    11093: SanctionedItem(
        sdn_id=11093,
        name="Ibrahim Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11093"},
        aliases=["Wei, Ibrahim", "I. Wei"]
    ),
    11094: SanctionedItem(
        sdn_id=11094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11094", "LEI": "54930000011094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    11095: SanctionedItem(
        sdn_id=11095,
        name="Tariq Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11095"},
        aliases=["Qiang, Tariq", "T. Qiang"]
    ),
    11096: SanctionedItem(
        sdn_id=11096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11096", "LEI": "54930000011096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    11097: SanctionedItem(
        sdn_id=11097,
        name="Nikolai Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11097"},
        aliases=["Cabello, Nikolai", "N. Cabello"]
    ),
    11098: SanctionedItem(
        sdn_id=11098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11098", "LEI": "54930000011098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    11099: SanctionedItem(
        sdn_id=11099,
        name="Vladimir Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11099"},
        aliases=["Lopez, Vladimir", "V. Lopez"]
    ),
    11100: SanctionedItem(
        sdn_id=11100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11100", "LEI": "54930000011100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    11101: SanctionedItem(
        sdn_id=11101,
        name="Andrei Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11101"},
        aliases=["Ivanov, Andrei", "A. Ivanov"]
    ),
    11102: SanctionedItem(
        sdn_id=11102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11102", "LEI": "54930000011102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    11103: SanctionedItem(
        sdn_id=11103,
        name="Mikhail Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11103"},
        aliases=["Smirnov, Mikhail", "M. Smirnov"]
    ),
    11104: SanctionedItem(
        sdn_id=11104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11104", "LEI": "54930000011104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    11105: SanctionedItem(
        sdn_id=11105,
        name="Reza Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11105"},
        aliases=["Sokolov, Reza", "R. Sokolov"]
    ),
    11106: SanctionedItem(
        sdn_id=11106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11106", "LEI": "54930000011106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    11107: SanctionedItem(
        sdn_id=11107,
        name="Farhad Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11107"},
        aliases=["Soleimani, Farhad", "F. Soleimani"]
    ),
    11108: SanctionedItem(
        sdn_id=11108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11108", "LEI": "54930000011108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    11109: SanctionedItem(
        sdn_id=11109,
        name="Mahmoud Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11109"},
        aliases=["Najafi, Mahmoud", "M. Najafi"]
    ),
    11110: SanctionedItem(
        sdn_id=11110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11110", "LEI": "54930000011110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    11111: SanctionedItem(
        sdn_id=11111,
        name="Slobodan Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11111"},
        aliases=["Il-sung, Slobodan", "S. Il-sung"]
    ),
    11112: SanctionedItem(
        sdn_id=11112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11112", "LEI": "54930000011112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    11113: SanctionedItem(
        sdn_id=11113,
        name="Radovan Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11113"},
        aliases=["Wei, Radovan", "R. Wei"]
    ),
    11114: SanctionedItem(
        sdn_id=11114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11114", "LEI": "54930000011114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    11115: SanctionedItem(
        sdn_id=11115,
        name="Goran Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11115"},
        aliases=["Qiang, Goran", "G. Qiang"]
    ),
    11116: SanctionedItem(
        sdn_id=11116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11116", "LEI": "54930000011116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    11117: SanctionedItem(
        sdn_id=11117,
        name="Milorad Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11117"},
        aliases=["Cabello, Milorad", "M. Cabello"]
    ),
    11118: SanctionedItem(
        sdn_id=11118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11118", "LEI": "54930000011118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    11119: SanctionedItem(
        sdn_id=11119,
        name="Jean-Pierre Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11119"},
        aliases=["Lopez, Jean-Pierre", "J. Lopez"]
    ),
    11120: SanctionedItem(
        sdn_id=11120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11120", "LEI": "54930000011120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    11121: SanctionedItem(
        sdn_id=11121,
        name="Viktor Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11121"},
        aliases=["Ivanov, Viktor", "V. Ivanov"]
    ),
    11122: SanctionedItem(
        sdn_id=11122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11122", "LEI": "54930000011122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    11123: SanctionedItem(
        sdn_id=11123,
        name="Dmitry Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11123"},
        aliases=["Smirnov, Dmitry", "D. Smirnov"]
    ),
    11124: SanctionedItem(
        sdn_id=11124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11124", "LEI": "54930000011124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    11125: SanctionedItem(
        sdn_id=11125,
        name="Sergei Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11125"},
        aliases=["Sokolov, Sergei", "S. Sokolov"]
    ),
    11126: SanctionedItem(
        sdn_id=11126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11126", "LEI": "54930000011126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    11127: SanctionedItem(
        sdn_id=11127,
        name="Alexander Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11127"},
        aliases=["Soleimani, Alexander", "A. Soleimani"]
    ),
    11128: SanctionedItem(
        sdn_id=11128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11128", "LEI": "54930000011128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    11129: SanctionedItem(
        sdn_id=11129,
        name="Mohammad Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11129"},
        aliases=["Najafi, Mohammad", "M. Najafi"]
    ),
    11130: SanctionedItem(
        sdn_id=11130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11130", "LEI": "54930000011130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    11131: SanctionedItem(
        sdn_id=11131,
        name="Hassan Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11131"},
        aliases=["Il-sung, Hassan", "H. Il-sung"]
    ),
    11132: SanctionedItem(
        sdn_id=11132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11132", "LEI": "54930000011132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    11133: SanctionedItem(
        sdn_id=11133,
        name="Ali Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11133"},
        aliases=["Wei, Ali", "A. Wei"]
    ),
    11134: SanctionedItem(
        sdn_id=11134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11134", "LEI": "54930000011134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    11135: SanctionedItem(
        sdn_id=11135,
        name="Ahmad Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11135"},
        aliases=["Qiang, Ahmad", "A. Qiang"]
    ),
    11136: SanctionedItem(
        sdn_id=11136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11136", "LEI": "54930000011136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    11137: SanctionedItem(
        sdn_id=11137,
        name="Kim Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11137"},
        aliases=["Cabello, Kim", "K. Cabello"]
    ),
    11138: SanctionedItem(
        sdn_id=11138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11138", "LEI": "54930000011138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    11139: SanctionedItem(
        sdn_id=11139,
        name="Park Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11139"},
        aliases=["Lopez, Park", "P. Lopez"]
    ),
    11140: SanctionedItem(
        sdn_id=11140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11140", "LEI": "54930000011140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    11141: SanctionedItem(
        sdn_id=11141,
        name="Chen Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11141"},
        aliases=["Ivanov, Chen", "C. Ivanov"]
    ),
    11142: SanctionedItem(
        sdn_id=11142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11142", "LEI": "54930000011142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    11143: SanctionedItem(
        sdn_id=11143,
        name="Wang Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11143"},
        aliases=["Smirnov, Wang", "W. Smirnov"]
    ),
    11144: SanctionedItem(
        sdn_id=11144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11144", "LEI": "54930000011144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    11145: SanctionedItem(
        sdn_id=11145,
        name="Zhang Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11145"},
        aliases=["Sokolov, Zhang", "Z. Sokolov"]
    ),
    11146: SanctionedItem(
        sdn_id=11146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11146", "LEI": "54930000011146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    11147: SanctionedItem(
        sdn_id=11147,
        name="Carlos Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11147"},
        aliases=["Soleimani, Carlos", "C. Soleimani"]
    ),
    11148: SanctionedItem(
        sdn_id=11148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11148", "LEI": "54930000011148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    11149: SanctionedItem(
        sdn_id=11149,
        name="Raul Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11149"},
        aliases=["Najafi, Raul", "R. Najafi"]
    ),
    11150: SanctionedItem(
        sdn_id=11150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11150", "LEI": "54930000011150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    11151: SanctionedItem(
        sdn_id=11151,
        name="Ernesto Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11151"},
        aliases=["Il-sung, Ernesto", "E. Il-sung"]
    ),
    11152: SanctionedItem(
        sdn_id=11152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11152", "LEI": "54930000011152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    11153: SanctionedItem(
        sdn_id=11153,
        name="Ibrahim Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11153"},
        aliases=["Wei, Ibrahim", "I. Wei"]
    ),
    11154: SanctionedItem(
        sdn_id=11154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11154", "LEI": "54930000011154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    11155: SanctionedItem(
        sdn_id=11155,
        name="Tariq Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11155"},
        aliases=["Qiang, Tariq", "T. Qiang"]
    ),
    11156: SanctionedItem(
        sdn_id=11156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11156", "LEI": "54930000011156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    11157: SanctionedItem(
        sdn_id=11157,
        name="Nikolai Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11157"},
        aliases=["Cabello, Nikolai", "N. Cabello"]
    ),
    11158: SanctionedItem(
        sdn_id=11158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11158", "LEI": "54930000011158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    11159: SanctionedItem(
        sdn_id=11159,
        name="Vladimir Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11159"},
        aliases=["Lopez, Vladimir", "V. Lopez"]
    ),
    11160: SanctionedItem(
        sdn_id=11160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11160", "LEI": "54930000011160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    11161: SanctionedItem(
        sdn_id=11161,
        name="Andrei Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11161"},
        aliases=["Ivanov, Andrei", "A. Ivanov"]
    ),
    11162: SanctionedItem(
        sdn_id=11162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11162", "LEI": "54930000011162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    11163: SanctionedItem(
        sdn_id=11163,
        name="Mikhail Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11163"},
        aliases=["Smirnov, Mikhail", "M. Smirnov"]
    ),
    11164: SanctionedItem(
        sdn_id=11164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11164", "LEI": "54930000011164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    11165: SanctionedItem(
        sdn_id=11165,
        name="Reza Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11165"},
        aliases=["Sokolov, Reza", "R. Sokolov"]
    ),
    11166: SanctionedItem(
        sdn_id=11166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11166", "LEI": "54930000011166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    11167: SanctionedItem(
        sdn_id=11167,
        name="Farhad Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11167"},
        aliases=["Soleimani, Farhad", "F. Soleimani"]
    ),
    11168: SanctionedItem(
        sdn_id=11168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11168", "LEI": "54930000011168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    11169: SanctionedItem(
        sdn_id=11169,
        name="Mahmoud Najafi",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11169"},
        aliases=["Najafi, Mahmoud", "M. Najafi"]
    ),
    11170: SanctionedItem(
        sdn_id=11170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11170", "LEI": "54930000011170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    11171: SanctionedItem(
        sdn_id=11171,
        name="Slobodan Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11171"},
        aliases=["Il-sung, Slobodan", "S. Il-sung"]
    ),
    11172: SanctionedItem(
        sdn_id=11172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11172", "LEI": "54930000011172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    11173: SanctionedItem(
        sdn_id=11173,
        name="Radovan Wei",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11173"},
        aliases=["Wei, Radovan", "R. Wei"]
    ),
    11174: SanctionedItem(
        sdn_id=11174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11174", "LEI": "54930000011174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    11175: SanctionedItem(
        sdn_id=11175,
        name="Goran Qiang",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11175"},
        aliases=["Qiang, Goran", "G. Qiang"]
    ),
    11176: SanctionedItem(
        sdn_id=11176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11176", "LEI": "54930000011176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    11177: SanctionedItem(
        sdn_id=11177,
        name="Milorad Cabello",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11177"},
        aliases=["Cabello, Milorad", "M. Cabello"]
    ),
    11178: SanctionedItem(
        sdn_id=11178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["RUSSIA-EO14024"],
        remarks="Designated entity under RUSSIA-EO14024 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-11178", "LEI": "54930000011178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    11179: SanctionedItem(
        sdn_id=11179,
        name="Jean-Pierre Lopez",
        sdn_type="INDIVIDUAL",
        programs=["RUSSIA-EO14024"],
        remarks="Designated individual under RUSSIA-EO14024; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-11179"},
        aliases=["Lopez, Jean-Pierre", "J. Lopez"]
    ),
}

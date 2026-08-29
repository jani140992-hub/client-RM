"""
Latin America Democratic Protection Sanctions.
Blocking Property of the Government of Venezuela.
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

RECORDS_LATIN_AMERICA_SANCTIONS: Dict[int, SanctionedItem] = {
    14000: SanctionedItem(
        sdn_id=14000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14000", "LEI": "54930000014000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    14001: SanctionedItem(
        sdn_id=14001,
        name="Viktor Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14001"},
        aliases=["Smirnov, Viktor", "V. Smirnov"]
    ),
    14002: SanctionedItem(
        sdn_id=14002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14002", "LEI": "54930000014002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    14003: SanctionedItem(
        sdn_id=14003,
        name="Dmitry Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14003"},
        aliases=["Sokolov, Dmitry", "D. Sokolov"]
    ),
    14004: SanctionedItem(
        sdn_id=14004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14004", "LEI": "54930000014004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    14005: SanctionedItem(
        sdn_id=14005,
        name="Sergei Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14005"},
        aliases=["Soleimani, Sergei", "S. Soleimani"]
    ),
    14006: SanctionedItem(
        sdn_id=14006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14006", "LEI": "54930000014006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    14007: SanctionedItem(
        sdn_id=14007,
        name="Alexander Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14007"},
        aliases=["Najafi, Alexander", "A. Najafi"]
    ),
    14008: SanctionedItem(
        sdn_id=14008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14008", "LEI": "54930000014008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    14009: SanctionedItem(
        sdn_id=14009,
        name="Mohammad Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14009"},
        aliases=["Il-sung, Mohammad", "M. Il-sung"]
    ),
    14010: SanctionedItem(
        sdn_id=14010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14010", "LEI": "54930000014010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    14011: SanctionedItem(
        sdn_id=14011,
        name="Hassan Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14011"},
        aliases=["Wei, Hassan", "H. Wei"]
    ),
    14012: SanctionedItem(
        sdn_id=14012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14012", "LEI": "54930000014012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    14013: SanctionedItem(
        sdn_id=14013,
        name="Ali Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14013"},
        aliases=["Qiang, Ali", "A. Qiang"]
    ),
    14014: SanctionedItem(
        sdn_id=14014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14014", "LEI": "54930000014014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    14015: SanctionedItem(
        sdn_id=14015,
        name="Ahmad Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14015"},
        aliases=["Cabello, Ahmad", "A. Cabello"]
    ),
    14016: SanctionedItem(
        sdn_id=14016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14016", "LEI": "54930000014016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    14017: SanctionedItem(
        sdn_id=14017,
        name="Kim Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14017"},
        aliases=["Lopez, Kim", "K. Lopez"]
    ),
    14018: SanctionedItem(
        sdn_id=14018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14018", "LEI": "54930000014018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    14019: SanctionedItem(
        sdn_id=14019,
        name="Park Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14019"},
        aliases=["Ivanov, Park", "P. Ivanov"]
    ),
    14020: SanctionedItem(
        sdn_id=14020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14020", "LEI": "54930000014020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    14021: SanctionedItem(
        sdn_id=14021,
        name="Chen Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14021"},
        aliases=["Smirnov, Chen", "C. Smirnov"]
    ),
    14022: SanctionedItem(
        sdn_id=14022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14022", "LEI": "54930000014022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    14023: SanctionedItem(
        sdn_id=14023,
        name="Wang Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14023"},
        aliases=["Sokolov, Wang", "W. Sokolov"]
    ),
    14024: SanctionedItem(
        sdn_id=14024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14024", "LEI": "54930000014024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    14025: SanctionedItem(
        sdn_id=14025,
        name="Zhang Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14025"},
        aliases=["Soleimani, Zhang", "Z. Soleimani"]
    ),
    14026: SanctionedItem(
        sdn_id=14026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14026", "LEI": "54930000014026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    14027: SanctionedItem(
        sdn_id=14027,
        name="Carlos Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14027"},
        aliases=["Najafi, Carlos", "C. Najafi"]
    ),
    14028: SanctionedItem(
        sdn_id=14028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14028", "LEI": "54930000014028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    14029: SanctionedItem(
        sdn_id=14029,
        name="Raul Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14029"},
        aliases=["Il-sung, Raul", "R. Il-sung"]
    ),
    14030: SanctionedItem(
        sdn_id=14030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14030", "LEI": "54930000014030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    14031: SanctionedItem(
        sdn_id=14031,
        name="Ernesto Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14031"},
        aliases=["Wei, Ernesto", "E. Wei"]
    ),
    14032: SanctionedItem(
        sdn_id=14032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14032", "LEI": "54930000014032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    14033: SanctionedItem(
        sdn_id=14033,
        name="Ibrahim Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14033"},
        aliases=["Qiang, Ibrahim", "I. Qiang"]
    ),
    14034: SanctionedItem(
        sdn_id=14034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14034", "LEI": "54930000014034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    14035: SanctionedItem(
        sdn_id=14035,
        name="Tariq Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14035"},
        aliases=["Cabello, Tariq", "T. Cabello"]
    ),
    14036: SanctionedItem(
        sdn_id=14036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14036", "LEI": "54930000014036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    14037: SanctionedItem(
        sdn_id=14037,
        name="Nikolai Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14037"},
        aliases=["Lopez, Nikolai", "N. Lopez"]
    ),
    14038: SanctionedItem(
        sdn_id=14038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14038", "LEI": "54930000014038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    14039: SanctionedItem(
        sdn_id=14039,
        name="Vladimir Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14039"},
        aliases=["Ivanov, Vladimir", "V. Ivanov"]
    ),
    14040: SanctionedItem(
        sdn_id=14040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14040", "LEI": "54930000014040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    14041: SanctionedItem(
        sdn_id=14041,
        name="Andrei Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14041"},
        aliases=["Smirnov, Andrei", "A. Smirnov"]
    ),
    14042: SanctionedItem(
        sdn_id=14042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14042", "LEI": "54930000014042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    14043: SanctionedItem(
        sdn_id=14043,
        name="Mikhail Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14043"},
        aliases=["Sokolov, Mikhail", "M. Sokolov"]
    ),
    14044: SanctionedItem(
        sdn_id=14044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14044", "LEI": "54930000014044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    14045: SanctionedItem(
        sdn_id=14045,
        name="Reza Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14045"},
        aliases=["Soleimani, Reza", "R. Soleimani"]
    ),
    14046: SanctionedItem(
        sdn_id=14046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14046", "LEI": "54930000014046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    14047: SanctionedItem(
        sdn_id=14047,
        name="Farhad Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14047"},
        aliases=["Najafi, Farhad", "F. Najafi"]
    ),
    14048: SanctionedItem(
        sdn_id=14048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14048", "LEI": "54930000014048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    14049: SanctionedItem(
        sdn_id=14049,
        name="Mahmoud Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14049"},
        aliases=["Il-sung, Mahmoud", "M. Il-sung"]
    ),
    14050: SanctionedItem(
        sdn_id=14050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14050", "LEI": "54930000014050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    14051: SanctionedItem(
        sdn_id=14051,
        name="Slobodan Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14051"},
        aliases=["Wei, Slobodan", "S. Wei"]
    ),
    14052: SanctionedItem(
        sdn_id=14052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14052", "LEI": "54930000014052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    14053: SanctionedItem(
        sdn_id=14053,
        name="Radovan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14053"},
        aliases=["Qiang, Radovan", "R. Qiang"]
    ),
    14054: SanctionedItem(
        sdn_id=14054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14054", "LEI": "54930000014054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    14055: SanctionedItem(
        sdn_id=14055,
        name="Goran Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14055"},
        aliases=["Cabello, Goran", "G. Cabello"]
    ),
    14056: SanctionedItem(
        sdn_id=14056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14056", "LEI": "54930000014056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    14057: SanctionedItem(
        sdn_id=14057,
        name="Milorad Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14057"},
        aliases=["Lopez, Milorad", "M. Lopez"]
    ),
    14058: SanctionedItem(
        sdn_id=14058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14058", "LEI": "54930000014058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    14059: SanctionedItem(
        sdn_id=14059,
        name="Jean-Pierre Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14059"},
        aliases=["Ivanov, Jean-Pierre", "J. Ivanov"]
    ),
    14060: SanctionedItem(
        sdn_id=14060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14060", "LEI": "54930000014060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    14061: SanctionedItem(
        sdn_id=14061,
        name="Viktor Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14061"},
        aliases=["Smirnov, Viktor", "V. Smirnov"]
    ),
    14062: SanctionedItem(
        sdn_id=14062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14062", "LEI": "54930000014062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    14063: SanctionedItem(
        sdn_id=14063,
        name="Dmitry Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14063"},
        aliases=["Sokolov, Dmitry", "D. Sokolov"]
    ),
    14064: SanctionedItem(
        sdn_id=14064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14064", "LEI": "54930000014064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    14065: SanctionedItem(
        sdn_id=14065,
        name="Sergei Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14065"},
        aliases=["Soleimani, Sergei", "S. Soleimani"]
    ),
    14066: SanctionedItem(
        sdn_id=14066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14066", "LEI": "54930000014066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    14067: SanctionedItem(
        sdn_id=14067,
        name="Alexander Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14067"},
        aliases=["Najafi, Alexander", "A. Najafi"]
    ),
    14068: SanctionedItem(
        sdn_id=14068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14068", "LEI": "54930000014068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    14069: SanctionedItem(
        sdn_id=14069,
        name="Mohammad Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14069"},
        aliases=["Il-sung, Mohammad", "M. Il-sung"]
    ),
    14070: SanctionedItem(
        sdn_id=14070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14070", "LEI": "54930000014070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    14071: SanctionedItem(
        sdn_id=14071,
        name="Hassan Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14071"},
        aliases=["Wei, Hassan", "H. Wei"]
    ),
    14072: SanctionedItem(
        sdn_id=14072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14072", "LEI": "54930000014072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    14073: SanctionedItem(
        sdn_id=14073,
        name="Ali Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14073"},
        aliases=["Qiang, Ali", "A. Qiang"]
    ),
    14074: SanctionedItem(
        sdn_id=14074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14074", "LEI": "54930000014074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    14075: SanctionedItem(
        sdn_id=14075,
        name="Ahmad Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14075"},
        aliases=["Cabello, Ahmad", "A. Cabello"]
    ),
    14076: SanctionedItem(
        sdn_id=14076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14076", "LEI": "54930000014076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    14077: SanctionedItem(
        sdn_id=14077,
        name="Kim Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14077"},
        aliases=["Lopez, Kim", "K. Lopez"]
    ),
    14078: SanctionedItem(
        sdn_id=14078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14078", "LEI": "54930000014078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    14079: SanctionedItem(
        sdn_id=14079,
        name="Park Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14079"},
        aliases=["Ivanov, Park", "P. Ivanov"]
    ),
    14080: SanctionedItem(
        sdn_id=14080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14080", "LEI": "54930000014080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    14081: SanctionedItem(
        sdn_id=14081,
        name="Chen Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14081"},
        aliases=["Smirnov, Chen", "C. Smirnov"]
    ),
    14082: SanctionedItem(
        sdn_id=14082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14082", "LEI": "54930000014082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    14083: SanctionedItem(
        sdn_id=14083,
        name="Wang Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14083"},
        aliases=["Sokolov, Wang", "W. Sokolov"]
    ),
    14084: SanctionedItem(
        sdn_id=14084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14084", "LEI": "54930000014084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    14085: SanctionedItem(
        sdn_id=14085,
        name="Zhang Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14085"},
        aliases=["Soleimani, Zhang", "Z. Soleimani"]
    ),
    14086: SanctionedItem(
        sdn_id=14086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14086", "LEI": "54930000014086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    14087: SanctionedItem(
        sdn_id=14087,
        name="Carlos Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14087"},
        aliases=["Najafi, Carlos", "C. Najafi"]
    ),
    14088: SanctionedItem(
        sdn_id=14088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14088", "LEI": "54930000014088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    14089: SanctionedItem(
        sdn_id=14089,
        name="Raul Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14089"},
        aliases=["Il-sung, Raul", "R. Il-sung"]
    ),
    14090: SanctionedItem(
        sdn_id=14090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14090", "LEI": "54930000014090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    14091: SanctionedItem(
        sdn_id=14091,
        name="Ernesto Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14091"},
        aliases=["Wei, Ernesto", "E. Wei"]
    ),
    14092: SanctionedItem(
        sdn_id=14092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14092", "LEI": "54930000014092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    14093: SanctionedItem(
        sdn_id=14093,
        name="Ibrahim Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14093"},
        aliases=["Qiang, Ibrahim", "I. Qiang"]
    ),
    14094: SanctionedItem(
        sdn_id=14094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14094", "LEI": "54930000014094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    14095: SanctionedItem(
        sdn_id=14095,
        name="Tariq Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14095"},
        aliases=["Cabello, Tariq", "T. Cabello"]
    ),
    14096: SanctionedItem(
        sdn_id=14096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14096", "LEI": "54930000014096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    14097: SanctionedItem(
        sdn_id=14097,
        name="Nikolai Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14097"},
        aliases=["Lopez, Nikolai", "N. Lopez"]
    ),
    14098: SanctionedItem(
        sdn_id=14098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14098", "LEI": "54930000014098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    14099: SanctionedItem(
        sdn_id=14099,
        name="Vladimir Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14099"},
        aliases=["Ivanov, Vladimir", "V. Ivanov"]
    ),
    14100: SanctionedItem(
        sdn_id=14100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14100", "LEI": "54930000014100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    14101: SanctionedItem(
        sdn_id=14101,
        name="Andrei Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14101"},
        aliases=["Smirnov, Andrei", "A. Smirnov"]
    ),
    14102: SanctionedItem(
        sdn_id=14102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14102", "LEI": "54930000014102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    14103: SanctionedItem(
        sdn_id=14103,
        name="Mikhail Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14103"},
        aliases=["Sokolov, Mikhail", "M. Sokolov"]
    ),
    14104: SanctionedItem(
        sdn_id=14104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14104", "LEI": "54930000014104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    14105: SanctionedItem(
        sdn_id=14105,
        name="Reza Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14105"},
        aliases=["Soleimani, Reza", "R. Soleimani"]
    ),
    14106: SanctionedItem(
        sdn_id=14106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14106", "LEI": "54930000014106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    14107: SanctionedItem(
        sdn_id=14107,
        name="Farhad Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14107"},
        aliases=["Najafi, Farhad", "F. Najafi"]
    ),
    14108: SanctionedItem(
        sdn_id=14108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14108", "LEI": "54930000014108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    14109: SanctionedItem(
        sdn_id=14109,
        name="Mahmoud Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14109"},
        aliases=["Il-sung, Mahmoud", "M. Il-sung"]
    ),
    14110: SanctionedItem(
        sdn_id=14110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14110", "LEI": "54930000014110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    14111: SanctionedItem(
        sdn_id=14111,
        name="Slobodan Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14111"},
        aliases=["Wei, Slobodan", "S. Wei"]
    ),
    14112: SanctionedItem(
        sdn_id=14112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14112", "LEI": "54930000014112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    14113: SanctionedItem(
        sdn_id=14113,
        name="Radovan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14113"},
        aliases=["Qiang, Radovan", "R. Qiang"]
    ),
    14114: SanctionedItem(
        sdn_id=14114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14114", "LEI": "54930000014114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    14115: SanctionedItem(
        sdn_id=14115,
        name="Goran Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14115"},
        aliases=["Cabello, Goran", "G. Cabello"]
    ),
    14116: SanctionedItem(
        sdn_id=14116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14116", "LEI": "54930000014116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    14117: SanctionedItem(
        sdn_id=14117,
        name="Milorad Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14117"},
        aliases=["Lopez, Milorad", "M. Lopez"]
    ),
    14118: SanctionedItem(
        sdn_id=14118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14118", "LEI": "54930000014118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    14119: SanctionedItem(
        sdn_id=14119,
        name="Jean-Pierre Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14119"},
        aliases=["Ivanov, Jean-Pierre", "J. Ivanov"]
    ),
    14120: SanctionedItem(
        sdn_id=14120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14120", "LEI": "54930000014120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    14121: SanctionedItem(
        sdn_id=14121,
        name="Viktor Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14121"},
        aliases=["Smirnov, Viktor", "V. Smirnov"]
    ),
    14122: SanctionedItem(
        sdn_id=14122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14122", "LEI": "54930000014122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    14123: SanctionedItem(
        sdn_id=14123,
        name="Dmitry Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14123"},
        aliases=["Sokolov, Dmitry", "D. Sokolov"]
    ),
    14124: SanctionedItem(
        sdn_id=14124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14124", "LEI": "54930000014124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    14125: SanctionedItem(
        sdn_id=14125,
        name="Sergei Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14125"},
        aliases=["Soleimani, Sergei", "S. Soleimani"]
    ),
    14126: SanctionedItem(
        sdn_id=14126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14126", "LEI": "54930000014126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    14127: SanctionedItem(
        sdn_id=14127,
        name="Alexander Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14127"},
        aliases=["Najafi, Alexander", "A. Najafi"]
    ),
    14128: SanctionedItem(
        sdn_id=14128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14128", "LEI": "54930000014128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    14129: SanctionedItem(
        sdn_id=14129,
        name="Mohammad Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14129"},
        aliases=["Il-sung, Mohammad", "M. Il-sung"]
    ),
    14130: SanctionedItem(
        sdn_id=14130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14130", "LEI": "54930000014130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    14131: SanctionedItem(
        sdn_id=14131,
        name="Hassan Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14131"},
        aliases=["Wei, Hassan", "H. Wei"]
    ),
    14132: SanctionedItem(
        sdn_id=14132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14132", "LEI": "54930000014132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    14133: SanctionedItem(
        sdn_id=14133,
        name="Ali Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14133"},
        aliases=["Qiang, Ali", "A. Qiang"]
    ),
    14134: SanctionedItem(
        sdn_id=14134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14134", "LEI": "54930000014134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    14135: SanctionedItem(
        sdn_id=14135,
        name="Ahmad Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14135"},
        aliases=["Cabello, Ahmad", "A. Cabello"]
    ),
    14136: SanctionedItem(
        sdn_id=14136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14136", "LEI": "54930000014136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    14137: SanctionedItem(
        sdn_id=14137,
        name="Kim Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14137"},
        aliases=["Lopez, Kim", "K. Lopez"]
    ),
    14138: SanctionedItem(
        sdn_id=14138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14138", "LEI": "54930000014138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    14139: SanctionedItem(
        sdn_id=14139,
        name="Park Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14139"},
        aliases=["Ivanov, Park", "P. Ivanov"]
    ),
    14140: SanctionedItem(
        sdn_id=14140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14140", "LEI": "54930000014140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    14141: SanctionedItem(
        sdn_id=14141,
        name="Chen Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14141"},
        aliases=["Smirnov, Chen", "C. Smirnov"]
    ),
    14142: SanctionedItem(
        sdn_id=14142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14142", "LEI": "54930000014142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    14143: SanctionedItem(
        sdn_id=14143,
        name="Wang Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14143"},
        aliases=["Sokolov, Wang", "W. Sokolov"]
    ),
    14144: SanctionedItem(
        sdn_id=14144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14144", "LEI": "54930000014144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    14145: SanctionedItem(
        sdn_id=14145,
        name="Zhang Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14145"},
        aliases=["Soleimani, Zhang", "Z. Soleimani"]
    ),
    14146: SanctionedItem(
        sdn_id=14146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14146", "LEI": "54930000014146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    14147: SanctionedItem(
        sdn_id=14147,
        name="Carlos Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14147"},
        aliases=["Najafi, Carlos", "C. Najafi"]
    ),
    14148: SanctionedItem(
        sdn_id=14148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14148", "LEI": "54930000014148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    14149: SanctionedItem(
        sdn_id=14149,
        name="Raul Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14149"},
        aliases=["Il-sung, Raul", "R. Il-sung"]
    ),
    14150: SanctionedItem(
        sdn_id=14150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14150", "LEI": "54930000014150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    14151: SanctionedItem(
        sdn_id=14151,
        name="Ernesto Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14151"},
        aliases=["Wei, Ernesto", "E. Wei"]
    ),
    14152: SanctionedItem(
        sdn_id=14152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14152", "LEI": "54930000014152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    14153: SanctionedItem(
        sdn_id=14153,
        name="Ibrahim Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14153"},
        aliases=["Qiang, Ibrahim", "I. Qiang"]
    ),
    14154: SanctionedItem(
        sdn_id=14154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14154", "LEI": "54930000014154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    14155: SanctionedItem(
        sdn_id=14155,
        name="Tariq Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14155"},
        aliases=["Cabello, Tariq", "T. Cabello"]
    ),
    14156: SanctionedItem(
        sdn_id=14156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14156", "LEI": "54930000014156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    14157: SanctionedItem(
        sdn_id=14157,
        name="Nikolai Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14157"},
        aliases=["Lopez, Nikolai", "N. Lopez"]
    ),
    14158: SanctionedItem(
        sdn_id=14158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14158", "LEI": "54930000014158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    14159: SanctionedItem(
        sdn_id=14159,
        name="Vladimir Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14159"},
        aliases=["Ivanov, Vladimir", "V. Ivanov"]
    ),
    14160: SanctionedItem(
        sdn_id=14160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14160", "LEI": "54930000014160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    14161: SanctionedItem(
        sdn_id=14161,
        name="Andrei Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14161"},
        aliases=["Smirnov, Andrei", "A. Smirnov"]
    ),
    14162: SanctionedItem(
        sdn_id=14162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14162", "LEI": "54930000014162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    14163: SanctionedItem(
        sdn_id=14163,
        name="Mikhail Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14163"},
        aliases=["Sokolov, Mikhail", "M. Sokolov"]
    ),
    14164: SanctionedItem(
        sdn_id=14164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14164", "LEI": "54930000014164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    14165: SanctionedItem(
        sdn_id=14165,
        name="Reza Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14165"},
        aliases=["Soleimani, Reza", "R. Soleimani"]
    ),
    14166: SanctionedItem(
        sdn_id=14166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14166", "LEI": "54930000014166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    14167: SanctionedItem(
        sdn_id=14167,
        name="Farhad Najafi",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14167"},
        aliases=["Najafi, Farhad", "F. Najafi"]
    ),
    14168: SanctionedItem(
        sdn_id=14168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14168", "LEI": "54930000014168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    14169: SanctionedItem(
        sdn_id=14169,
        name="Mahmoud Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14169"},
        aliases=["Il-sung, Mahmoud", "M. Il-sung"]
    ),
    14170: SanctionedItem(
        sdn_id=14170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14170", "LEI": "54930000014170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    14171: SanctionedItem(
        sdn_id=14171,
        name="Slobodan Wei",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14171"},
        aliases=["Wei, Slobodan", "S. Wei"]
    ),
    14172: SanctionedItem(
        sdn_id=14172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14172", "LEI": "54930000014172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    14173: SanctionedItem(
        sdn_id=14173,
        name="Radovan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14173"},
        aliases=["Qiang, Radovan", "R. Qiang"]
    ),
    14174: SanctionedItem(
        sdn_id=14174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14174", "LEI": "54930000014174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    14175: SanctionedItem(
        sdn_id=14175,
        name="Goran Cabello",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14175"},
        aliases=["Cabello, Goran", "G. Cabello"]
    ),
    14176: SanctionedItem(
        sdn_id=14176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14176", "LEI": "54930000014176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    14177: SanctionedItem(
        sdn_id=14177,
        name="Milorad Lopez",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14177"},
        aliases=["Lopez, Milorad", "M. Lopez"]
    ),
    14178: SanctionedItem(
        sdn_id=14178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated entity under VENEZUELA-EO13884 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-14178", "LEI": "54930000014178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    14179: SanctionedItem(
        sdn_id=14179,
        name="Jean-Pierre Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["VENEZUELA-EO13884"],
        remarks="Designated individual under VENEZUELA-EO13884; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-14179"},
        aliases=["Ivanov, Jean-Pierre", "J. Ivanov"]
    ),
}

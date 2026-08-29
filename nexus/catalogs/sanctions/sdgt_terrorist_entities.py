"""
Global Counter-Terrorism Sanctions.
SDGT Counter-Terrorism Program.
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

RECORDS_SDGT_TERRORIST_ENTITIES: Dict[int, SanctionedItem] = {
    10000: SanctionedItem(
        sdn_id=10000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10000", "LEI": "54930000010000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    10001: SanctionedItem(
        sdn_id=10001,
        name="Viktor Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10001"},
        aliases=["Petrov, Viktor", "V. Petrov"]
    ),
    10002: SanctionedItem(
        sdn_id=10002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10002", "LEI": "54930000010002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    10003: SanctionedItem(
        sdn_id=10003,
        name="Dmitry Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10003"},
        aliases=["Volkov, Dmitry", "D. Volkov"]
    ),
    10004: SanctionedItem(
        sdn_id=10004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10004", "LEI": "54930000010004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    10005: SanctionedItem(
        sdn_id=10005,
        name="Sergei Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10005"},
        aliases=["Popov, Sergei", "S. Popov"]
    ),
    10006: SanctionedItem(
        sdn_id=10006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10006", "LEI": "54930000010006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    10007: SanctionedItem(
        sdn_id=10007,
        name="Alexander Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10007"},
        aliases=["Hosseini, Alexander", "A. Hosseini"]
    ),
    10008: SanctionedItem(
        sdn_id=10008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10008", "LEI": "54930000010008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    10009: SanctionedItem(
        sdn_id=10009,
        name="Mohammad Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10009"},
        aliases=["Jafari, Mohammad", "M. Jafari"]
    ),
    10010: SanctionedItem(
        sdn_id=10010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10010", "LEI": "54930000010010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    10011: SanctionedItem(
        sdn_id=10011,
        name="Hassan Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10011"},
        aliases=["Jong-un, Hassan", "H. Jong-un"]
    ),
    10012: SanctionedItem(
        sdn_id=10012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10012", "LEI": "54930000010012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    10013: SanctionedItem(
        sdn_id=10013,
        name="Ali Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10013"},
        aliases=["Kwang-hyok, Ali", "A. Kwang-hyok"]
    ),
    10014: SanctionedItem(
        sdn_id=10014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10014", "LEI": "54930000010014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    10015: SanctionedItem(
        sdn_id=10015,
        name="Ahmad Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10015"},
        aliases=["Gang, Ahmad", "A. Gang"]
    ),
    10016: SanctionedItem(
        sdn_id=10016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10016", "LEI": "54930000010016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    10017: SanctionedItem(
        sdn_id=10017,
        name="Kim Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10017"},
        aliases=["Morales, Kim", "K. Morales"]
    ),
    10018: SanctionedItem(
        sdn_id=10018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10018", "LEI": "54930000010018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    10019: SanctionedItem(
        sdn_id=10019,
        name="Park Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10019"},
        aliases=["Flores, Park", "P. Flores"]
    ),
    10020: SanctionedItem(
        sdn_id=10020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10020", "LEI": "54930000010020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    10021: SanctionedItem(
        sdn_id=10021,
        name="Chen Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10021"},
        aliases=["Petrov, Chen", "C. Petrov"]
    ),
    10022: SanctionedItem(
        sdn_id=10022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10022", "LEI": "54930000010022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    10023: SanctionedItem(
        sdn_id=10023,
        name="Wang Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10023"},
        aliases=["Volkov, Wang", "W. Volkov"]
    ),
    10024: SanctionedItem(
        sdn_id=10024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10024", "LEI": "54930000010024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    10025: SanctionedItem(
        sdn_id=10025,
        name="Zhang Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10025"},
        aliases=["Popov, Zhang", "Z. Popov"]
    ),
    10026: SanctionedItem(
        sdn_id=10026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10026", "LEI": "54930000010026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    10027: SanctionedItem(
        sdn_id=10027,
        name="Carlos Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10027"},
        aliases=["Hosseini, Carlos", "C. Hosseini"]
    ),
    10028: SanctionedItem(
        sdn_id=10028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10028", "LEI": "54930000010028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    10029: SanctionedItem(
        sdn_id=10029,
        name="Raul Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10029"},
        aliases=["Jafari, Raul", "R. Jafari"]
    ),
    10030: SanctionedItem(
        sdn_id=10030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10030", "LEI": "54930000010030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    10031: SanctionedItem(
        sdn_id=10031,
        name="Ernesto Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10031"},
        aliases=["Jong-un, Ernesto", "E. Jong-un"]
    ),
    10032: SanctionedItem(
        sdn_id=10032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10032", "LEI": "54930000010032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    10033: SanctionedItem(
        sdn_id=10033,
        name="Ibrahim Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10033"},
        aliases=["Kwang-hyok, Ibrahim", "I. Kwang-hyok"]
    ),
    10034: SanctionedItem(
        sdn_id=10034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10034", "LEI": "54930000010034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    10035: SanctionedItem(
        sdn_id=10035,
        name="Tariq Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10035"},
        aliases=["Gang, Tariq", "T. Gang"]
    ),
    10036: SanctionedItem(
        sdn_id=10036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10036", "LEI": "54930000010036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    10037: SanctionedItem(
        sdn_id=10037,
        name="Nikolai Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10037"},
        aliases=["Morales, Nikolai", "N. Morales"]
    ),
    10038: SanctionedItem(
        sdn_id=10038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10038", "LEI": "54930000010038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    10039: SanctionedItem(
        sdn_id=10039,
        name="Vladimir Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10039"},
        aliases=["Flores, Vladimir", "V. Flores"]
    ),
    10040: SanctionedItem(
        sdn_id=10040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10040", "LEI": "54930000010040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    10041: SanctionedItem(
        sdn_id=10041,
        name="Andrei Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10041"},
        aliases=["Petrov, Andrei", "A. Petrov"]
    ),
    10042: SanctionedItem(
        sdn_id=10042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10042", "LEI": "54930000010042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    10043: SanctionedItem(
        sdn_id=10043,
        name="Mikhail Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10043"},
        aliases=["Volkov, Mikhail", "M. Volkov"]
    ),
    10044: SanctionedItem(
        sdn_id=10044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10044", "LEI": "54930000010044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    10045: SanctionedItem(
        sdn_id=10045,
        name="Reza Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10045"},
        aliases=["Popov, Reza", "R. Popov"]
    ),
    10046: SanctionedItem(
        sdn_id=10046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10046", "LEI": "54930000010046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    10047: SanctionedItem(
        sdn_id=10047,
        name="Farhad Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10047"},
        aliases=["Hosseini, Farhad", "F. Hosseini"]
    ),
    10048: SanctionedItem(
        sdn_id=10048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10048", "LEI": "54930000010048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    10049: SanctionedItem(
        sdn_id=10049,
        name="Mahmoud Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10049"},
        aliases=["Jafari, Mahmoud", "M. Jafari"]
    ),
    10050: SanctionedItem(
        sdn_id=10050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10050", "LEI": "54930000010050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    10051: SanctionedItem(
        sdn_id=10051,
        name="Slobodan Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10051"},
        aliases=["Jong-un, Slobodan", "S. Jong-un"]
    ),
    10052: SanctionedItem(
        sdn_id=10052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10052", "LEI": "54930000010052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    10053: SanctionedItem(
        sdn_id=10053,
        name="Radovan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10053"},
        aliases=["Kwang-hyok, Radovan", "R. Kwang-hyok"]
    ),
    10054: SanctionedItem(
        sdn_id=10054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10054", "LEI": "54930000010054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    10055: SanctionedItem(
        sdn_id=10055,
        name="Goran Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10055"},
        aliases=["Gang, Goran", "G. Gang"]
    ),
    10056: SanctionedItem(
        sdn_id=10056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10056", "LEI": "54930000010056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    10057: SanctionedItem(
        sdn_id=10057,
        name="Milorad Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10057"},
        aliases=["Morales, Milorad", "M. Morales"]
    ),
    10058: SanctionedItem(
        sdn_id=10058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10058", "LEI": "54930000010058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    10059: SanctionedItem(
        sdn_id=10059,
        name="Jean-Pierre Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10059"},
        aliases=["Flores, Jean-Pierre", "J. Flores"]
    ),
    10060: SanctionedItem(
        sdn_id=10060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10060", "LEI": "54930000010060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    10061: SanctionedItem(
        sdn_id=10061,
        name="Viktor Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10061"},
        aliases=["Petrov, Viktor", "V. Petrov"]
    ),
    10062: SanctionedItem(
        sdn_id=10062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10062", "LEI": "54930000010062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    10063: SanctionedItem(
        sdn_id=10063,
        name="Dmitry Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10063"},
        aliases=["Volkov, Dmitry", "D. Volkov"]
    ),
    10064: SanctionedItem(
        sdn_id=10064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10064", "LEI": "54930000010064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    10065: SanctionedItem(
        sdn_id=10065,
        name="Sergei Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10065"},
        aliases=["Popov, Sergei", "S. Popov"]
    ),
    10066: SanctionedItem(
        sdn_id=10066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10066", "LEI": "54930000010066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    10067: SanctionedItem(
        sdn_id=10067,
        name="Alexander Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10067"},
        aliases=["Hosseini, Alexander", "A. Hosseini"]
    ),
    10068: SanctionedItem(
        sdn_id=10068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10068", "LEI": "54930000010068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    10069: SanctionedItem(
        sdn_id=10069,
        name="Mohammad Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10069"},
        aliases=["Jafari, Mohammad", "M. Jafari"]
    ),
    10070: SanctionedItem(
        sdn_id=10070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10070", "LEI": "54930000010070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    10071: SanctionedItem(
        sdn_id=10071,
        name="Hassan Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10071"},
        aliases=["Jong-un, Hassan", "H. Jong-un"]
    ),
    10072: SanctionedItem(
        sdn_id=10072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10072", "LEI": "54930000010072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    10073: SanctionedItem(
        sdn_id=10073,
        name="Ali Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10073"},
        aliases=["Kwang-hyok, Ali", "A. Kwang-hyok"]
    ),
    10074: SanctionedItem(
        sdn_id=10074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10074", "LEI": "54930000010074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    10075: SanctionedItem(
        sdn_id=10075,
        name="Ahmad Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10075"},
        aliases=["Gang, Ahmad", "A. Gang"]
    ),
    10076: SanctionedItem(
        sdn_id=10076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10076", "LEI": "54930000010076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    10077: SanctionedItem(
        sdn_id=10077,
        name="Kim Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10077"},
        aliases=["Morales, Kim", "K. Morales"]
    ),
    10078: SanctionedItem(
        sdn_id=10078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10078", "LEI": "54930000010078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    10079: SanctionedItem(
        sdn_id=10079,
        name="Park Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10079"},
        aliases=["Flores, Park", "P. Flores"]
    ),
    10080: SanctionedItem(
        sdn_id=10080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10080", "LEI": "54930000010080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    10081: SanctionedItem(
        sdn_id=10081,
        name="Chen Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10081"},
        aliases=["Petrov, Chen", "C. Petrov"]
    ),
    10082: SanctionedItem(
        sdn_id=10082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10082", "LEI": "54930000010082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    10083: SanctionedItem(
        sdn_id=10083,
        name="Wang Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10083"},
        aliases=["Volkov, Wang", "W. Volkov"]
    ),
    10084: SanctionedItem(
        sdn_id=10084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10084", "LEI": "54930000010084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    10085: SanctionedItem(
        sdn_id=10085,
        name="Zhang Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10085"},
        aliases=["Popov, Zhang", "Z. Popov"]
    ),
    10086: SanctionedItem(
        sdn_id=10086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10086", "LEI": "54930000010086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    10087: SanctionedItem(
        sdn_id=10087,
        name="Carlos Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10087"},
        aliases=["Hosseini, Carlos", "C. Hosseini"]
    ),
    10088: SanctionedItem(
        sdn_id=10088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10088", "LEI": "54930000010088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    10089: SanctionedItem(
        sdn_id=10089,
        name="Raul Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10089"},
        aliases=["Jafari, Raul", "R. Jafari"]
    ),
    10090: SanctionedItem(
        sdn_id=10090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10090", "LEI": "54930000010090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    10091: SanctionedItem(
        sdn_id=10091,
        name="Ernesto Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10091"},
        aliases=["Jong-un, Ernesto", "E. Jong-un"]
    ),
    10092: SanctionedItem(
        sdn_id=10092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10092", "LEI": "54930000010092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    10093: SanctionedItem(
        sdn_id=10093,
        name="Ibrahim Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10093"},
        aliases=["Kwang-hyok, Ibrahim", "I. Kwang-hyok"]
    ),
    10094: SanctionedItem(
        sdn_id=10094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10094", "LEI": "54930000010094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    10095: SanctionedItem(
        sdn_id=10095,
        name="Tariq Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10095"},
        aliases=["Gang, Tariq", "T. Gang"]
    ),
    10096: SanctionedItem(
        sdn_id=10096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10096", "LEI": "54930000010096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    10097: SanctionedItem(
        sdn_id=10097,
        name="Nikolai Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10097"},
        aliases=["Morales, Nikolai", "N. Morales"]
    ),
    10098: SanctionedItem(
        sdn_id=10098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10098", "LEI": "54930000010098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    10099: SanctionedItem(
        sdn_id=10099,
        name="Vladimir Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10099"},
        aliases=["Flores, Vladimir", "V. Flores"]
    ),
    10100: SanctionedItem(
        sdn_id=10100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10100", "LEI": "54930000010100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    10101: SanctionedItem(
        sdn_id=10101,
        name="Andrei Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10101"},
        aliases=["Petrov, Andrei", "A. Petrov"]
    ),
    10102: SanctionedItem(
        sdn_id=10102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10102", "LEI": "54930000010102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    10103: SanctionedItem(
        sdn_id=10103,
        name="Mikhail Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10103"},
        aliases=["Volkov, Mikhail", "M. Volkov"]
    ),
    10104: SanctionedItem(
        sdn_id=10104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10104", "LEI": "54930000010104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    10105: SanctionedItem(
        sdn_id=10105,
        name="Reza Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10105"},
        aliases=["Popov, Reza", "R. Popov"]
    ),
    10106: SanctionedItem(
        sdn_id=10106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10106", "LEI": "54930000010106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    10107: SanctionedItem(
        sdn_id=10107,
        name="Farhad Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10107"},
        aliases=["Hosseini, Farhad", "F. Hosseini"]
    ),
    10108: SanctionedItem(
        sdn_id=10108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10108", "LEI": "54930000010108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    10109: SanctionedItem(
        sdn_id=10109,
        name="Mahmoud Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10109"},
        aliases=["Jafari, Mahmoud", "M. Jafari"]
    ),
    10110: SanctionedItem(
        sdn_id=10110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10110", "LEI": "54930000010110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    10111: SanctionedItem(
        sdn_id=10111,
        name="Slobodan Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10111"},
        aliases=["Jong-un, Slobodan", "S. Jong-un"]
    ),
    10112: SanctionedItem(
        sdn_id=10112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10112", "LEI": "54930000010112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    10113: SanctionedItem(
        sdn_id=10113,
        name="Radovan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10113"},
        aliases=["Kwang-hyok, Radovan", "R. Kwang-hyok"]
    ),
    10114: SanctionedItem(
        sdn_id=10114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10114", "LEI": "54930000010114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    10115: SanctionedItem(
        sdn_id=10115,
        name="Goran Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10115"},
        aliases=["Gang, Goran", "G. Gang"]
    ),
    10116: SanctionedItem(
        sdn_id=10116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10116", "LEI": "54930000010116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    10117: SanctionedItem(
        sdn_id=10117,
        name="Milorad Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10117"},
        aliases=["Morales, Milorad", "M. Morales"]
    ),
    10118: SanctionedItem(
        sdn_id=10118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10118", "LEI": "54930000010118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    10119: SanctionedItem(
        sdn_id=10119,
        name="Jean-Pierre Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10119"},
        aliases=["Flores, Jean-Pierre", "J. Flores"]
    ),
    10120: SanctionedItem(
        sdn_id=10120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10120", "LEI": "54930000010120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    10121: SanctionedItem(
        sdn_id=10121,
        name="Viktor Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10121"},
        aliases=["Petrov, Viktor", "V. Petrov"]
    ),
    10122: SanctionedItem(
        sdn_id=10122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10122", "LEI": "54930000010122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    10123: SanctionedItem(
        sdn_id=10123,
        name="Dmitry Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10123"},
        aliases=["Volkov, Dmitry", "D. Volkov"]
    ),
    10124: SanctionedItem(
        sdn_id=10124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10124", "LEI": "54930000010124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    10125: SanctionedItem(
        sdn_id=10125,
        name="Sergei Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10125"},
        aliases=["Popov, Sergei", "S. Popov"]
    ),
    10126: SanctionedItem(
        sdn_id=10126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10126", "LEI": "54930000010126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    10127: SanctionedItem(
        sdn_id=10127,
        name="Alexander Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10127"},
        aliases=["Hosseini, Alexander", "A. Hosseini"]
    ),
    10128: SanctionedItem(
        sdn_id=10128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10128", "LEI": "54930000010128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    10129: SanctionedItem(
        sdn_id=10129,
        name="Mohammad Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10129"},
        aliases=["Jafari, Mohammad", "M. Jafari"]
    ),
    10130: SanctionedItem(
        sdn_id=10130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10130", "LEI": "54930000010130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    10131: SanctionedItem(
        sdn_id=10131,
        name="Hassan Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10131"},
        aliases=["Jong-un, Hassan", "H. Jong-un"]
    ),
    10132: SanctionedItem(
        sdn_id=10132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10132", "LEI": "54930000010132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    10133: SanctionedItem(
        sdn_id=10133,
        name="Ali Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10133"},
        aliases=["Kwang-hyok, Ali", "A. Kwang-hyok"]
    ),
    10134: SanctionedItem(
        sdn_id=10134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10134", "LEI": "54930000010134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    10135: SanctionedItem(
        sdn_id=10135,
        name="Ahmad Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10135"},
        aliases=["Gang, Ahmad", "A. Gang"]
    ),
    10136: SanctionedItem(
        sdn_id=10136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10136", "LEI": "54930000010136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    10137: SanctionedItem(
        sdn_id=10137,
        name="Kim Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10137"},
        aliases=["Morales, Kim", "K. Morales"]
    ),
    10138: SanctionedItem(
        sdn_id=10138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10138", "LEI": "54930000010138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    10139: SanctionedItem(
        sdn_id=10139,
        name="Park Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10139"},
        aliases=["Flores, Park", "P. Flores"]
    ),
    10140: SanctionedItem(
        sdn_id=10140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10140", "LEI": "54930000010140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    10141: SanctionedItem(
        sdn_id=10141,
        name="Chen Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10141"},
        aliases=["Petrov, Chen", "C. Petrov"]
    ),
    10142: SanctionedItem(
        sdn_id=10142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10142", "LEI": "54930000010142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    10143: SanctionedItem(
        sdn_id=10143,
        name="Wang Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10143"},
        aliases=["Volkov, Wang", "W. Volkov"]
    ),
    10144: SanctionedItem(
        sdn_id=10144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10144", "LEI": "54930000010144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    10145: SanctionedItem(
        sdn_id=10145,
        name="Zhang Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10145"},
        aliases=["Popov, Zhang", "Z. Popov"]
    ),
    10146: SanctionedItem(
        sdn_id=10146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10146", "LEI": "54930000010146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    10147: SanctionedItem(
        sdn_id=10147,
        name="Carlos Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10147"},
        aliases=["Hosseini, Carlos", "C. Hosseini"]
    ),
    10148: SanctionedItem(
        sdn_id=10148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10148", "LEI": "54930000010148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    10149: SanctionedItem(
        sdn_id=10149,
        name="Raul Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10149"},
        aliases=["Jafari, Raul", "R. Jafari"]
    ),
    10150: SanctionedItem(
        sdn_id=10150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10150", "LEI": "54930000010150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    10151: SanctionedItem(
        sdn_id=10151,
        name="Ernesto Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10151"},
        aliases=["Jong-un, Ernesto", "E. Jong-un"]
    ),
    10152: SanctionedItem(
        sdn_id=10152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10152", "LEI": "54930000010152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    10153: SanctionedItem(
        sdn_id=10153,
        name="Ibrahim Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10153"},
        aliases=["Kwang-hyok, Ibrahim", "I. Kwang-hyok"]
    ),
    10154: SanctionedItem(
        sdn_id=10154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10154", "LEI": "54930000010154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    10155: SanctionedItem(
        sdn_id=10155,
        name="Tariq Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10155"},
        aliases=["Gang, Tariq", "T. Gang"]
    ),
    10156: SanctionedItem(
        sdn_id=10156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10156", "LEI": "54930000010156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    10157: SanctionedItem(
        sdn_id=10157,
        name="Nikolai Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10157"},
        aliases=["Morales, Nikolai", "N. Morales"]
    ),
    10158: SanctionedItem(
        sdn_id=10158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10158", "LEI": "54930000010158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    10159: SanctionedItem(
        sdn_id=10159,
        name="Vladimir Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10159"},
        aliases=["Flores, Vladimir", "V. Flores"]
    ),
    10160: SanctionedItem(
        sdn_id=10160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10160", "LEI": "54930000010160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    10161: SanctionedItem(
        sdn_id=10161,
        name="Andrei Petrov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10161"},
        aliases=["Petrov, Andrei", "A. Petrov"]
    ),
    10162: SanctionedItem(
        sdn_id=10162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10162", "LEI": "54930000010162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    10163: SanctionedItem(
        sdn_id=10163,
        name="Mikhail Volkov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10163"},
        aliases=["Volkov, Mikhail", "M. Volkov"]
    ),
    10164: SanctionedItem(
        sdn_id=10164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10164", "LEI": "54930000010164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    10165: SanctionedItem(
        sdn_id=10165,
        name="Reza Popov",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10165"},
        aliases=["Popov, Reza", "R. Popov"]
    ),
    10166: SanctionedItem(
        sdn_id=10166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10166", "LEI": "54930000010166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    10167: SanctionedItem(
        sdn_id=10167,
        name="Farhad Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10167"},
        aliases=["Hosseini, Farhad", "F. Hosseini"]
    ),
    10168: SanctionedItem(
        sdn_id=10168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10168", "LEI": "54930000010168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    10169: SanctionedItem(
        sdn_id=10169,
        name="Mahmoud Jafari",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10169"},
        aliases=["Jafari, Mahmoud", "M. Jafari"]
    ),
    10170: SanctionedItem(
        sdn_id=10170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10170", "LEI": "54930000010170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    10171: SanctionedItem(
        sdn_id=10171,
        name="Slobodan Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10171"},
        aliases=["Jong-un, Slobodan", "S. Jong-un"]
    ),
    10172: SanctionedItem(
        sdn_id=10172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10172", "LEI": "54930000010172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    10173: SanctionedItem(
        sdn_id=10173,
        name="Radovan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10173"},
        aliases=["Kwang-hyok, Radovan", "R. Kwang-hyok"]
    ),
    10174: SanctionedItem(
        sdn_id=10174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10174", "LEI": "54930000010174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    10175: SanctionedItem(
        sdn_id=10175,
        name="Goran Gang",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10175"},
        aliases=["Gang, Goran", "G. Gang"]
    ),
    10176: SanctionedItem(
        sdn_id=10176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10176", "LEI": "54930000010176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    10177: SanctionedItem(
        sdn_id=10177,
        name="Milorad Morales",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10177"},
        aliases=["Morales, Milorad", "M. Morales"]
    ),
    10178: SanctionedItem(
        sdn_id=10178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["SDGT"],
        remarks="Designated entity under SDGT enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-10178", "LEI": "54930000010178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    10179: SanctionedItem(
        sdn_id=10179,
        name="Jean-Pierre Flores",
        sdn_type="INDIVIDUAL",
        programs=["SDGT"],
        remarks="Designated individual under SDGT; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-10179"},
        aliases=["Flores, Jean-Pierre", "J. Flores"]
    ),
}

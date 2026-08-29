"""
Malicious Cyber Activities & Crime Sanctions.
Cybersecurity EO 13757.
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

RECORDS_CYBER_TRANSNATIONAL_SANCTIONS: Dict[int, SanctionedItem] = {
    16000: SanctionedItem(
        sdn_id=16000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16000", "LEI": "54930000016000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    16001: SanctionedItem(
        sdn_id=16001,
        name="Viktor Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16001"},
        aliases=["Popov, Viktor", "V. Popov"]
    ),
    16002: SanctionedItem(
        sdn_id=16002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16002", "LEI": "54930000016002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    16003: SanctionedItem(
        sdn_id=16003,
        name="Dmitry Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16003"},
        aliases=["Hosseini, Dmitry", "D. Hosseini"]
    ),
    16004: SanctionedItem(
        sdn_id=16004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16004", "LEI": "54930000016004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    16005: SanctionedItem(
        sdn_id=16005,
        name="Sergei Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16005"},
        aliases=["Jafari, Sergei", "S. Jafari"]
    ),
    16006: SanctionedItem(
        sdn_id=16006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16006", "LEI": "54930000016006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    16007: SanctionedItem(
        sdn_id=16007,
        name="Alexander Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16007"},
        aliases=["Jong-un, Alexander", "A. Jong-un"]
    ),
    16008: SanctionedItem(
        sdn_id=16008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16008", "LEI": "54930000016008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    16009: SanctionedItem(
        sdn_id=16009,
        name="Mohammad Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16009"},
        aliases=["Kwang-hyok, Mohammad", "M. Kwang-hyok"]
    ),
    16010: SanctionedItem(
        sdn_id=16010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16010", "LEI": "54930000016010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    16011: SanctionedItem(
        sdn_id=16011,
        name="Hassan Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16011"},
        aliases=["Gang, Hassan", "H. Gang"]
    ),
    16012: SanctionedItem(
        sdn_id=16012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16012", "LEI": "54930000016012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    16013: SanctionedItem(
        sdn_id=16013,
        name="Ali Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16013"},
        aliases=["Morales, Ali", "A. Morales"]
    ),
    16014: SanctionedItem(
        sdn_id=16014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16014", "LEI": "54930000016014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    16015: SanctionedItem(
        sdn_id=16015,
        name="Ahmad Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16015"},
        aliases=["Flores, Ahmad", "A. Flores"]
    ),
    16016: SanctionedItem(
        sdn_id=16016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16016", "LEI": "54930000016016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    16017: SanctionedItem(
        sdn_id=16017,
        name="Kim Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16017"},
        aliases=["Petrov, Kim", "K. Petrov"]
    ),
    16018: SanctionedItem(
        sdn_id=16018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16018", "LEI": "54930000016018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    16019: SanctionedItem(
        sdn_id=16019,
        name="Park Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16019"},
        aliases=["Volkov, Park", "P. Volkov"]
    ),
    16020: SanctionedItem(
        sdn_id=16020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16020", "LEI": "54930000016020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    16021: SanctionedItem(
        sdn_id=16021,
        name="Chen Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16021"},
        aliases=["Popov, Chen", "C. Popov"]
    ),
    16022: SanctionedItem(
        sdn_id=16022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16022", "LEI": "54930000016022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    16023: SanctionedItem(
        sdn_id=16023,
        name="Wang Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16023"},
        aliases=["Hosseini, Wang", "W. Hosseini"]
    ),
    16024: SanctionedItem(
        sdn_id=16024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16024", "LEI": "54930000016024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    16025: SanctionedItem(
        sdn_id=16025,
        name="Zhang Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16025"},
        aliases=["Jafari, Zhang", "Z. Jafari"]
    ),
    16026: SanctionedItem(
        sdn_id=16026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16026", "LEI": "54930000016026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    16027: SanctionedItem(
        sdn_id=16027,
        name="Carlos Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16027"},
        aliases=["Jong-un, Carlos", "C. Jong-un"]
    ),
    16028: SanctionedItem(
        sdn_id=16028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16028", "LEI": "54930000016028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    16029: SanctionedItem(
        sdn_id=16029,
        name="Raul Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16029"},
        aliases=["Kwang-hyok, Raul", "R. Kwang-hyok"]
    ),
    16030: SanctionedItem(
        sdn_id=16030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16030", "LEI": "54930000016030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    16031: SanctionedItem(
        sdn_id=16031,
        name="Ernesto Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16031"},
        aliases=["Gang, Ernesto", "E. Gang"]
    ),
    16032: SanctionedItem(
        sdn_id=16032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16032", "LEI": "54930000016032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    16033: SanctionedItem(
        sdn_id=16033,
        name="Ibrahim Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16033"},
        aliases=["Morales, Ibrahim", "I. Morales"]
    ),
    16034: SanctionedItem(
        sdn_id=16034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16034", "LEI": "54930000016034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    16035: SanctionedItem(
        sdn_id=16035,
        name="Tariq Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16035"},
        aliases=["Flores, Tariq", "T. Flores"]
    ),
    16036: SanctionedItem(
        sdn_id=16036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16036", "LEI": "54930000016036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    16037: SanctionedItem(
        sdn_id=16037,
        name="Nikolai Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16037"},
        aliases=["Petrov, Nikolai", "N. Petrov"]
    ),
    16038: SanctionedItem(
        sdn_id=16038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16038", "LEI": "54930000016038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    16039: SanctionedItem(
        sdn_id=16039,
        name="Vladimir Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16039"},
        aliases=["Volkov, Vladimir", "V. Volkov"]
    ),
    16040: SanctionedItem(
        sdn_id=16040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16040", "LEI": "54930000016040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    16041: SanctionedItem(
        sdn_id=16041,
        name="Andrei Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16041"},
        aliases=["Popov, Andrei", "A. Popov"]
    ),
    16042: SanctionedItem(
        sdn_id=16042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16042", "LEI": "54930000016042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    16043: SanctionedItem(
        sdn_id=16043,
        name="Mikhail Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16043"},
        aliases=["Hosseini, Mikhail", "M. Hosseini"]
    ),
    16044: SanctionedItem(
        sdn_id=16044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16044", "LEI": "54930000016044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    16045: SanctionedItem(
        sdn_id=16045,
        name="Reza Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16045"},
        aliases=["Jafari, Reza", "R. Jafari"]
    ),
    16046: SanctionedItem(
        sdn_id=16046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16046", "LEI": "54930000016046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    16047: SanctionedItem(
        sdn_id=16047,
        name="Farhad Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16047"},
        aliases=["Jong-un, Farhad", "F. Jong-un"]
    ),
    16048: SanctionedItem(
        sdn_id=16048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16048", "LEI": "54930000016048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    16049: SanctionedItem(
        sdn_id=16049,
        name="Mahmoud Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16049"},
        aliases=["Kwang-hyok, Mahmoud", "M. Kwang-hyok"]
    ),
    16050: SanctionedItem(
        sdn_id=16050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16050", "LEI": "54930000016050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    16051: SanctionedItem(
        sdn_id=16051,
        name="Slobodan Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16051"},
        aliases=["Gang, Slobodan", "S. Gang"]
    ),
    16052: SanctionedItem(
        sdn_id=16052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16052", "LEI": "54930000016052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    16053: SanctionedItem(
        sdn_id=16053,
        name="Radovan Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16053"},
        aliases=["Morales, Radovan", "R. Morales"]
    ),
    16054: SanctionedItem(
        sdn_id=16054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16054", "LEI": "54930000016054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    16055: SanctionedItem(
        sdn_id=16055,
        name="Goran Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16055"},
        aliases=["Flores, Goran", "G. Flores"]
    ),
    16056: SanctionedItem(
        sdn_id=16056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16056", "LEI": "54930000016056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    16057: SanctionedItem(
        sdn_id=16057,
        name="Milorad Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16057"},
        aliases=["Petrov, Milorad", "M. Petrov"]
    ),
    16058: SanctionedItem(
        sdn_id=16058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16058", "LEI": "54930000016058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    16059: SanctionedItem(
        sdn_id=16059,
        name="Jean-Pierre Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16059"},
        aliases=["Volkov, Jean-Pierre", "J. Volkov"]
    ),
    16060: SanctionedItem(
        sdn_id=16060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16060", "LEI": "54930000016060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    16061: SanctionedItem(
        sdn_id=16061,
        name="Viktor Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16061"},
        aliases=["Popov, Viktor", "V. Popov"]
    ),
    16062: SanctionedItem(
        sdn_id=16062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16062", "LEI": "54930000016062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    16063: SanctionedItem(
        sdn_id=16063,
        name="Dmitry Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16063"},
        aliases=["Hosseini, Dmitry", "D. Hosseini"]
    ),
    16064: SanctionedItem(
        sdn_id=16064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16064", "LEI": "54930000016064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    16065: SanctionedItem(
        sdn_id=16065,
        name="Sergei Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16065"},
        aliases=["Jafari, Sergei", "S. Jafari"]
    ),
    16066: SanctionedItem(
        sdn_id=16066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16066", "LEI": "54930000016066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    16067: SanctionedItem(
        sdn_id=16067,
        name="Alexander Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16067"},
        aliases=["Jong-un, Alexander", "A. Jong-un"]
    ),
    16068: SanctionedItem(
        sdn_id=16068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16068", "LEI": "54930000016068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    16069: SanctionedItem(
        sdn_id=16069,
        name="Mohammad Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16069"},
        aliases=["Kwang-hyok, Mohammad", "M. Kwang-hyok"]
    ),
    16070: SanctionedItem(
        sdn_id=16070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16070", "LEI": "54930000016070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    16071: SanctionedItem(
        sdn_id=16071,
        name="Hassan Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16071"},
        aliases=["Gang, Hassan", "H. Gang"]
    ),
    16072: SanctionedItem(
        sdn_id=16072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16072", "LEI": "54930000016072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    16073: SanctionedItem(
        sdn_id=16073,
        name="Ali Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16073"},
        aliases=["Morales, Ali", "A. Morales"]
    ),
    16074: SanctionedItem(
        sdn_id=16074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16074", "LEI": "54930000016074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    16075: SanctionedItem(
        sdn_id=16075,
        name="Ahmad Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16075"},
        aliases=["Flores, Ahmad", "A. Flores"]
    ),
    16076: SanctionedItem(
        sdn_id=16076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16076", "LEI": "54930000016076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    16077: SanctionedItem(
        sdn_id=16077,
        name="Kim Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16077"},
        aliases=["Petrov, Kim", "K. Petrov"]
    ),
    16078: SanctionedItem(
        sdn_id=16078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16078", "LEI": "54930000016078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    16079: SanctionedItem(
        sdn_id=16079,
        name="Park Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16079"},
        aliases=["Volkov, Park", "P. Volkov"]
    ),
    16080: SanctionedItem(
        sdn_id=16080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16080", "LEI": "54930000016080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    16081: SanctionedItem(
        sdn_id=16081,
        name="Chen Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16081"},
        aliases=["Popov, Chen", "C. Popov"]
    ),
    16082: SanctionedItem(
        sdn_id=16082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16082", "LEI": "54930000016082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    16083: SanctionedItem(
        sdn_id=16083,
        name="Wang Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16083"},
        aliases=["Hosseini, Wang", "W. Hosseini"]
    ),
    16084: SanctionedItem(
        sdn_id=16084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16084", "LEI": "54930000016084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    16085: SanctionedItem(
        sdn_id=16085,
        name="Zhang Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16085"},
        aliases=["Jafari, Zhang", "Z. Jafari"]
    ),
    16086: SanctionedItem(
        sdn_id=16086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16086", "LEI": "54930000016086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    16087: SanctionedItem(
        sdn_id=16087,
        name="Carlos Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16087"},
        aliases=["Jong-un, Carlos", "C. Jong-un"]
    ),
    16088: SanctionedItem(
        sdn_id=16088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16088", "LEI": "54930000016088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    16089: SanctionedItem(
        sdn_id=16089,
        name="Raul Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16089"},
        aliases=["Kwang-hyok, Raul", "R. Kwang-hyok"]
    ),
    16090: SanctionedItem(
        sdn_id=16090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16090", "LEI": "54930000016090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    16091: SanctionedItem(
        sdn_id=16091,
        name="Ernesto Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16091"},
        aliases=["Gang, Ernesto", "E. Gang"]
    ),
    16092: SanctionedItem(
        sdn_id=16092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16092", "LEI": "54930000016092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    16093: SanctionedItem(
        sdn_id=16093,
        name="Ibrahim Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16093"},
        aliases=["Morales, Ibrahim", "I. Morales"]
    ),
    16094: SanctionedItem(
        sdn_id=16094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16094", "LEI": "54930000016094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    16095: SanctionedItem(
        sdn_id=16095,
        name="Tariq Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16095"},
        aliases=["Flores, Tariq", "T. Flores"]
    ),
    16096: SanctionedItem(
        sdn_id=16096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16096", "LEI": "54930000016096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    16097: SanctionedItem(
        sdn_id=16097,
        name="Nikolai Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16097"},
        aliases=["Petrov, Nikolai", "N. Petrov"]
    ),
    16098: SanctionedItem(
        sdn_id=16098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16098", "LEI": "54930000016098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    16099: SanctionedItem(
        sdn_id=16099,
        name="Vladimir Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16099"},
        aliases=["Volkov, Vladimir", "V. Volkov"]
    ),
    16100: SanctionedItem(
        sdn_id=16100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16100", "LEI": "54930000016100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    16101: SanctionedItem(
        sdn_id=16101,
        name="Andrei Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16101"},
        aliases=["Popov, Andrei", "A. Popov"]
    ),
    16102: SanctionedItem(
        sdn_id=16102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16102", "LEI": "54930000016102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    16103: SanctionedItem(
        sdn_id=16103,
        name="Mikhail Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16103"},
        aliases=["Hosseini, Mikhail", "M. Hosseini"]
    ),
    16104: SanctionedItem(
        sdn_id=16104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16104", "LEI": "54930000016104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    16105: SanctionedItem(
        sdn_id=16105,
        name="Reza Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16105"},
        aliases=["Jafari, Reza", "R. Jafari"]
    ),
    16106: SanctionedItem(
        sdn_id=16106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16106", "LEI": "54930000016106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    16107: SanctionedItem(
        sdn_id=16107,
        name="Farhad Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16107"},
        aliases=["Jong-un, Farhad", "F. Jong-un"]
    ),
    16108: SanctionedItem(
        sdn_id=16108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16108", "LEI": "54930000016108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    16109: SanctionedItem(
        sdn_id=16109,
        name="Mahmoud Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16109"},
        aliases=["Kwang-hyok, Mahmoud", "M. Kwang-hyok"]
    ),
    16110: SanctionedItem(
        sdn_id=16110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16110", "LEI": "54930000016110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    16111: SanctionedItem(
        sdn_id=16111,
        name="Slobodan Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16111"},
        aliases=["Gang, Slobodan", "S. Gang"]
    ),
    16112: SanctionedItem(
        sdn_id=16112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16112", "LEI": "54930000016112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    16113: SanctionedItem(
        sdn_id=16113,
        name="Radovan Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16113"},
        aliases=["Morales, Radovan", "R. Morales"]
    ),
    16114: SanctionedItem(
        sdn_id=16114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16114", "LEI": "54930000016114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    16115: SanctionedItem(
        sdn_id=16115,
        name="Goran Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16115"},
        aliases=["Flores, Goran", "G. Flores"]
    ),
    16116: SanctionedItem(
        sdn_id=16116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16116", "LEI": "54930000016116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    16117: SanctionedItem(
        sdn_id=16117,
        name="Milorad Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16117"},
        aliases=["Petrov, Milorad", "M. Petrov"]
    ),
    16118: SanctionedItem(
        sdn_id=16118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16118", "LEI": "54930000016118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    16119: SanctionedItem(
        sdn_id=16119,
        name="Jean-Pierre Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16119"},
        aliases=["Volkov, Jean-Pierre", "J. Volkov"]
    ),
    16120: SanctionedItem(
        sdn_id=16120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16120", "LEI": "54930000016120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    16121: SanctionedItem(
        sdn_id=16121,
        name="Viktor Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16121"},
        aliases=["Popov, Viktor", "V. Popov"]
    ),
    16122: SanctionedItem(
        sdn_id=16122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16122", "LEI": "54930000016122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    16123: SanctionedItem(
        sdn_id=16123,
        name="Dmitry Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16123"},
        aliases=["Hosseini, Dmitry", "D. Hosseini"]
    ),
    16124: SanctionedItem(
        sdn_id=16124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16124", "LEI": "54930000016124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    16125: SanctionedItem(
        sdn_id=16125,
        name="Sergei Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16125"},
        aliases=["Jafari, Sergei", "S. Jafari"]
    ),
    16126: SanctionedItem(
        sdn_id=16126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16126", "LEI": "54930000016126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    16127: SanctionedItem(
        sdn_id=16127,
        name="Alexander Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16127"},
        aliases=["Jong-un, Alexander", "A. Jong-un"]
    ),
    16128: SanctionedItem(
        sdn_id=16128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16128", "LEI": "54930000016128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    16129: SanctionedItem(
        sdn_id=16129,
        name="Mohammad Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16129"},
        aliases=["Kwang-hyok, Mohammad", "M. Kwang-hyok"]
    ),
    16130: SanctionedItem(
        sdn_id=16130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16130", "LEI": "54930000016130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    16131: SanctionedItem(
        sdn_id=16131,
        name="Hassan Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16131"},
        aliases=["Gang, Hassan", "H. Gang"]
    ),
    16132: SanctionedItem(
        sdn_id=16132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16132", "LEI": "54930000016132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    16133: SanctionedItem(
        sdn_id=16133,
        name="Ali Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16133"},
        aliases=["Morales, Ali", "A. Morales"]
    ),
    16134: SanctionedItem(
        sdn_id=16134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16134", "LEI": "54930000016134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    16135: SanctionedItem(
        sdn_id=16135,
        name="Ahmad Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16135"},
        aliases=["Flores, Ahmad", "A. Flores"]
    ),
    16136: SanctionedItem(
        sdn_id=16136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16136", "LEI": "54930000016136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    16137: SanctionedItem(
        sdn_id=16137,
        name="Kim Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16137"},
        aliases=["Petrov, Kim", "K. Petrov"]
    ),
    16138: SanctionedItem(
        sdn_id=16138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16138", "LEI": "54930000016138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    16139: SanctionedItem(
        sdn_id=16139,
        name="Park Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16139"},
        aliases=["Volkov, Park", "P. Volkov"]
    ),
    16140: SanctionedItem(
        sdn_id=16140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16140", "LEI": "54930000016140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    16141: SanctionedItem(
        sdn_id=16141,
        name="Chen Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16141"},
        aliases=["Popov, Chen", "C. Popov"]
    ),
    16142: SanctionedItem(
        sdn_id=16142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16142", "LEI": "54930000016142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    16143: SanctionedItem(
        sdn_id=16143,
        name="Wang Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16143"},
        aliases=["Hosseini, Wang", "W. Hosseini"]
    ),
    16144: SanctionedItem(
        sdn_id=16144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16144", "LEI": "54930000016144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    16145: SanctionedItem(
        sdn_id=16145,
        name="Zhang Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16145"},
        aliases=["Jafari, Zhang", "Z. Jafari"]
    ),
    16146: SanctionedItem(
        sdn_id=16146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16146", "LEI": "54930000016146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    16147: SanctionedItem(
        sdn_id=16147,
        name="Carlos Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16147"},
        aliases=["Jong-un, Carlos", "C. Jong-un"]
    ),
    16148: SanctionedItem(
        sdn_id=16148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16148", "LEI": "54930000016148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    16149: SanctionedItem(
        sdn_id=16149,
        name="Raul Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16149"},
        aliases=["Kwang-hyok, Raul", "R. Kwang-hyok"]
    ),
    16150: SanctionedItem(
        sdn_id=16150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16150", "LEI": "54930000016150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    16151: SanctionedItem(
        sdn_id=16151,
        name="Ernesto Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16151"},
        aliases=["Gang, Ernesto", "E. Gang"]
    ),
    16152: SanctionedItem(
        sdn_id=16152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16152", "LEI": "54930000016152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    16153: SanctionedItem(
        sdn_id=16153,
        name="Ibrahim Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16153"},
        aliases=["Morales, Ibrahim", "I. Morales"]
    ),
    16154: SanctionedItem(
        sdn_id=16154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16154", "LEI": "54930000016154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    16155: SanctionedItem(
        sdn_id=16155,
        name="Tariq Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16155"},
        aliases=["Flores, Tariq", "T. Flores"]
    ),
    16156: SanctionedItem(
        sdn_id=16156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16156", "LEI": "54930000016156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    16157: SanctionedItem(
        sdn_id=16157,
        name="Nikolai Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16157"},
        aliases=["Petrov, Nikolai", "N. Petrov"]
    ),
    16158: SanctionedItem(
        sdn_id=16158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16158", "LEI": "54930000016158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    16159: SanctionedItem(
        sdn_id=16159,
        name="Vladimir Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16159"},
        aliases=["Volkov, Vladimir", "V. Volkov"]
    ),
    16160: SanctionedItem(
        sdn_id=16160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16160", "LEI": "54930000016160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    16161: SanctionedItem(
        sdn_id=16161,
        name="Andrei Popov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16161"},
        aliases=["Popov, Andrei", "A. Popov"]
    ),
    16162: SanctionedItem(
        sdn_id=16162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16162", "LEI": "54930000016162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    16163: SanctionedItem(
        sdn_id=16163,
        name="Mikhail Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16163"},
        aliases=["Hosseini, Mikhail", "M. Hosseini"]
    ),
    16164: SanctionedItem(
        sdn_id=16164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16164", "LEI": "54930000016164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    16165: SanctionedItem(
        sdn_id=16165,
        name="Reza Jafari",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16165"},
        aliases=["Jafari, Reza", "R. Jafari"]
    ),
    16166: SanctionedItem(
        sdn_id=16166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16166", "LEI": "54930000016166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    16167: SanctionedItem(
        sdn_id=16167,
        name="Farhad Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16167"},
        aliases=["Jong-un, Farhad", "F. Jong-un"]
    ),
    16168: SanctionedItem(
        sdn_id=16168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16168", "LEI": "54930000016168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    16169: SanctionedItem(
        sdn_id=16169,
        name="Mahmoud Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16169"},
        aliases=["Kwang-hyok, Mahmoud", "M. Kwang-hyok"]
    ),
    16170: SanctionedItem(
        sdn_id=16170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16170", "LEI": "54930000016170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    16171: SanctionedItem(
        sdn_id=16171,
        name="Slobodan Gang",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16171"},
        aliases=["Gang, Slobodan", "S. Gang"]
    ),
    16172: SanctionedItem(
        sdn_id=16172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16172", "LEI": "54930000016172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    16173: SanctionedItem(
        sdn_id=16173,
        name="Radovan Morales",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16173"},
        aliases=["Morales, Radovan", "R. Morales"]
    ),
    16174: SanctionedItem(
        sdn_id=16174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16174", "LEI": "54930000016174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    16175: SanctionedItem(
        sdn_id=16175,
        name="Goran Flores",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16175"},
        aliases=["Flores, Goran", "G. Flores"]
    ),
    16176: SanctionedItem(
        sdn_id=16176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16176", "LEI": "54930000016176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    16177: SanctionedItem(
        sdn_id=16177,
        name="Milorad Petrov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16177"},
        aliases=["Petrov, Milorad", "M. Petrov"]
    ),
    16178: SanctionedItem(
        sdn_id=16178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["CYBER2"],
        remarks="Designated entity under CYBER2 enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-16178", "LEI": "54930000016178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    16179: SanctionedItem(
        sdn_id=16179,
        name="Jean-Pierre Volkov",
        sdn_type="INDIVIDUAL",
        programs=["CYBER2"],
        remarks="Designated individual under CYBER2; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-16179"},
        aliases=["Volkov, Jean-Pierre", "J. Volkov"]
    ),
}

"""
East Asia & Counter-Proliferation Sanctions.
North Korea Non-Proliferation Regulations.
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

RECORDS_EAST_ASIA_SANCTIONS: Dict[int, SanctionedItem] = {
    13000: SanctionedItem(
        sdn_id=13000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13000", "LEI": "54930000013000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    13001: SanctionedItem(
        sdn_id=13001,
        name="Viktor Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13001"},
        aliases=["Volkov, Viktor", "V. Volkov"]
    ),
    13002: SanctionedItem(
        sdn_id=13002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13002", "LEI": "54930000013002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    13003: SanctionedItem(
        sdn_id=13003,
        name="Dmitry Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13003"},
        aliases=["Popov, Dmitry", "D. Popov"]
    ),
    13004: SanctionedItem(
        sdn_id=13004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13004", "LEI": "54930000013004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    13005: SanctionedItem(
        sdn_id=13005,
        name="Sergei Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13005"},
        aliases=["Hosseini, Sergei", "S. Hosseini"]
    ),
    13006: SanctionedItem(
        sdn_id=13006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13006", "LEI": "54930000013006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    13007: SanctionedItem(
        sdn_id=13007,
        name="Alexander Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13007"},
        aliases=["Jafari, Alexander", "A. Jafari"]
    ),
    13008: SanctionedItem(
        sdn_id=13008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13008", "LEI": "54930000013008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    13009: SanctionedItem(
        sdn_id=13009,
        name="Mohammad Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13009"},
        aliases=["Jong-un, Mohammad", "M. Jong-un"]
    ),
    13010: SanctionedItem(
        sdn_id=13010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13010", "LEI": "54930000013010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    13011: SanctionedItem(
        sdn_id=13011,
        name="Hassan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13011"},
        aliases=["Kwang-hyok, Hassan", "H. Kwang-hyok"]
    ),
    13012: SanctionedItem(
        sdn_id=13012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13012", "LEI": "54930000013012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    13013: SanctionedItem(
        sdn_id=13013,
        name="Ali Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13013"},
        aliases=["Gang, Ali", "A. Gang"]
    ),
    13014: SanctionedItem(
        sdn_id=13014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13014", "LEI": "54930000013014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    13015: SanctionedItem(
        sdn_id=13015,
        name="Ahmad Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13015"},
        aliases=["Morales, Ahmad", "A. Morales"]
    ),
    13016: SanctionedItem(
        sdn_id=13016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13016", "LEI": "54930000013016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    13017: SanctionedItem(
        sdn_id=13017,
        name="Kim Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13017"},
        aliases=["Flores, Kim", "K. Flores"]
    ),
    13018: SanctionedItem(
        sdn_id=13018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13018", "LEI": "54930000013018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    13019: SanctionedItem(
        sdn_id=13019,
        name="Park Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13019"},
        aliases=["Petrov, Park", "P. Petrov"]
    ),
    13020: SanctionedItem(
        sdn_id=13020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13020", "LEI": "54930000013020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    13021: SanctionedItem(
        sdn_id=13021,
        name="Chen Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13021"},
        aliases=["Volkov, Chen", "C. Volkov"]
    ),
    13022: SanctionedItem(
        sdn_id=13022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13022", "LEI": "54930000013022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    13023: SanctionedItem(
        sdn_id=13023,
        name="Wang Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13023"},
        aliases=["Popov, Wang", "W. Popov"]
    ),
    13024: SanctionedItem(
        sdn_id=13024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13024", "LEI": "54930000013024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    13025: SanctionedItem(
        sdn_id=13025,
        name="Zhang Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13025"},
        aliases=["Hosseini, Zhang", "Z. Hosseini"]
    ),
    13026: SanctionedItem(
        sdn_id=13026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13026", "LEI": "54930000013026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    13027: SanctionedItem(
        sdn_id=13027,
        name="Carlos Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13027"},
        aliases=["Jafari, Carlos", "C. Jafari"]
    ),
    13028: SanctionedItem(
        sdn_id=13028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13028", "LEI": "54930000013028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    13029: SanctionedItem(
        sdn_id=13029,
        name="Raul Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13029"},
        aliases=["Jong-un, Raul", "R. Jong-un"]
    ),
    13030: SanctionedItem(
        sdn_id=13030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13030", "LEI": "54930000013030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    13031: SanctionedItem(
        sdn_id=13031,
        name="Ernesto Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13031"},
        aliases=["Kwang-hyok, Ernesto", "E. Kwang-hyok"]
    ),
    13032: SanctionedItem(
        sdn_id=13032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13032", "LEI": "54930000013032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    13033: SanctionedItem(
        sdn_id=13033,
        name="Ibrahim Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13033"},
        aliases=["Gang, Ibrahim", "I. Gang"]
    ),
    13034: SanctionedItem(
        sdn_id=13034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13034", "LEI": "54930000013034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    13035: SanctionedItem(
        sdn_id=13035,
        name="Tariq Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13035"},
        aliases=["Morales, Tariq", "T. Morales"]
    ),
    13036: SanctionedItem(
        sdn_id=13036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13036", "LEI": "54930000013036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    13037: SanctionedItem(
        sdn_id=13037,
        name="Nikolai Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13037"},
        aliases=["Flores, Nikolai", "N. Flores"]
    ),
    13038: SanctionedItem(
        sdn_id=13038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13038", "LEI": "54930000013038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    13039: SanctionedItem(
        sdn_id=13039,
        name="Vladimir Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13039"},
        aliases=["Petrov, Vladimir", "V. Petrov"]
    ),
    13040: SanctionedItem(
        sdn_id=13040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13040", "LEI": "54930000013040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    13041: SanctionedItem(
        sdn_id=13041,
        name="Andrei Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13041"},
        aliases=["Volkov, Andrei", "A. Volkov"]
    ),
    13042: SanctionedItem(
        sdn_id=13042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13042", "LEI": "54930000013042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    13043: SanctionedItem(
        sdn_id=13043,
        name="Mikhail Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13043"},
        aliases=["Popov, Mikhail", "M. Popov"]
    ),
    13044: SanctionedItem(
        sdn_id=13044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13044", "LEI": "54930000013044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    13045: SanctionedItem(
        sdn_id=13045,
        name="Reza Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13045"},
        aliases=["Hosseini, Reza", "R. Hosseini"]
    ),
    13046: SanctionedItem(
        sdn_id=13046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13046", "LEI": "54930000013046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    13047: SanctionedItem(
        sdn_id=13047,
        name="Farhad Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13047"},
        aliases=["Jafari, Farhad", "F. Jafari"]
    ),
    13048: SanctionedItem(
        sdn_id=13048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13048", "LEI": "54930000013048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    13049: SanctionedItem(
        sdn_id=13049,
        name="Mahmoud Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13049"},
        aliases=["Jong-un, Mahmoud", "M. Jong-un"]
    ),
    13050: SanctionedItem(
        sdn_id=13050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13050", "LEI": "54930000013050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    13051: SanctionedItem(
        sdn_id=13051,
        name="Slobodan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13051"},
        aliases=["Kwang-hyok, Slobodan", "S. Kwang-hyok"]
    ),
    13052: SanctionedItem(
        sdn_id=13052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13052", "LEI": "54930000013052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    13053: SanctionedItem(
        sdn_id=13053,
        name="Radovan Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13053"},
        aliases=["Gang, Radovan", "R. Gang"]
    ),
    13054: SanctionedItem(
        sdn_id=13054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13054", "LEI": "54930000013054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    13055: SanctionedItem(
        sdn_id=13055,
        name="Goran Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13055"},
        aliases=["Morales, Goran", "G. Morales"]
    ),
    13056: SanctionedItem(
        sdn_id=13056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13056", "LEI": "54930000013056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    13057: SanctionedItem(
        sdn_id=13057,
        name="Milorad Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13057"},
        aliases=["Flores, Milorad", "M. Flores"]
    ),
    13058: SanctionedItem(
        sdn_id=13058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13058", "LEI": "54930000013058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    13059: SanctionedItem(
        sdn_id=13059,
        name="Jean-Pierre Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13059"},
        aliases=["Petrov, Jean-Pierre", "J. Petrov"]
    ),
    13060: SanctionedItem(
        sdn_id=13060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13060", "LEI": "54930000013060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    13061: SanctionedItem(
        sdn_id=13061,
        name="Viktor Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13061"},
        aliases=["Volkov, Viktor", "V. Volkov"]
    ),
    13062: SanctionedItem(
        sdn_id=13062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13062", "LEI": "54930000013062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    13063: SanctionedItem(
        sdn_id=13063,
        name="Dmitry Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13063"},
        aliases=["Popov, Dmitry", "D. Popov"]
    ),
    13064: SanctionedItem(
        sdn_id=13064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13064", "LEI": "54930000013064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    13065: SanctionedItem(
        sdn_id=13065,
        name="Sergei Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13065"},
        aliases=["Hosseini, Sergei", "S. Hosseini"]
    ),
    13066: SanctionedItem(
        sdn_id=13066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13066", "LEI": "54930000013066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    13067: SanctionedItem(
        sdn_id=13067,
        name="Alexander Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13067"},
        aliases=["Jafari, Alexander", "A. Jafari"]
    ),
    13068: SanctionedItem(
        sdn_id=13068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13068", "LEI": "54930000013068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    13069: SanctionedItem(
        sdn_id=13069,
        name="Mohammad Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13069"},
        aliases=["Jong-un, Mohammad", "M. Jong-un"]
    ),
    13070: SanctionedItem(
        sdn_id=13070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13070", "LEI": "54930000013070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    13071: SanctionedItem(
        sdn_id=13071,
        name="Hassan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13071"},
        aliases=["Kwang-hyok, Hassan", "H. Kwang-hyok"]
    ),
    13072: SanctionedItem(
        sdn_id=13072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13072", "LEI": "54930000013072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    13073: SanctionedItem(
        sdn_id=13073,
        name="Ali Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13073"},
        aliases=["Gang, Ali", "A. Gang"]
    ),
    13074: SanctionedItem(
        sdn_id=13074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13074", "LEI": "54930000013074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    13075: SanctionedItem(
        sdn_id=13075,
        name="Ahmad Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13075"},
        aliases=["Morales, Ahmad", "A. Morales"]
    ),
    13076: SanctionedItem(
        sdn_id=13076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13076", "LEI": "54930000013076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    13077: SanctionedItem(
        sdn_id=13077,
        name="Kim Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13077"},
        aliases=["Flores, Kim", "K. Flores"]
    ),
    13078: SanctionedItem(
        sdn_id=13078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13078", "LEI": "54930000013078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    13079: SanctionedItem(
        sdn_id=13079,
        name="Park Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13079"},
        aliases=["Petrov, Park", "P. Petrov"]
    ),
    13080: SanctionedItem(
        sdn_id=13080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13080", "LEI": "54930000013080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    13081: SanctionedItem(
        sdn_id=13081,
        name="Chen Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13081"},
        aliases=["Volkov, Chen", "C. Volkov"]
    ),
    13082: SanctionedItem(
        sdn_id=13082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13082", "LEI": "54930000013082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    13083: SanctionedItem(
        sdn_id=13083,
        name="Wang Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13083"},
        aliases=["Popov, Wang", "W. Popov"]
    ),
    13084: SanctionedItem(
        sdn_id=13084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13084", "LEI": "54930000013084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    13085: SanctionedItem(
        sdn_id=13085,
        name="Zhang Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13085"},
        aliases=["Hosseini, Zhang", "Z. Hosseini"]
    ),
    13086: SanctionedItem(
        sdn_id=13086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13086", "LEI": "54930000013086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    13087: SanctionedItem(
        sdn_id=13087,
        name="Carlos Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13087"},
        aliases=["Jafari, Carlos", "C. Jafari"]
    ),
    13088: SanctionedItem(
        sdn_id=13088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13088", "LEI": "54930000013088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    13089: SanctionedItem(
        sdn_id=13089,
        name="Raul Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13089"},
        aliases=["Jong-un, Raul", "R. Jong-un"]
    ),
    13090: SanctionedItem(
        sdn_id=13090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13090", "LEI": "54930000013090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    13091: SanctionedItem(
        sdn_id=13091,
        name="Ernesto Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13091"},
        aliases=["Kwang-hyok, Ernesto", "E. Kwang-hyok"]
    ),
    13092: SanctionedItem(
        sdn_id=13092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13092", "LEI": "54930000013092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    13093: SanctionedItem(
        sdn_id=13093,
        name="Ibrahim Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13093"},
        aliases=["Gang, Ibrahim", "I. Gang"]
    ),
    13094: SanctionedItem(
        sdn_id=13094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13094", "LEI": "54930000013094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    13095: SanctionedItem(
        sdn_id=13095,
        name="Tariq Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13095"},
        aliases=["Morales, Tariq", "T. Morales"]
    ),
    13096: SanctionedItem(
        sdn_id=13096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13096", "LEI": "54930000013096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    13097: SanctionedItem(
        sdn_id=13097,
        name="Nikolai Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13097"},
        aliases=["Flores, Nikolai", "N. Flores"]
    ),
    13098: SanctionedItem(
        sdn_id=13098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13098", "LEI": "54930000013098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    13099: SanctionedItem(
        sdn_id=13099,
        name="Vladimir Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13099"},
        aliases=["Petrov, Vladimir", "V. Petrov"]
    ),
    13100: SanctionedItem(
        sdn_id=13100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13100", "LEI": "54930000013100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    13101: SanctionedItem(
        sdn_id=13101,
        name="Andrei Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13101"},
        aliases=["Volkov, Andrei", "A. Volkov"]
    ),
    13102: SanctionedItem(
        sdn_id=13102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13102", "LEI": "54930000013102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    13103: SanctionedItem(
        sdn_id=13103,
        name="Mikhail Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13103"},
        aliases=["Popov, Mikhail", "M. Popov"]
    ),
    13104: SanctionedItem(
        sdn_id=13104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13104", "LEI": "54930000013104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    13105: SanctionedItem(
        sdn_id=13105,
        name="Reza Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13105"},
        aliases=["Hosseini, Reza", "R. Hosseini"]
    ),
    13106: SanctionedItem(
        sdn_id=13106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13106", "LEI": "54930000013106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    13107: SanctionedItem(
        sdn_id=13107,
        name="Farhad Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13107"},
        aliases=["Jafari, Farhad", "F. Jafari"]
    ),
    13108: SanctionedItem(
        sdn_id=13108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13108", "LEI": "54930000013108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    13109: SanctionedItem(
        sdn_id=13109,
        name="Mahmoud Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13109"},
        aliases=["Jong-un, Mahmoud", "M. Jong-un"]
    ),
    13110: SanctionedItem(
        sdn_id=13110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13110", "LEI": "54930000013110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    13111: SanctionedItem(
        sdn_id=13111,
        name="Slobodan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13111"},
        aliases=["Kwang-hyok, Slobodan", "S. Kwang-hyok"]
    ),
    13112: SanctionedItem(
        sdn_id=13112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13112", "LEI": "54930000013112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    13113: SanctionedItem(
        sdn_id=13113,
        name="Radovan Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13113"},
        aliases=["Gang, Radovan", "R. Gang"]
    ),
    13114: SanctionedItem(
        sdn_id=13114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13114", "LEI": "54930000013114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    13115: SanctionedItem(
        sdn_id=13115,
        name="Goran Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13115"},
        aliases=["Morales, Goran", "G. Morales"]
    ),
    13116: SanctionedItem(
        sdn_id=13116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13116", "LEI": "54930000013116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    13117: SanctionedItem(
        sdn_id=13117,
        name="Milorad Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13117"},
        aliases=["Flores, Milorad", "M. Flores"]
    ),
    13118: SanctionedItem(
        sdn_id=13118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13118", "LEI": "54930000013118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    13119: SanctionedItem(
        sdn_id=13119,
        name="Jean-Pierre Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13119"},
        aliases=["Petrov, Jean-Pierre", "J. Petrov"]
    ),
    13120: SanctionedItem(
        sdn_id=13120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13120", "LEI": "54930000013120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    13121: SanctionedItem(
        sdn_id=13121,
        name="Viktor Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13121"},
        aliases=["Volkov, Viktor", "V. Volkov"]
    ),
    13122: SanctionedItem(
        sdn_id=13122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13122", "LEI": "54930000013122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    13123: SanctionedItem(
        sdn_id=13123,
        name="Dmitry Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13123"},
        aliases=["Popov, Dmitry", "D. Popov"]
    ),
    13124: SanctionedItem(
        sdn_id=13124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13124", "LEI": "54930000013124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    13125: SanctionedItem(
        sdn_id=13125,
        name="Sergei Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13125"},
        aliases=["Hosseini, Sergei", "S. Hosseini"]
    ),
    13126: SanctionedItem(
        sdn_id=13126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13126", "LEI": "54930000013126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    13127: SanctionedItem(
        sdn_id=13127,
        name="Alexander Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13127"},
        aliases=["Jafari, Alexander", "A. Jafari"]
    ),
    13128: SanctionedItem(
        sdn_id=13128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13128", "LEI": "54930000013128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    13129: SanctionedItem(
        sdn_id=13129,
        name="Mohammad Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13129"},
        aliases=["Jong-un, Mohammad", "M. Jong-un"]
    ),
    13130: SanctionedItem(
        sdn_id=13130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13130", "LEI": "54930000013130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    13131: SanctionedItem(
        sdn_id=13131,
        name="Hassan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13131"},
        aliases=["Kwang-hyok, Hassan", "H. Kwang-hyok"]
    ),
    13132: SanctionedItem(
        sdn_id=13132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13132", "LEI": "54930000013132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    13133: SanctionedItem(
        sdn_id=13133,
        name="Ali Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13133"},
        aliases=["Gang, Ali", "A. Gang"]
    ),
    13134: SanctionedItem(
        sdn_id=13134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13134", "LEI": "54930000013134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    13135: SanctionedItem(
        sdn_id=13135,
        name="Ahmad Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13135"},
        aliases=["Morales, Ahmad", "A. Morales"]
    ),
    13136: SanctionedItem(
        sdn_id=13136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13136", "LEI": "54930000013136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    13137: SanctionedItem(
        sdn_id=13137,
        name="Kim Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13137"},
        aliases=["Flores, Kim", "K. Flores"]
    ),
    13138: SanctionedItem(
        sdn_id=13138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13138", "LEI": "54930000013138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    13139: SanctionedItem(
        sdn_id=13139,
        name="Park Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13139"},
        aliases=["Petrov, Park", "P. Petrov"]
    ),
    13140: SanctionedItem(
        sdn_id=13140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13140", "LEI": "54930000013140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    13141: SanctionedItem(
        sdn_id=13141,
        name="Chen Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13141"},
        aliases=["Volkov, Chen", "C. Volkov"]
    ),
    13142: SanctionedItem(
        sdn_id=13142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13142", "LEI": "54930000013142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    13143: SanctionedItem(
        sdn_id=13143,
        name="Wang Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13143"},
        aliases=["Popov, Wang", "W. Popov"]
    ),
    13144: SanctionedItem(
        sdn_id=13144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13144", "LEI": "54930000013144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    13145: SanctionedItem(
        sdn_id=13145,
        name="Zhang Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13145"},
        aliases=["Hosseini, Zhang", "Z. Hosseini"]
    ),
    13146: SanctionedItem(
        sdn_id=13146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13146", "LEI": "54930000013146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    13147: SanctionedItem(
        sdn_id=13147,
        name="Carlos Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13147"},
        aliases=["Jafari, Carlos", "C. Jafari"]
    ),
    13148: SanctionedItem(
        sdn_id=13148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13148", "LEI": "54930000013148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    13149: SanctionedItem(
        sdn_id=13149,
        name="Raul Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13149"},
        aliases=["Jong-un, Raul", "R. Jong-un"]
    ),
    13150: SanctionedItem(
        sdn_id=13150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13150", "LEI": "54930000013150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    13151: SanctionedItem(
        sdn_id=13151,
        name="Ernesto Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13151"},
        aliases=["Kwang-hyok, Ernesto", "E. Kwang-hyok"]
    ),
    13152: SanctionedItem(
        sdn_id=13152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13152", "LEI": "54930000013152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    13153: SanctionedItem(
        sdn_id=13153,
        name="Ibrahim Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13153"},
        aliases=["Gang, Ibrahim", "I. Gang"]
    ),
    13154: SanctionedItem(
        sdn_id=13154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13154", "LEI": "54930000013154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    13155: SanctionedItem(
        sdn_id=13155,
        name="Tariq Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13155"},
        aliases=["Morales, Tariq", "T. Morales"]
    ),
    13156: SanctionedItem(
        sdn_id=13156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13156", "LEI": "54930000013156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    13157: SanctionedItem(
        sdn_id=13157,
        name="Nikolai Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13157"},
        aliases=["Flores, Nikolai", "N. Flores"]
    ),
    13158: SanctionedItem(
        sdn_id=13158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13158", "LEI": "54930000013158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    13159: SanctionedItem(
        sdn_id=13159,
        name="Vladimir Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13159"},
        aliases=["Petrov, Vladimir", "V. Petrov"]
    ),
    13160: SanctionedItem(
        sdn_id=13160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13160", "LEI": "54930000013160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    13161: SanctionedItem(
        sdn_id=13161,
        name="Andrei Volkov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13161"},
        aliases=["Volkov, Andrei", "A. Volkov"]
    ),
    13162: SanctionedItem(
        sdn_id=13162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13162", "LEI": "54930000013162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    13163: SanctionedItem(
        sdn_id=13163,
        name="Mikhail Popov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13163"},
        aliases=["Popov, Mikhail", "M. Popov"]
    ),
    13164: SanctionedItem(
        sdn_id=13164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13164", "LEI": "54930000013164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    13165: SanctionedItem(
        sdn_id=13165,
        name="Reza Hosseini",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13165"},
        aliases=["Hosseini, Reza", "R. Hosseini"]
    ),
    13166: SanctionedItem(
        sdn_id=13166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13166", "LEI": "54930000013166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    13167: SanctionedItem(
        sdn_id=13167,
        name="Farhad Jafari",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13167"},
        aliases=["Jafari, Farhad", "F. Jafari"]
    ),
    13168: SanctionedItem(
        sdn_id=13168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13168", "LEI": "54930000013168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    13169: SanctionedItem(
        sdn_id=13169,
        name="Mahmoud Jong-un",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13169"},
        aliases=["Jong-un, Mahmoud", "M. Jong-un"]
    ),
    13170: SanctionedItem(
        sdn_id=13170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13170", "LEI": "54930000013170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    13171: SanctionedItem(
        sdn_id=13171,
        name="Slobodan Kwang-hyok",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13171"},
        aliases=["Kwang-hyok, Slobodan", "S. Kwang-hyok"]
    ),
    13172: SanctionedItem(
        sdn_id=13172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13172", "LEI": "54930000013172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    13173: SanctionedItem(
        sdn_id=13173,
        name="Radovan Gang",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13173"},
        aliases=["Gang, Radovan", "R. Gang"]
    ),
    13174: SanctionedItem(
        sdn_id=13174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13174", "LEI": "54930000013174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    13175: SanctionedItem(
        sdn_id=13175,
        name="Goran Morales",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13175"},
        aliases=["Morales, Goran", "G. Morales"]
    ),
    13176: SanctionedItem(
        sdn_id=13176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13176", "LEI": "54930000013176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    13177: SanctionedItem(
        sdn_id=13177,
        name="Milorad Flores",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13177"},
        aliases=["Flores, Milorad", "M. Flores"]
    ),
    13178: SanctionedItem(
        sdn_id=13178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["DPRK"],
        remarks="Designated entity under DPRK enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-13178", "LEI": "54930000013178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    13179: SanctionedItem(
        sdn_id=13179,
        name="Jean-Pierre Petrov",
        sdn_type="INDIVIDUAL",
        programs=["DPRK"],
        remarks="Designated individual under DPRK; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-13179"},
        aliases=["Petrov, Jean-Pierre", "J. Petrov"]
    ),
}

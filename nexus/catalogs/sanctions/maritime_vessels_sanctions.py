"""
Maritime Shadow Fleet & Vessel Sanctions.
Illicit Petroleum Ship-to-Ship Transshipment.
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

RECORDS_MARITIME_VESSELS_SANCTIONS: Dict[int, SanctionedItem] = {
    15000: SanctionedItem(
        sdn_id=15000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15000", "LEI": "54930000015000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    15001: SanctionedItem(
        sdn_id=15001,
        name="Viktor Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15001"},
        aliases=["Kuznetsov, Viktor", "V. Kuznetsov"]
    ),
    15002: SanctionedItem(
        sdn_id=15002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15002", "LEI": "54930000015002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    15003: SanctionedItem(
        sdn_id=15003,
        name="Dmitry Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15003"},
        aliases=["Mousavi, Dmitry", "D. Mousavi"]
    ),
    15004: SanctionedItem(
        sdn_id=15004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15004", "LEI": "54930000015004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    15005: SanctionedItem(
        sdn_id=15005,
        name="Sergei Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15005"},
        aliases=["Khamenei, Sergei", "S. Khamenei"]
    ),
    15006: SanctionedItem(
        sdn_id=15006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15006", "LEI": "54930000015006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    15007: SanctionedItem(
        sdn_id=15007,
        name="Alexander Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15007"},
        aliases=["Karimi, Alexander", "A. Karimi"]
    ),
    15008: SanctionedItem(
        sdn_id=15008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15008", "LEI": "54930000015008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    15009: SanctionedItem(
        sdn_id=15009,
        name="Mohammad Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15009"},
        aliases=["Myong-sik, Mohammad", "M. Myong-sik"]
    ),
    15010: SanctionedItem(
        sdn_id=15010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15010", "LEI": "54930000015010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    15011: SanctionedItem(
        sdn_id=15011,
        name="Hassan Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15011"},
        aliases=["Bo, Hassan", "H. Bo"]
    ),
    15012: SanctionedItem(
        sdn_id=15012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15012", "LEI": "54930000015012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    15013: SanctionedItem(
        sdn_id=15013,
        name="Ali Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15013"},
        aliases=["Rodriguez, Ali", "A. Rodriguez"]
    ),
    15014: SanctionedItem(
        sdn_id=15014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15014", "LEI": "54930000015014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    15015: SanctionedItem(
        sdn_id=15015,
        name="Ahmad Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15015"},
        aliases=["Maduro, Ahmad", "A. Maduro"]
    ),
    15016: SanctionedItem(
        sdn_id=15016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15016", "LEI": "54930000015016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    15017: SanctionedItem(
        sdn_id=15017,
        name="Kim Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15017"},
        aliases=["Al-Assad, Kim", "K. Al-Assad"]
    ),
    15018: SanctionedItem(
        sdn_id=15018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15018", "LEI": "54930000015018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    15019: SanctionedItem(
        sdn_id=15019,
        name="Park Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15019"},
        aliases=["Sidorov, Park", "P. Sidorov"]
    ),
    15020: SanctionedItem(
        sdn_id=15020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15020", "LEI": "54930000015020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    15021: SanctionedItem(
        sdn_id=15021,
        name="Chen Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15021"},
        aliases=["Kuznetsov, Chen", "C. Kuznetsov"]
    ),
    15022: SanctionedItem(
        sdn_id=15022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15022", "LEI": "54930000015022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    15023: SanctionedItem(
        sdn_id=15023,
        name="Wang Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15023"},
        aliases=["Mousavi, Wang", "W. Mousavi"]
    ),
    15024: SanctionedItem(
        sdn_id=15024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15024", "LEI": "54930000015024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    15025: SanctionedItem(
        sdn_id=15025,
        name="Zhang Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15025"},
        aliases=["Khamenei, Zhang", "Z. Khamenei"]
    ),
    15026: SanctionedItem(
        sdn_id=15026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15026", "LEI": "54930000015026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    15027: SanctionedItem(
        sdn_id=15027,
        name="Carlos Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15027"},
        aliases=["Karimi, Carlos", "C. Karimi"]
    ),
    15028: SanctionedItem(
        sdn_id=15028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15028", "LEI": "54930000015028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    15029: SanctionedItem(
        sdn_id=15029,
        name="Raul Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15029"},
        aliases=["Myong-sik, Raul", "R. Myong-sik"]
    ),
    15030: SanctionedItem(
        sdn_id=15030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15030", "LEI": "54930000015030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    15031: SanctionedItem(
        sdn_id=15031,
        name="Ernesto Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15031"},
        aliases=["Bo, Ernesto", "E. Bo"]
    ),
    15032: SanctionedItem(
        sdn_id=15032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15032", "LEI": "54930000015032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    15033: SanctionedItem(
        sdn_id=15033,
        name="Ibrahim Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15033"},
        aliases=["Rodriguez, Ibrahim", "I. Rodriguez"]
    ),
    15034: SanctionedItem(
        sdn_id=15034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15034", "LEI": "54930000015034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    15035: SanctionedItem(
        sdn_id=15035,
        name="Tariq Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15035"},
        aliases=["Maduro, Tariq", "T. Maduro"]
    ),
    15036: SanctionedItem(
        sdn_id=15036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15036", "LEI": "54930000015036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    15037: SanctionedItem(
        sdn_id=15037,
        name="Nikolai Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15037"},
        aliases=["Al-Assad, Nikolai", "N. Al-Assad"]
    ),
    15038: SanctionedItem(
        sdn_id=15038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15038", "LEI": "54930000015038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    15039: SanctionedItem(
        sdn_id=15039,
        name="Vladimir Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15039"},
        aliases=["Sidorov, Vladimir", "V. Sidorov"]
    ),
    15040: SanctionedItem(
        sdn_id=15040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15040", "LEI": "54930000015040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    15041: SanctionedItem(
        sdn_id=15041,
        name="Andrei Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15041"},
        aliases=["Kuznetsov, Andrei", "A. Kuznetsov"]
    ),
    15042: SanctionedItem(
        sdn_id=15042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15042", "LEI": "54930000015042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    15043: SanctionedItem(
        sdn_id=15043,
        name="Mikhail Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15043"},
        aliases=["Mousavi, Mikhail", "M. Mousavi"]
    ),
    15044: SanctionedItem(
        sdn_id=15044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15044", "LEI": "54930000015044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    15045: SanctionedItem(
        sdn_id=15045,
        name="Reza Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15045"},
        aliases=["Khamenei, Reza", "R. Khamenei"]
    ),
    15046: SanctionedItem(
        sdn_id=15046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15046", "LEI": "54930000015046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    15047: SanctionedItem(
        sdn_id=15047,
        name="Farhad Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15047"},
        aliases=["Karimi, Farhad", "F. Karimi"]
    ),
    15048: SanctionedItem(
        sdn_id=15048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15048", "LEI": "54930000015048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    15049: SanctionedItem(
        sdn_id=15049,
        name="Mahmoud Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15049"},
        aliases=["Myong-sik, Mahmoud", "M. Myong-sik"]
    ),
    15050: SanctionedItem(
        sdn_id=15050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15050", "LEI": "54930000015050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    15051: SanctionedItem(
        sdn_id=15051,
        name="Slobodan Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15051"},
        aliases=["Bo, Slobodan", "S. Bo"]
    ),
    15052: SanctionedItem(
        sdn_id=15052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15052", "LEI": "54930000015052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    15053: SanctionedItem(
        sdn_id=15053,
        name="Radovan Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15053"},
        aliases=["Rodriguez, Radovan", "R. Rodriguez"]
    ),
    15054: SanctionedItem(
        sdn_id=15054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15054", "LEI": "54930000015054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    15055: SanctionedItem(
        sdn_id=15055,
        name="Goran Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15055"},
        aliases=["Maduro, Goran", "G. Maduro"]
    ),
    15056: SanctionedItem(
        sdn_id=15056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15056", "LEI": "54930000015056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    15057: SanctionedItem(
        sdn_id=15057,
        name="Milorad Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15057"},
        aliases=["Al-Assad, Milorad", "M. Al-Assad"]
    ),
    15058: SanctionedItem(
        sdn_id=15058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15058", "LEI": "54930000015058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    15059: SanctionedItem(
        sdn_id=15059,
        name="Jean-Pierre Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15059"},
        aliases=["Sidorov, Jean-Pierre", "J. Sidorov"]
    ),
    15060: SanctionedItem(
        sdn_id=15060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15060", "LEI": "54930000015060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    15061: SanctionedItem(
        sdn_id=15061,
        name="Viktor Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15061"},
        aliases=["Kuznetsov, Viktor", "V. Kuznetsov"]
    ),
    15062: SanctionedItem(
        sdn_id=15062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15062", "LEI": "54930000015062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    15063: SanctionedItem(
        sdn_id=15063,
        name="Dmitry Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15063"},
        aliases=["Mousavi, Dmitry", "D. Mousavi"]
    ),
    15064: SanctionedItem(
        sdn_id=15064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15064", "LEI": "54930000015064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    15065: SanctionedItem(
        sdn_id=15065,
        name="Sergei Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15065"},
        aliases=["Khamenei, Sergei", "S. Khamenei"]
    ),
    15066: SanctionedItem(
        sdn_id=15066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15066", "LEI": "54930000015066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    15067: SanctionedItem(
        sdn_id=15067,
        name="Alexander Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15067"},
        aliases=["Karimi, Alexander", "A. Karimi"]
    ),
    15068: SanctionedItem(
        sdn_id=15068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15068", "LEI": "54930000015068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    15069: SanctionedItem(
        sdn_id=15069,
        name="Mohammad Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15069"},
        aliases=["Myong-sik, Mohammad", "M. Myong-sik"]
    ),
    15070: SanctionedItem(
        sdn_id=15070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15070", "LEI": "54930000015070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    15071: SanctionedItem(
        sdn_id=15071,
        name="Hassan Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15071"},
        aliases=["Bo, Hassan", "H. Bo"]
    ),
    15072: SanctionedItem(
        sdn_id=15072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15072", "LEI": "54930000015072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    15073: SanctionedItem(
        sdn_id=15073,
        name="Ali Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15073"},
        aliases=["Rodriguez, Ali", "A. Rodriguez"]
    ),
    15074: SanctionedItem(
        sdn_id=15074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15074", "LEI": "54930000015074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    15075: SanctionedItem(
        sdn_id=15075,
        name="Ahmad Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15075"},
        aliases=["Maduro, Ahmad", "A. Maduro"]
    ),
    15076: SanctionedItem(
        sdn_id=15076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15076", "LEI": "54930000015076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    15077: SanctionedItem(
        sdn_id=15077,
        name="Kim Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15077"},
        aliases=["Al-Assad, Kim", "K. Al-Assad"]
    ),
    15078: SanctionedItem(
        sdn_id=15078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15078", "LEI": "54930000015078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    15079: SanctionedItem(
        sdn_id=15079,
        name="Park Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15079"},
        aliases=["Sidorov, Park", "P. Sidorov"]
    ),
    15080: SanctionedItem(
        sdn_id=15080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15080", "LEI": "54930000015080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    15081: SanctionedItem(
        sdn_id=15081,
        name="Chen Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15081"},
        aliases=["Kuznetsov, Chen", "C. Kuznetsov"]
    ),
    15082: SanctionedItem(
        sdn_id=15082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15082", "LEI": "54930000015082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    15083: SanctionedItem(
        sdn_id=15083,
        name="Wang Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15083"},
        aliases=["Mousavi, Wang", "W. Mousavi"]
    ),
    15084: SanctionedItem(
        sdn_id=15084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15084", "LEI": "54930000015084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    15085: SanctionedItem(
        sdn_id=15085,
        name="Zhang Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15085"},
        aliases=["Khamenei, Zhang", "Z. Khamenei"]
    ),
    15086: SanctionedItem(
        sdn_id=15086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15086", "LEI": "54930000015086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    15087: SanctionedItem(
        sdn_id=15087,
        name="Carlos Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15087"},
        aliases=["Karimi, Carlos", "C. Karimi"]
    ),
    15088: SanctionedItem(
        sdn_id=15088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15088", "LEI": "54930000015088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    15089: SanctionedItem(
        sdn_id=15089,
        name="Raul Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15089"},
        aliases=["Myong-sik, Raul", "R. Myong-sik"]
    ),
    15090: SanctionedItem(
        sdn_id=15090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15090", "LEI": "54930000015090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    15091: SanctionedItem(
        sdn_id=15091,
        name="Ernesto Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15091"},
        aliases=["Bo, Ernesto", "E. Bo"]
    ),
    15092: SanctionedItem(
        sdn_id=15092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15092", "LEI": "54930000015092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    15093: SanctionedItem(
        sdn_id=15093,
        name="Ibrahim Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15093"},
        aliases=["Rodriguez, Ibrahim", "I. Rodriguez"]
    ),
    15094: SanctionedItem(
        sdn_id=15094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15094", "LEI": "54930000015094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    15095: SanctionedItem(
        sdn_id=15095,
        name="Tariq Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15095"},
        aliases=["Maduro, Tariq", "T. Maduro"]
    ),
    15096: SanctionedItem(
        sdn_id=15096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15096", "LEI": "54930000015096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    15097: SanctionedItem(
        sdn_id=15097,
        name="Nikolai Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15097"},
        aliases=["Al-Assad, Nikolai", "N. Al-Assad"]
    ),
    15098: SanctionedItem(
        sdn_id=15098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15098", "LEI": "54930000015098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    15099: SanctionedItem(
        sdn_id=15099,
        name="Vladimir Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15099"},
        aliases=["Sidorov, Vladimir", "V. Sidorov"]
    ),
    15100: SanctionedItem(
        sdn_id=15100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15100", "LEI": "54930000015100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    15101: SanctionedItem(
        sdn_id=15101,
        name="Andrei Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15101"},
        aliases=["Kuznetsov, Andrei", "A. Kuznetsov"]
    ),
    15102: SanctionedItem(
        sdn_id=15102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15102", "LEI": "54930000015102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    15103: SanctionedItem(
        sdn_id=15103,
        name="Mikhail Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15103"},
        aliases=["Mousavi, Mikhail", "M. Mousavi"]
    ),
    15104: SanctionedItem(
        sdn_id=15104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15104", "LEI": "54930000015104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    15105: SanctionedItem(
        sdn_id=15105,
        name="Reza Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15105"},
        aliases=["Khamenei, Reza", "R. Khamenei"]
    ),
    15106: SanctionedItem(
        sdn_id=15106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15106", "LEI": "54930000015106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    15107: SanctionedItem(
        sdn_id=15107,
        name="Farhad Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15107"},
        aliases=["Karimi, Farhad", "F. Karimi"]
    ),
    15108: SanctionedItem(
        sdn_id=15108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15108", "LEI": "54930000015108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    15109: SanctionedItem(
        sdn_id=15109,
        name="Mahmoud Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15109"},
        aliases=["Myong-sik, Mahmoud", "M. Myong-sik"]
    ),
    15110: SanctionedItem(
        sdn_id=15110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15110", "LEI": "54930000015110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    15111: SanctionedItem(
        sdn_id=15111,
        name="Slobodan Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15111"},
        aliases=["Bo, Slobodan", "S. Bo"]
    ),
    15112: SanctionedItem(
        sdn_id=15112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15112", "LEI": "54930000015112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    15113: SanctionedItem(
        sdn_id=15113,
        name="Radovan Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15113"},
        aliases=["Rodriguez, Radovan", "R. Rodriguez"]
    ),
    15114: SanctionedItem(
        sdn_id=15114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15114", "LEI": "54930000015114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    15115: SanctionedItem(
        sdn_id=15115,
        name="Goran Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15115"},
        aliases=["Maduro, Goran", "G. Maduro"]
    ),
    15116: SanctionedItem(
        sdn_id=15116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15116", "LEI": "54930000015116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    15117: SanctionedItem(
        sdn_id=15117,
        name="Milorad Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15117"},
        aliases=["Al-Assad, Milorad", "M. Al-Assad"]
    ),
    15118: SanctionedItem(
        sdn_id=15118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15118", "LEI": "54930000015118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    15119: SanctionedItem(
        sdn_id=15119,
        name="Jean-Pierre Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15119"},
        aliases=["Sidorov, Jean-Pierre", "J. Sidorov"]
    ),
    15120: SanctionedItem(
        sdn_id=15120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15120", "LEI": "54930000015120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    15121: SanctionedItem(
        sdn_id=15121,
        name="Viktor Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15121"},
        aliases=["Kuznetsov, Viktor", "V. Kuznetsov"]
    ),
    15122: SanctionedItem(
        sdn_id=15122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15122", "LEI": "54930000015122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    15123: SanctionedItem(
        sdn_id=15123,
        name="Dmitry Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15123"},
        aliases=["Mousavi, Dmitry", "D. Mousavi"]
    ),
    15124: SanctionedItem(
        sdn_id=15124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15124", "LEI": "54930000015124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    15125: SanctionedItem(
        sdn_id=15125,
        name="Sergei Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15125"},
        aliases=["Khamenei, Sergei", "S. Khamenei"]
    ),
    15126: SanctionedItem(
        sdn_id=15126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15126", "LEI": "54930000015126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    15127: SanctionedItem(
        sdn_id=15127,
        name="Alexander Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15127"},
        aliases=["Karimi, Alexander", "A. Karimi"]
    ),
    15128: SanctionedItem(
        sdn_id=15128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15128", "LEI": "54930000015128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    15129: SanctionedItem(
        sdn_id=15129,
        name="Mohammad Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15129"},
        aliases=["Myong-sik, Mohammad", "M. Myong-sik"]
    ),
    15130: SanctionedItem(
        sdn_id=15130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15130", "LEI": "54930000015130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    15131: SanctionedItem(
        sdn_id=15131,
        name="Hassan Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15131"},
        aliases=["Bo, Hassan", "H. Bo"]
    ),
    15132: SanctionedItem(
        sdn_id=15132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15132", "LEI": "54930000015132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    15133: SanctionedItem(
        sdn_id=15133,
        name="Ali Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15133"},
        aliases=["Rodriguez, Ali", "A. Rodriguez"]
    ),
    15134: SanctionedItem(
        sdn_id=15134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15134", "LEI": "54930000015134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    15135: SanctionedItem(
        sdn_id=15135,
        name="Ahmad Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15135"},
        aliases=["Maduro, Ahmad", "A. Maduro"]
    ),
    15136: SanctionedItem(
        sdn_id=15136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15136", "LEI": "54930000015136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    15137: SanctionedItem(
        sdn_id=15137,
        name="Kim Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15137"},
        aliases=["Al-Assad, Kim", "K. Al-Assad"]
    ),
    15138: SanctionedItem(
        sdn_id=15138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15138", "LEI": "54930000015138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    15139: SanctionedItem(
        sdn_id=15139,
        name="Park Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15139"},
        aliases=["Sidorov, Park", "P. Sidorov"]
    ),
    15140: SanctionedItem(
        sdn_id=15140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15140", "LEI": "54930000015140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    15141: SanctionedItem(
        sdn_id=15141,
        name="Chen Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15141"},
        aliases=["Kuznetsov, Chen", "C. Kuznetsov"]
    ),
    15142: SanctionedItem(
        sdn_id=15142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15142", "LEI": "54930000015142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    15143: SanctionedItem(
        sdn_id=15143,
        name="Wang Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15143"},
        aliases=["Mousavi, Wang", "W. Mousavi"]
    ),
    15144: SanctionedItem(
        sdn_id=15144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15144", "LEI": "54930000015144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    15145: SanctionedItem(
        sdn_id=15145,
        name="Zhang Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15145"},
        aliases=["Khamenei, Zhang", "Z. Khamenei"]
    ),
    15146: SanctionedItem(
        sdn_id=15146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15146", "LEI": "54930000015146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    15147: SanctionedItem(
        sdn_id=15147,
        name="Carlos Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15147"},
        aliases=["Karimi, Carlos", "C. Karimi"]
    ),
    15148: SanctionedItem(
        sdn_id=15148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15148", "LEI": "54930000015148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    15149: SanctionedItem(
        sdn_id=15149,
        name="Raul Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15149"},
        aliases=["Myong-sik, Raul", "R. Myong-sik"]
    ),
    15150: SanctionedItem(
        sdn_id=15150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15150", "LEI": "54930000015150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    15151: SanctionedItem(
        sdn_id=15151,
        name="Ernesto Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15151"},
        aliases=["Bo, Ernesto", "E. Bo"]
    ),
    15152: SanctionedItem(
        sdn_id=15152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15152", "LEI": "54930000015152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    15153: SanctionedItem(
        sdn_id=15153,
        name="Ibrahim Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15153"},
        aliases=["Rodriguez, Ibrahim", "I. Rodriguez"]
    ),
    15154: SanctionedItem(
        sdn_id=15154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15154", "LEI": "54930000015154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    15155: SanctionedItem(
        sdn_id=15155,
        name="Tariq Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15155"},
        aliases=["Maduro, Tariq", "T. Maduro"]
    ),
    15156: SanctionedItem(
        sdn_id=15156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15156", "LEI": "54930000015156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    15157: SanctionedItem(
        sdn_id=15157,
        name="Nikolai Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15157"},
        aliases=["Al-Assad, Nikolai", "N. Al-Assad"]
    ),
    15158: SanctionedItem(
        sdn_id=15158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15158", "LEI": "54930000015158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    15159: SanctionedItem(
        sdn_id=15159,
        name="Vladimir Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15159"},
        aliases=["Sidorov, Vladimir", "V. Sidorov"]
    ),
    15160: SanctionedItem(
        sdn_id=15160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15160", "LEI": "54930000015160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    15161: SanctionedItem(
        sdn_id=15161,
        name="Andrei Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15161"},
        aliases=["Kuznetsov, Andrei", "A. Kuznetsov"]
    ),
    15162: SanctionedItem(
        sdn_id=15162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15162", "LEI": "54930000015162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    15163: SanctionedItem(
        sdn_id=15163,
        name="Mikhail Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15163"},
        aliases=["Mousavi, Mikhail", "M. Mousavi"]
    ),
    15164: SanctionedItem(
        sdn_id=15164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15164", "LEI": "54930000015164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    15165: SanctionedItem(
        sdn_id=15165,
        name="Reza Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15165"},
        aliases=["Khamenei, Reza", "R. Khamenei"]
    ),
    15166: SanctionedItem(
        sdn_id=15166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15166", "LEI": "54930000015166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    15167: SanctionedItem(
        sdn_id=15167,
        name="Farhad Karimi",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15167"},
        aliases=["Karimi, Farhad", "F. Karimi"]
    ),
    15168: SanctionedItem(
        sdn_id=15168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15168", "LEI": "54930000015168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    15169: SanctionedItem(
        sdn_id=15169,
        name="Mahmoud Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15169"},
        aliases=["Myong-sik, Mahmoud", "M. Myong-sik"]
    ),
    15170: SanctionedItem(
        sdn_id=15170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15170", "LEI": "54930000015170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    15171: SanctionedItem(
        sdn_id=15171,
        name="Slobodan Bo",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15171"},
        aliases=["Bo, Slobodan", "S. Bo"]
    ),
    15172: SanctionedItem(
        sdn_id=15172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15172", "LEI": "54930000015172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    15173: SanctionedItem(
        sdn_id=15173,
        name="Radovan Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15173"},
        aliases=["Rodriguez, Radovan", "R. Rodriguez"]
    ),
    15174: SanctionedItem(
        sdn_id=15174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15174", "LEI": "54930000015174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    15175: SanctionedItem(
        sdn_id=15175,
        name="Goran Maduro",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15175"},
        aliases=["Maduro, Goran", "G. Maduro"]
    ),
    15176: SanctionedItem(
        sdn_id=15176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15176", "LEI": "54930000015176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    15177: SanctionedItem(
        sdn_id=15177,
        name="Milorad Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15177"},
        aliases=["Al-Assad, Milorad", "M. Al-Assad"]
    ),
    15178: SanctionedItem(
        sdn_id=15178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["MARITIME"],
        remarks="Designated entity under MARITIME enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-15178", "LEI": "54930000015178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    15179: SanctionedItem(
        sdn_id=15179,
        name="Jean-Pierre Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["MARITIME"],
        remarks="Designated individual under MARITIME; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-15179"},
        aliases=["Sidorov, Jean-Pierre", "J. Sidorov"]
    ),
}

"""
Middle East Regional & Nuclear Sanctions.
Iranian Transactions and Non-Proliferation Regulations.
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

RECORDS_MIDDLE_EAST_SANCTIONS: Dict[int, SanctionedItem] = {
    12000: SanctionedItem(
        sdn_id=12000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12000", "LEI": "54930000012000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    12001: SanctionedItem(
        sdn_id=12001,
        name="Viktor Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12001"},
        aliases=["Sidorov, Viktor", "V. Sidorov"]
    ),
    12002: SanctionedItem(
        sdn_id=12002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12002", "LEI": "54930000012002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    12003: SanctionedItem(
        sdn_id=12003,
        name="Dmitry Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12003"},
        aliases=["Kuznetsov, Dmitry", "D. Kuznetsov"]
    ),
    12004: SanctionedItem(
        sdn_id=12004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12004", "LEI": "54930000012004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    12005: SanctionedItem(
        sdn_id=12005,
        name="Sergei Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12005"},
        aliases=["Mousavi, Sergei", "S. Mousavi"]
    ),
    12006: SanctionedItem(
        sdn_id=12006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12006", "LEI": "54930000012006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    12007: SanctionedItem(
        sdn_id=12007,
        name="Alexander Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12007"},
        aliases=["Khamenei, Alexander", "A. Khamenei"]
    ),
    12008: SanctionedItem(
        sdn_id=12008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12008", "LEI": "54930000012008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    12009: SanctionedItem(
        sdn_id=12009,
        name="Mohammad Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12009"},
        aliases=["Karimi, Mohammad", "M. Karimi"]
    ),
    12010: SanctionedItem(
        sdn_id=12010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12010", "LEI": "54930000012010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    12011: SanctionedItem(
        sdn_id=12011,
        name="Hassan Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12011"},
        aliases=["Myong-sik, Hassan", "H. Myong-sik"]
    ),
    12012: SanctionedItem(
        sdn_id=12012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12012", "LEI": "54930000012012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    12013: SanctionedItem(
        sdn_id=12013,
        name="Ali Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12013"},
        aliases=["Bo, Ali", "A. Bo"]
    ),
    12014: SanctionedItem(
        sdn_id=12014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12014", "LEI": "54930000012014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    12015: SanctionedItem(
        sdn_id=12015,
        name="Ahmad Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12015"},
        aliases=["Rodriguez, Ahmad", "A. Rodriguez"]
    ),
    12016: SanctionedItem(
        sdn_id=12016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12016", "LEI": "54930000012016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    12017: SanctionedItem(
        sdn_id=12017,
        name="Kim Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12017"},
        aliases=["Maduro, Kim", "K. Maduro"]
    ),
    12018: SanctionedItem(
        sdn_id=12018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12018", "LEI": "54930000012018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    12019: SanctionedItem(
        sdn_id=12019,
        name="Park Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12019"},
        aliases=["Al-Assad, Park", "P. Al-Assad"]
    ),
    12020: SanctionedItem(
        sdn_id=12020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12020", "LEI": "54930000012020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    12021: SanctionedItem(
        sdn_id=12021,
        name="Chen Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12021"},
        aliases=["Sidorov, Chen", "C. Sidorov"]
    ),
    12022: SanctionedItem(
        sdn_id=12022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12022", "LEI": "54930000012022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    12023: SanctionedItem(
        sdn_id=12023,
        name="Wang Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12023"},
        aliases=["Kuznetsov, Wang", "W. Kuznetsov"]
    ),
    12024: SanctionedItem(
        sdn_id=12024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12024", "LEI": "54930000012024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    12025: SanctionedItem(
        sdn_id=12025,
        name="Zhang Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12025"},
        aliases=["Mousavi, Zhang", "Z. Mousavi"]
    ),
    12026: SanctionedItem(
        sdn_id=12026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12026", "LEI": "54930000012026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    12027: SanctionedItem(
        sdn_id=12027,
        name="Carlos Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12027"},
        aliases=["Khamenei, Carlos", "C. Khamenei"]
    ),
    12028: SanctionedItem(
        sdn_id=12028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12028", "LEI": "54930000012028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    12029: SanctionedItem(
        sdn_id=12029,
        name="Raul Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12029"},
        aliases=["Karimi, Raul", "R. Karimi"]
    ),
    12030: SanctionedItem(
        sdn_id=12030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12030", "LEI": "54930000012030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    12031: SanctionedItem(
        sdn_id=12031,
        name="Ernesto Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12031"},
        aliases=["Myong-sik, Ernesto", "E. Myong-sik"]
    ),
    12032: SanctionedItem(
        sdn_id=12032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12032", "LEI": "54930000012032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    12033: SanctionedItem(
        sdn_id=12033,
        name="Ibrahim Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12033"},
        aliases=["Bo, Ibrahim", "I. Bo"]
    ),
    12034: SanctionedItem(
        sdn_id=12034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12034", "LEI": "54930000012034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    12035: SanctionedItem(
        sdn_id=12035,
        name="Tariq Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12035"},
        aliases=["Rodriguez, Tariq", "T. Rodriguez"]
    ),
    12036: SanctionedItem(
        sdn_id=12036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12036", "LEI": "54930000012036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    12037: SanctionedItem(
        sdn_id=12037,
        name="Nikolai Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12037"},
        aliases=["Maduro, Nikolai", "N. Maduro"]
    ),
    12038: SanctionedItem(
        sdn_id=12038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12038", "LEI": "54930000012038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    12039: SanctionedItem(
        sdn_id=12039,
        name="Vladimir Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12039"},
        aliases=["Al-Assad, Vladimir", "V. Al-Assad"]
    ),
    12040: SanctionedItem(
        sdn_id=12040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12040", "LEI": "54930000012040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    12041: SanctionedItem(
        sdn_id=12041,
        name="Andrei Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12041"},
        aliases=["Sidorov, Andrei", "A. Sidorov"]
    ),
    12042: SanctionedItem(
        sdn_id=12042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12042", "LEI": "54930000012042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    12043: SanctionedItem(
        sdn_id=12043,
        name="Mikhail Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12043"},
        aliases=["Kuznetsov, Mikhail", "M. Kuznetsov"]
    ),
    12044: SanctionedItem(
        sdn_id=12044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12044", "LEI": "54930000012044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    12045: SanctionedItem(
        sdn_id=12045,
        name="Reza Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12045"},
        aliases=["Mousavi, Reza", "R. Mousavi"]
    ),
    12046: SanctionedItem(
        sdn_id=12046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12046", "LEI": "54930000012046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    12047: SanctionedItem(
        sdn_id=12047,
        name="Farhad Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12047"},
        aliases=["Khamenei, Farhad", "F. Khamenei"]
    ),
    12048: SanctionedItem(
        sdn_id=12048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12048", "LEI": "54930000012048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    12049: SanctionedItem(
        sdn_id=12049,
        name="Mahmoud Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12049"},
        aliases=["Karimi, Mahmoud", "M. Karimi"]
    ),
    12050: SanctionedItem(
        sdn_id=12050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12050", "LEI": "54930000012050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    12051: SanctionedItem(
        sdn_id=12051,
        name="Slobodan Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12051"},
        aliases=["Myong-sik, Slobodan", "S. Myong-sik"]
    ),
    12052: SanctionedItem(
        sdn_id=12052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12052", "LEI": "54930000012052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    12053: SanctionedItem(
        sdn_id=12053,
        name="Radovan Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12053"},
        aliases=["Bo, Radovan", "R. Bo"]
    ),
    12054: SanctionedItem(
        sdn_id=12054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12054", "LEI": "54930000012054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    12055: SanctionedItem(
        sdn_id=12055,
        name="Goran Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12055"},
        aliases=["Rodriguez, Goran", "G. Rodriguez"]
    ),
    12056: SanctionedItem(
        sdn_id=12056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12056", "LEI": "54930000012056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    12057: SanctionedItem(
        sdn_id=12057,
        name="Milorad Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12057"},
        aliases=["Maduro, Milorad", "M. Maduro"]
    ),
    12058: SanctionedItem(
        sdn_id=12058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12058", "LEI": "54930000012058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    12059: SanctionedItem(
        sdn_id=12059,
        name="Jean-Pierre Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12059"},
        aliases=["Al-Assad, Jean-Pierre", "J. Al-Assad"]
    ),
    12060: SanctionedItem(
        sdn_id=12060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12060", "LEI": "54930000012060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    12061: SanctionedItem(
        sdn_id=12061,
        name="Viktor Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12061"},
        aliases=["Sidorov, Viktor", "V. Sidorov"]
    ),
    12062: SanctionedItem(
        sdn_id=12062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12062", "LEI": "54930000012062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    12063: SanctionedItem(
        sdn_id=12063,
        name="Dmitry Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12063"},
        aliases=["Kuznetsov, Dmitry", "D. Kuznetsov"]
    ),
    12064: SanctionedItem(
        sdn_id=12064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12064", "LEI": "54930000012064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    12065: SanctionedItem(
        sdn_id=12065,
        name="Sergei Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12065"},
        aliases=["Mousavi, Sergei", "S. Mousavi"]
    ),
    12066: SanctionedItem(
        sdn_id=12066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12066", "LEI": "54930000012066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    12067: SanctionedItem(
        sdn_id=12067,
        name="Alexander Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12067"},
        aliases=["Khamenei, Alexander", "A. Khamenei"]
    ),
    12068: SanctionedItem(
        sdn_id=12068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12068", "LEI": "54930000012068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    12069: SanctionedItem(
        sdn_id=12069,
        name="Mohammad Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12069"},
        aliases=["Karimi, Mohammad", "M. Karimi"]
    ),
    12070: SanctionedItem(
        sdn_id=12070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12070", "LEI": "54930000012070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    12071: SanctionedItem(
        sdn_id=12071,
        name="Hassan Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12071"},
        aliases=["Myong-sik, Hassan", "H. Myong-sik"]
    ),
    12072: SanctionedItem(
        sdn_id=12072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12072", "LEI": "54930000012072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    12073: SanctionedItem(
        sdn_id=12073,
        name="Ali Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12073"},
        aliases=["Bo, Ali", "A. Bo"]
    ),
    12074: SanctionedItem(
        sdn_id=12074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12074", "LEI": "54930000012074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    12075: SanctionedItem(
        sdn_id=12075,
        name="Ahmad Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12075"},
        aliases=["Rodriguez, Ahmad", "A. Rodriguez"]
    ),
    12076: SanctionedItem(
        sdn_id=12076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12076", "LEI": "54930000012076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    12077: SanctionedItem(
        sdn_id=12077,
        name="Kim Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12077"},
        aliases=["Maduro, Kim", "K. Maduro"]
    ),
    12078: SanctionedItem(
        sdn_id=12078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12078", "LEI": "54930000012078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    12079: SanctionedItem(
        sdn_id=12079,
        name="Park Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12079"},
        aliases=["Al-Assad, Park", "P. Al-Assad"]
    ),
    12080: SanctionedItem(
        sdn_id=12080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12080", "LEI": "54930000012080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    12081: SanctionedItem(
        sdn_id=12081,
        name="Chen Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12081"},
        aliases=["Sidorov, Chen", "C. Sidorov"]
    ),
    12082: SanctionedItem(
        sdn_id=12082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12082", "LEI": "54930000012082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    12083: SanctionedItem(
        sdn_id=12083,
        name="Wang Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12083"},
        aliases=["Kuznetsov, Wang", "W. Kuznetsov"]
    ),
    12084: SanctionedItem(
        sdn_id=12084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12084", "LEI": "54930000012084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    12085: SanctionedItem(
        sdn_id=12085,
        name="Zhang Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12085"},
        aliases=["Mousavi, Zhang", "Z. Mousavi"]
    ),
    12086: SanctionedItem(
        sdn_id=12086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12086", "LEI": "54930000012086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    12087: SanctionedItem(
        sdn_id=12087,
        name="Carlos Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12087"},
        aliases=["Khamenei, Carlos", "C. Khamenei"]
    ),
    12088: SanctionedItem(
        sdn_id=12088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12088", "LEI": "54930000012088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    12089: SanctionedItem(
        sdn_id=12089,
        name="Raul Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12089"},
        aliases=["Karimi, Raul", "R. Karimi"]
    ),
    12090: SanctionedItem(
        sdn_id=12090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12090", "LEI": "54930000012090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    12091: SanctionedItem(
        sdn_id=12091,
        name="Ernesto Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12091"},
        aliases=["Myong-sik, Ernesto", "E. Myong-sik"]
    ),
    12092: SanctionedItem(
        sdn_id=12092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12092", "LEI": "54930000012092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    12093: SanctionedItem(
        sdn_id=12093,
        name="Ibrahim Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12093"},
        aliases=["Bo, Ibrahim", "I. Bo"]
    ),
    12094: SanctionedItem(
        sdn_id=12094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12094", "LEI": "54930000012094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    12095: SanctionedItem(
        sdn_id=12095,
        name="Tariq Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12095"},
        aliases=["Rodriguez, Tariq", "T. Rodriguez"]
    ),
    12096: SanctionedItem(
        sdn_id=12096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12096", "LEI": "54930000012096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    12097: SanctionedItem(
        sdn_id=12097,
        name="Nikolai Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12097"},
        aliases=["Maduro, Nikolai", "N. Maduro"]
    ),
    12098: SanctionedItem(
        sdn_id=12098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12098", "LEI": "54930000012098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    12099: SanctionedItem(
        sdn_id=12099,
        name="Vladimir Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12099"},
        aliases=["Al-Assad, Vladimir", "V. Al-Assad"]
    ),
    12100: SanctionedItem(
        sdn_id=12100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12100", "LEI": "54930000012100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    12101: SanctionedItem(
        sdn_id=12101,
        name="Andrei Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12101"},
        aliases=["Sidorov, Andrei", "A. Sidorov"]
    ),
    12102: SanctionedItem(
        sdn_id=12102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12102", "LEI": "54930000012102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    12103: SanctionedItem(
        sdn_id=12103,
        name="Mikhail Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12103"},
        aliases=["Kuznetsov, Mikhail", "M. Kuznetsov"]
    ),
    12104: SanctionedItem(
        sdn_id=12104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12104", "LEI": "54930000012104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    12105: SanctionedItem(
        sdn_id=12105,
        name="Reza Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12105"},
        aliases=["Mousavi, Reza", "R. Mousavi"]
    ),
    12106: SanctionedItem(
        sdn_id=12106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12106", "LEI": "54930000012106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    12107: SanctionedItem(
        sdn_id=12107,
        name="Farhad Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12107"},
        aliases=["Khamenei, Farhad", "F. Khamenei"]
    ),
    12108: SanctionedItem(
        sdn_id=12108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12108", "LEI": "54930000012108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    12109: SanctionedItem(
        sdn_id=12109,
        name="Mahmoud Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12109"},
        aliases=["Karimi, Mahmoud", "M. Karimi"]
    ),
    12110: SanctionedItem(
        sdn_id=12110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12110", "LEI": "54930000012110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    12111: SanctionedItem(
        sdn_id=12111,
        name="Slobodan Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12111"},
        aliases=["Myong-sik, Slobodan", "S. Myong-sik"]
    ),
    12112: SanctionedItem(
        sdn_id=12112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12112", "LEI": "54930000012112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    12113: SanctionedItem(
        sdn_id=12113,
        name="Radovan Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12113"},
        aliases=["Bo, Radovan", "R. Bo"]
    ),
    12114: SanctionedItem(
        sdn_id=12114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12114", "LEI": "54930000012114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    12115: SanctionedItem(
        sdn_id=12115,
        name="Goran Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12115"},
        aliases=["Rodriguez, Goran", "G. Rodriguez"]
    ),
    12116: SanctionedItem(
        sdn_id=12116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12116", "LEI": "54930000012116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    12117: SanctionedItem(
        sdn_id=12117,
        name="Milorad Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12117"},
        aliases=["Maduro, Milorad", "M. Maduro"]
    ),
    12118: SanctionedItem(
        sdn_id=12118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12118", "LEI": "54930000012118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    12119: SanctionedItem(
        sdn_id=12119,
        name="Jean-Pierre Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12119"},
        aliases=["Al-Assad, Jean-Pierre", "J. Al-Assad"]
    ),
    12120: SanctionedItem(
        sdn_id=12120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12120", "LEI": "54930000012120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    12121: SanctionedItem(
        sdn_id=12121,
        name="Viktor Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12121"},
        aliases=["Sidorov, Viktor", "V. Sidorov"]
    ),
    12122: SanctionedItem(
        sdn_id=12122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12122", "LEI": "54930000012122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    12123: SanctionedItem(
        sdn_id=12123,
        name="Dmitry Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12123"},
        aliases=["Kuznetsov, Dmitry", "D. Kuznetsov"]
    ),
    12124: SanctionedItem(
        sdn_id=12124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12124", "LEI": "54930000012124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    12125: SanctionedItem(
        sdn_id=12125,
        name="Sergei Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12125"},
        aliases=["Mousavi, Sergei", "S. Mousavi"]
    ),
    12126: SanctionedItem(
        sdn_id=12126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12126", "LEI": "54930000012126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    12127: SanctionedItem(
        sdn_id=12127,
        name="Alexander Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12127"},
        aliases=["Khamenei, Alexander", "A. Khamenei"]
    ),
    12128: SanctionedItem(
        sdn_id=12128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12128", "LEI": "54930000012128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    12129: SanctionedItem(
        sdn_id=12129,
        name="Mohammad Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12129"},
        aliases=["Karimi, Mohammad", "M. Karimi"]
    ),
    12130: SanctionedItem(
        sdn_id=12130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12130", "LEI": "54930000012130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    12131: SanctionedItem(
        sdn_id=12131,
        name="Hassan Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12131"},
        aliases=["Myong-sik, Hassan", "H. Myong-sik"]
    ),
    12132: SanctionedItem(
        sdn_id=12132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12132", "LEI": "54930000012132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    12133: SanctionedItem(
        sdn_id=12133,
        name="Ali Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12133"},
        aliases=["Bo, Ali", "A. Bo"]
    ),
    12134: SanctionedItem(
        sdn_id=12134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12134", "LEI": "54930000012134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    12135: SanctionedItem(
        sdn_id=12135,
        name="Ahmad Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12135"},
        aliases=["Rodriguez, Ahmad", "A. Rodriguez"]
    ),
    12136: SanctionedItem(
        sdn_id=12136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12136", "LEI": "54930000012136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    12137: SanctionedItem(
        sdn_id=12137,
        name="Kim Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12137"},
        aliases=["Maduro, Kim", "K. Maduro"]
    ),
    12138: SanctionedItem(
        sdn_id=12138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12138", "LEI": "54930000012138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    12139: SanctionedItem(
        sdn_id=12139,
        name="Park Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12139"},
        aliases=["Al-Assad, Park", "P. Al-Assad"]
    ),
    12140: SanctionedItem(
        sdn_id=12140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12140", "LEI": "54930000012140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    12141: SanctionedItem(
        sdn_id=12141,
        name="Chen Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12141"},
        aliases=["Sidorov, Chen", "C. Sidorov"]
    ),
    12142: SanctionedItem(
        sdn_id=12142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12142", "LEI": "54930000012142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    12143: SanctionedItem(
        sdn_id=12143,
        name="Wang Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12143"},
        aliases=["Kuznetsov, Wang", "W. Kuznetsov"]
    ),
    12144: SanctionedItem(
        sdn_id=12144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12144", "LEI": "54930000012144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    12145: SanctionedItem(
        sdn_id=12145,
        name="Zhang Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12145"},
        aliases=["Mousavi, Zhang", "Z. Mousavi"]
    ),
    12146: SanctionedItem(
        sdn_id=12146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12146", "LEI": "54930000012146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    12147: SanctionedItem(
        sdn_id=12147,
        name="Carlos Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12147"},
        aliases=["Khamenei, Carlos", "C. Khamenei"]
    ),
    12148: SanctionedItem(
        sdn_id=12148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12148", "LEI": "54930000012148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    12149: SanctionedItem(
        sdn_id=12149,
        name="Raul Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12149"},
        aliases=["Karimi, Raul", "R. Karimi"]
    ),
    12150: SanctionedItem(
        sdn_id=12150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12150", "LEI": "54930000012150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    12151: SanctionedItem(
        sdn_id=12151,
        name="Ernesto Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12151"},
        aliases=["Myong-sik, Ernesto", "E. Myong-sik"]
    ),
    12152: SanctionedItem(
        sdn_id=12152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12152", "LEI": "54930000012152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    12153: SanctionedItem(
        sdn_id=12153,
        name="Ibrahim Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12153"},
        aliases=["Bo, Ibrahim", "I. Bo"]
    ),
    12154: SanctionedItem(
        sdn_id=12154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12154", "LEI": "54930000012154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    12155: SanctionedItem(
        sdn_id=12155,
        name="Tariq Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12155"},
        aliases=["Rodriguez, Tariq", "T. Rodriguez"]
    ),
    12156: SanctionedItem(
        sdn_id=12156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12156", "LEI": "54930000012156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    12157: SanctionedItem(
        sdn_id=12157,
        name="Nikolai Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12157"},
        aliases=["Maduro, Nikolai", "N. Maduro"]
    ),
    12158: SanctionedItem(
        sdn_id=12158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12158", "LEI": "54930000012158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    12159: SanctionedItem(
        sdn_id=12159,
        name="Vladimir Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12159"},
        aliases=["Al-Assad, Vladimir", "V. Al-Assad"]
    ),
    12160: SanctionedItem(
        sdn_id=12160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12160", "LEI": "54930000012160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    12161: SanctionedItem(
        sdn_id=12161,
        name="Andrei Sidorov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12161"},
        aliases=["Sidorov, Andrei", "A. Sidorov"]
    ),
    12162: SanctionedItem(
        sdn_id=12162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12162", "LEI": "54930000012162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    12163: SanctionedItem(
        sdn_id=12163,
        name="Mikhail Kuznetsov",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12163"},
        aliases=["Kuznetsov, Mikhail", "M. Kuznetsov"]
    ),
    12164: SanctionedItem(
        sdn_id=12164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12164", "LEI": "54930000012164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    12165: SanctionedItem(
        sdn_id=12165,
        name="Reza Mousavi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12165"},
        aliases=["Mousavi, Reza", "R. Mousavi"]
    ),
    12166: SanctionedItem(
        sdn_id=12166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12166", "LEI": "54930000012166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    12167: SanctionedItem(
        sdn_id=12167,
        name="Farhad Khamenei",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12167"},
        aliases=["Khamenei, Farhad", "F. Khamenei"]
    ),
    12168: SanctionedItem(
        sdn_id=12168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12168", "LEI": "54930000012168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    12169: SanctionedItem(
        sdn_id=12169,
        name="Mahmoud Karimi",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12169"},
        aliases=["Karimi, Mahmoud", "M. Karimi"]
    ),
    12170: SanctionedItem(
        sdn_id=12170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12170", "LEI": "54930000012170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    12171: SanctionedItem(
        sdn_id=12171,
        name="Slobodan Myong-sik",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12171"},
        aliases=["Myong-sik, Slobodan", "S. Myong-sik"]
    ),
    12172: SanctionedItem(
        sdn_id=12172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12172", "LEI": "54930000012172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    12173: SanctionedItem(
        sdn_id=12173,
        name="Radovan Bo",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12173"},
        aliases=["Bo, Radovan", "R. Bo"]
    ),
    12174: SanctionedItem(
        sdn_id=12174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12174", "LEI": "54930000012174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    12175: SanctionedItem(
        sdn_id=12175,
        name="Goran Rodriguez",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12175"},
        aliases=["Rodriguez, Goran", "G. Rodriguez"]
    ),
    12176: SanctionedItem(
        sdn_id=12176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12176", "LEI": "54930000012176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    12177: SanctionedItem(
        sdn_id=12177,
        name="Milorad Maduro",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12177"},
        aliases=["Maduro, Milorad", "M. Maduro"]
    ),
    12178: SanctionedItem(
        sdn_id=12178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["IRAN"],
        remarks="Designated entity under IRAN enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-12178", "LEI": "54930000012178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    12179: SanctionedItem(
        sdn_id=12179,
        name="Jean-Pierre Al-Assad",
        sdn_type="INDIVIDUAL",
        programs=["IRAN"],
        remarks="Designated individual under IRAN; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-12179"},
        aliases=["Al-Assad, Jean-Pierre", "J. Al-Assad"]
    ),
}

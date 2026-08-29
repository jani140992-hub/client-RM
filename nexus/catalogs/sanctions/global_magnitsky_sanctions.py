"""
Global Magnitsky Anti-Corruption Sanctions.
Global Magnitsky Human Rights Accountability.
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

RECORDS_GLOBAL_MAGNITSKY_SANCTIONS: Dict[int, SanctionedItem] = {
    17000: SanctionedItem(
        sdn_id=17000,
        name="Ros Prom Enterprises 1",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17000", "LEI": "54930000017000001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 1"]
    ),
    17001: SanctionedItem(
        sdn_id=17001,
        name="Viktor Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17001"},
        aliases=["Sokolov, Viktor", "V. Sokolov"]
    ),
    17002: SanctionedItem(
        sdn_id=17002,
        name="PJSC Finance Consortium 3",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17002", "LEI": "54930000017002001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 3"]
    ),
    17003: SanctionedItem(
        sdn_id=17003,
        name="Dmitry Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17003"},
        aliases=["Soleimani, Dmitry", "D. Soleimani"]
    ),
    17004: SanctionedItem(
        sdn_id=17004,
        name="OJSC Energy S.A. 5",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17004", "LEI": "54930000017004001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 5"]
    ),
    17005: SanctionedItem(
        sdn_id=17005,
        name="Sergei Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17005"},
        aliases=["Najafi, Sergei", "S. Najafi"]
    ),
    17006: SanctionedItem(
        sdn_id=17006,
        name="Al- Telecom Corporation 7",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17006", "LEI": "54930000017006001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 7"]
    ),
    17007: SanctionedItem(
        sdn_id=17007,
        name="Alexander Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17007"},
        aliases=["Il-sung, Alexander", "A. Il-sung"]
    ),
    17008: SanctionedItem(
        sdn_id=17008,
        name="Mahan Flot Services DMCC 9",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17008", "LEI": "54930000017008001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 9"]
    ),
    17009: SanctionedItem(
        sdn_id=17009,
        name="Mohammad Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17009"},
        aliases=["Wei, Mohammad", "M. Wei"]
    ),
    17010: SanctionedItem(
        sdn_id=17010,
        name="Koryo Maritime Holdings Inc 11",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17010", "LEI": "54930000017010001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 11"]
    ),
    17011: SanctionedItem(
        sdn_id=17011,
        name="Hassan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17011"},
        aliases=["Qiang, Hassan", "H. Qiang"]
    ),
    17012: SanctionedItem(
        sdn_id=17012,
        name="Orion Optics Group 13",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17012", "LEI": "54930000017012001"},
        aliases=["Optics Group", "Group Orion Optics Group 13"]
    ),
    17013: SanctionedItem(
        sdn_id=17013,
        name="Ali Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17013"},
        aliases=["Cabello, Ali", "A. Cabello"]
    ),
    17014: SanctionedItem(
        sdn_id=17014,
        name="Volga Tech Enterprises 15",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17014", "LEI": "54930000017014001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 15"]
    ),
    17015: SanctionedItem(
        sdn_id=17015,
        name="Ahmad Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17015"},
        aliases=["Lopez, Ahmad", "A. Lopez"]
    ),
    17016: SanctionedItem(
        sdn_id=17016,
        name="Caspian Resource Consortium 17",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17016", "LEI": "54930000017016001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 17"]
    ),
    17017: SanctionedItem(
        sdn_id=17017,
        name="Kim Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17017"},
        aliases=["Ivanov, Kim", "K. Ivanov"]
    ),
    17018: SanctionedItem(
        sdn_id=17018,
        name="Pacific Metals S.A. 19",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17018", "LEI": "54930000017018001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 19"]
    ),
    17019: SanctionedItem(
        sdn_id=17019,
        name="Park Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17019"},
        aliases=["Smirnov, Park", "P. Smirnov"]
    ),
    17020: SanctionedItem(
        sdn_id=17020,
        name="Ros Prom Corporation 21",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17020", "LEI": "54930000017020001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 21"]
    ),
    17021: SanctionedItem(
        sdn_id=17021,
        name="Chen Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17021"},
        aliases=["Sokolov, Chen", "C. Sokolov"]
    ),
    17022: SanctionedItem(
        sdn_id=17022,
        name="PJSC Finance Services DMCC 23",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17022", "LEI": "54930000017022001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 23"]
    ),
    17023: SanctionedItem(
        sdn_id=17023,
        name="Wang Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17023"},
        aliases=["Soleimani, Wang", "W. Soleimani"]
    ),
    17024: SanctionedItem(
        sdn_id=17024,
        name="OJSC Energy Holdings Inc 25",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17024", "LEI": "54930000017024001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 25"]
    ),
    17025: SanctionedItem(
        sdn_id=17025,
        name="Zhang Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17025"},
        aliases=["Najafi, Zhang", "Z. Najafi"]
    ),
    17026: SanctionedItem(
        sdn_id=17026,
        name="Al- Telecom Group 27",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17026", "LEI": "54930000017026001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 27"]
    ),
    17027: SanctionedItem(
        sdn_id=17027,
        name="Carlos Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17027"},
        aliases=["Il-sung, Carlos", "C. Il-sung"]
    ),
    17028: SanctionedItem(
        sdn_id=17028,
        name="Mahan Flot Enterprises 29",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17028", "LEI": "54930000017028001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 29"]
    ),
    17029: SanctionedItem(
        sdn_id=17029,
        name="Raul Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17029"},
        aliases=["Wei, Raul", "R. Wei"]
    ),
    17030: SanctionedItem(
        sdn_id=17030,
        name="Koryo Maritime Consortium 31",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17030", "LEI": "54930000017030001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 31"]
    ),
    17031: SanctionedItem(
        sdn_id=17031,
        name="Ernesto Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17031"},
        aliases=["Qiang, Ernesto", "E. Qiang"]
    ),
    17032: SanctionedItem(
        sdn_id=17032,
        name="Orion Optics S.A. 33",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17032", "LEI": "54930000017032001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 33"]
    ),
    17033: SanctionedItem(
        sdn_id=17033,
        name="Ibrahim Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17033"},
        aliases=["Cabello, Ibrahim", "I. Cabello"]
    ),
    17034: SanctionedItem(
        sdn_id=17034,
        name="Volga Tech Corporation 35",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17034", "LEI": "54930000017034001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 35"]
    ),
    17035: SanctionedItem(
        sdn_id=17035,
        name="Tariq Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17035"},
        aliases=["Lopez, Tariq", "T. Lopez"]
    ),
    17036: SanctionedItem(
        sdn_id=17036,
        name="Caspian Resource Services DMCC 37",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17036", "LEI": "54930000017036001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 37"]
    ),
    17037: SanctionedItem(
        sdn_id=17037,
        name="Nikolai Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17037"},
        aliases=["Ivanov, Nikolai", "N. Ivanov"]
    ),
    17038: SanctionedItem(
        sdn_id=17038,
        name="Pacific Metals Holdings Inc 39",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17038", "LEI": "54930000017038001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 39"]
    ),
    17039: SanctionedItem(
        sdn_id=17039,
        name="Vladimir Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17039"},
        aliases=["Smirnov, Vladimir", "V. Smirnov"]
    ),
    17040: SanctionedItem(
        sdn_id=17040,
        name="Ros Prom Group 41",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17040", "LEI": "54930000017040001"},
        aliases=["Prom Group", "Group Ros Prom Group 41"]
    ),
    17041: SanctionedItem(
        sdn_id=17041,
        name="Andrei Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17041"},
        aliases=["Sokolov, Andrei", "A. Sokolov"]
    ),
    17042: SanctionedItem(
        sdn_id=17042,
        name="PJSC Finance Enterprises 43",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17042", "LEI": "54930000017042001"},
        aliases=["Finance Enterprises", "Group PJSC Finance Enterprises 43"]
    ),
    17043: SanctionedItem(
        sdn_id=17043,
        name="Mikhail Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17043"},
        aliases=["Soleimani, Mikhail", "M. Soleimani"]
    ),
    17044: SanctionedItem(
        sdn_id=17044,
        name="OJSC Energy Consortium 45",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17044", "LEI": "54930000017044001"},
        aliases=["Energy Consortium", "Group OJSC Energy Consortium 45"]
    ),
    17045: SanctionedItem(
        sdn_id=17045,
        name="Reza Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17045"},
        aliases=["Najafi, Reza", "R. Najafi"]
    ),
    17046: SanctionedItem(
        sdn_id=17046,
        name="Al- Telecom S.A. 47",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17046", "LEI": "54930000017046001"},
        aliases=["Telecom S.A.", "Group Al- Telecom S.A. 47"]
    ),
    17047: SanctionedItem(
        sdn_id=17047,
        name="Farhad Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17047"},
        aliases=["Il-sung, Farhad", "F. Il-sung"]
    ),
    17048: SanctionedItem(
        sdn_id=17048,
        name="Mahan Flot Corporation 49",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17048", "LEI": "54930000017048001"},
        aliases=["Flot Corporation", "Group Mahan Flot Corporation 49"]
    ),
    17049: SanctionedItem(
        sdn_id=17049,
        name="Mahmoud Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17049"},
        aliases=["Wei, Mahmoud", "M. Wei"]
    ),
    17050: SanctionedItem(
        sdn_id=17050,
        name="Koryo Maritime Services DMCC 51",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17050", "LEI": "54930000017050001"},
        aliases=["Maritime Services DMCC", "Group Koryo Maritime Services DMCC 51"]
    ),
    17051: SanctionedItem(
        sdn_id=17051,
        name="Slobodan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17051"},
        aliases=["Qiang, Slobodan", "S. Qiang"]
    ),
    17052: SanctionedItem(
        sdn_id=17052,
        name="Orion Optics Holdings Inc 53",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17052", "LEI": "54930000017052001"},
        aliases=["Optics Holdings Inc", "Group Orion Optics Holdings Inc 53"]
    ),
    17053: SanctionedItem(
        sdn_id=17053,
        name="Radovan Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17053"},
        aliases=["Cabello, Radovan", "R. Cabello"]
    ),
    17054: SanctionedItem(
        sdn_id=17054,
        name="Volga Tech Group 55",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17054", "LEI": "54930000017054001"},
        aliases=["Tech Group", "Group Volga Tech Group 55"]
    ),
    17055: SanctionedItem(
        sdn_id=17055,
        name="Goran Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17055"},
        aliases=["Lopez, Goran", "G. Lopez"]
    ),
    17056: SanctionedItem(
        sdn_id=17056,
        name="Caspian Resource Enterprises 57",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17056", "LEI": "54930000017056001"},
        aliases=["Resource Enterprises", "Group Caspian Resource Enterprises 57"]
    ),
    17057: SanctionedItem(
        sdn_id=17057,
        name="Milorad Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17057"},
        aliases=["Ivanov, Milorad", "M. Ivanov"]
    ),
    17058: SanctionedItem(
        sdn_id=17058,
        name="Pacific Metals Consortium 59",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17058", "LEI": "54930000017058001"},
        aliases=["Metals Consortium", "Group Pacific Metals Consortium 59"]
    ),
    17059: SanctionedItem(
        sdn_id=17059,
        name="Jean-Pierre Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17059"},
        aliases=["Smirnov, Jean-Pierre", "J. Smirnov"]
    ),
    17060: SanctionedItem(
        sdn_id=17060,
        name="Ros Prom S.A. 61",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17060", "LEI": "54930000017060001"},
        aliases=["Prom S.A.", "Group Ros Prom S.A. 61"]
    ),
    17061: SanctionedItem(
        sdn_id=17061,
        name="Viktor Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17061"},
        aliases=["Sokolov, Viktor", "V. Sokolov"]
    ),
    17062: SanctionedItem(
        sdn_id=17062,
        name="PJSC Finance Corporation 63",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17062", "LEI": "54930000017062001"},
        aliases=["Finance Corporation", "Group PJSC Finance Corporation 63"]
    ),
    17063: SanctionedItem(
        sdn_id=17063,
        name="Dmitry Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17063"},
        aliases=["Soleimani, Dmitry", "D. Soleimani"]
    ),
    17064: SanctionedItem(
        sdn_id=17064,
        name="OJSC Energy Services DMCC 65",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17064", "LEI": "54930000017064001"},
        aliases=["Energy Services DMCC", "Group OJSC Energy Services DMCC 65"]
    ),
    17065: SanctionedItem(
        sdn_id=17065,
        name="Sergei Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17065"},
        aliases=["Najafi, Sergei", "S. Najafi"]
    ),
    17066: SanctionedItem(
        sdn_id=17066,
        name="Al- Telecom Holdings Inc 67",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17066", "LEI": "54930000017066001"},
        aliases=["Telecom Holdings Inc", "Group Al- Telecom Holdings Inc 67"]
    ),
    17067: SanctionedItem(
        sdn_id=17067,
        name="Alexander Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17067"},
        aliases=["Il-sung, Alexander", "A. Il-sung"]
    ),
    17068: SanctionedItem(
        sdn_id=17068,
        name="Mahan Flot Group 69",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17068", "LEI": "54930000017068001"},
        aliases=["Flot Group", "Group Mahan Flot Group 69"]
    ),
    17069: SanctionedItem(
        sdn_id=17069,
        name="Mohammad Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17069"},
        aliases=["Wei, Mohammad", "M. Wei"]
    ),
    17070: SanctionedItem(
        sdn_id=17070,
        name="Koryo Maritime Enterprises 71",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17070", "LEI": "54930000017070001"},
        aliases=["Maritime Enterprises", "Group Koryo Maritime Enterprises 71"]
    ),
    17071: SanctionedItem(
        sdn_id=17071,
        name="Hassan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17071"},
        aliases=["Qiang, Hassan", "H. Qiang"]
    ),
    17072: SanctionedItem(
        sdn_id=17072,
        name="Orion Optics Consortium 73",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17072", "LEI": "54930000017072001"},
        aliases=["Optics Consortium", "Group Orion Optics Consortium 73"]
    ),
    17073: SanctionedItem(
        sdn_id=17073,
        name="Ali Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17073"},
        aliases=["Cabello, Ali", "A. Cabello"]
    ),
    17074: SanctionedItem(
        sdn_id=17074,
        name="Volga Tech S.A. 75",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17074", "LEI": "54930000017074001"},
        aliases=["Tech S.A.", "Group Volga Tech S.A. 75"]
    ),
    17075: SanctionedItem(
        sdn_id=17075,
        name="Ahmad Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17075"},
        aliases=["Lopez, Ahmad", "A. Lopez"]
    ),
    17076: SanctionedItem(
        sdn_id=17076,
        name="Caspian Resource Corporation 77",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17076", "LEI": "54930000017076001"},
        aliases=["Resource Corporation", "Group Caspian Resource Corporation 77"]
    ),
    17077: SanctionedItem(
        sdn_id=17077,
        name="Kim Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17077"},
        aliases=["Ivanov, Kim", "K. Ivanov"]
    ),
    17078: SanctionedItem(
        sdn_id=17078,
        name="Pacific Metals Services DMCC 79",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17078", "LEI": "54930000017078001"},
        aliases=["Metals Services DMCC", "Group Pacific Metals Services DMCC 79"]
    ),
    17079: SanctionedItem(
        sdn_id=17079,
        name="Park Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17079"},
        aliases=["Smirnov, Park", "P. Smirnov"]
    ),
    17080: SanctionedItem(
        sdn_id=17080,
        name="Ros Prom Holdings Inc 81",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17080", "LEI": "54930000017080001"},
        aliases=["Prom Holdings Inc", "Group Ros Prom Holdings Inc 81"]
    ),
    17081: SanctionedItem(
        sdn_id=17081,
        name="Chen Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17081"},
        aliases=["Sokolov, Chen", "C. Sokolov"]
    ),
    17082: SanctionedItem(
        sdn_id=17082,
        name="PJSC Finance Group 83",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17082", "LEI": "54930000017082001"},
        aliases=["Finance Group", "Group PJSC Finance Group 83"]
    ),
    17083: SanctionedItem(
        sdn_id=17083,
        name="Wang Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17083"},
        aliases=["Soleimani, Wang", "W. Soleimani"]
    ),
    17084: SanctionedItem(
        sdn_id=17084,
        name="OJSC Energy Enterprises 85",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17084", "LEI": "54930000017084001"},
        aliases=["Energy Enterprises", "Group OJSC Energy Enterprises 85"]
    ),
    17085: SanctionedItem(
        sdn_id=17085,
        name="Zhang Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17085"},
        aliases=["Najafi, Zhang", "Z. Najafi"]
    ),
    17086: SanctionedItem(
        sdn_id=17086,
        name="Al- Telecom Consortium 87",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17086", "LEI": "54930000017086001"},
        aliases=["Telecom Consortium", "Group Al- Telecom Consortium 87"]
    ),
    17087: SanctionedItem(
        sdn_id=17087,
        name="Carlos Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17087"},
        aliases=["Il-sung, Carlos", "C. Il-sung"]
    ),
    17088: SanctionedItem(
        sdn_id=17088,
        name="Mahan Flot S.A. 89",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17088", "LEI": "54930000017088001"},
        aliases=["Flot S.A.", "Group Mahan Flot S.A. 89"]
    ),
    17089: SanctionedItem(
        sdn_id=17089,
        name="Raul Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17089"},
        aliases=["Wei, Raul", "R. Wei"]
    ),
    17090: SanctionedItem(
        sdn_id=17090,
        name="Koryo Maritime Corporation 91",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17090", "LEI": "54930000017090001"},
        aliases=["Maritime Corporation", "Group Koryo Maritime Corporation 91"]
    ),
    17091: SanctionedItem(
        sdn_id=17091,
        name="Ernesto Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17091"},
        aliases=["Qiang, Ernesto", "E. Qiang"]
    ),
    17092: SanctionedItem(
        sdn_id=17092,
        name="Orion Optics Services DMCC 93",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17092", "LEI": "54930000017092001"},
        aliases=["Optics Services DMCC", "Group Orion Optics Services DMCC 93"]
    ),
    17093: SanctionedItem(
        sdn_id=17093,
        name="Ibrahim Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17093"},
        aliases=["Cabello, Ibrahim", "I. Cabello"]
    ),
    17094: SanctionedItem(
        sdn_id=17094,
        name="Volga Tech Holdings Inc 95",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17094", "LEI": "54930000017094001"},
        aliases=["Tech Holdings Inc", "Group Volga Tech Holdings Inc 95"]
    ),
    17095: SanctionedItem(
        sdn_id=17095,
        name="Tariq Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17095"},
        aliases=["Lopez, Tariq", "T. Lopez"]
    ),
    17096: SanctionedItem(
        sdn_id=17096,
        name="Caspian Resource Group 97",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17096", "LEI": "54930000017096001"},
        aliases=["Resource Group", "Group Caspian Resource Group 97"]
    ),
    17097: SanctionedItem(
        sdn_id=17097,
        name="Nikolai Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17097"},
        aliases=["Ivanov, Nikolai", "N. Ivanov"]
    ),
    17098: SanctionedItem(
        sdn_id=17098,
        name="Pacific Metals Enterprises 99",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17098", "LEI": "54930000017098001"},
        aliases=["Metals Enterprises", "Group Pacific Metals Enterprises 99"]
    ),
    17099: SanctionedItem(
        sdn_id=17099,
        name="Vladimir Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17099"},
        aliases=["Smirnov, Vladimir", "V. Smirnov"]
    ),
    17100: SanctionedItem(
        sdn_id=17100,
        name="Ros Prom Consortium 101",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17100", "LEI": "54930000017100001"},
        aliases=["Prom Consortium", "Group Ros Prom Consortium 101"]
    ),
    17101: SanctionedItem(
        sdn_id=17101,
        name="Andrei Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17101"},
        aliases=["Sokolov, Andrei", "A. Sokolov"]
    ),
    17102: SanctionedItem(
        sdn_id=17102,
        name="PJSC Finance S.A. 103",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17102", "LEI": "54930000017102001"},
        aliases=["Finance S.A.", "Group PJSC Finance S.A. 103"]
    ),
    17103: SanctionedItem(
        sdn_id=17103,
        name="Mikhail Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17103"},
        aliases=["Soleimani, Mikhail", "M. Soleimani"]
    ),
    17104: SanctionedItem(
        sdn_id=17104,
        name="OJSC Energy Corporation 105",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17104", "LEI": "54930000017104001"},
        aliases=["Energy Corporation", "Group OJSC Energy Corporation 105"]
    ),
    17105: SanctionedItem(
        sdn_id=17105,
        name="Reza Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17105"},
        aliases=["Najafi, Reza", "R. Najafi"]
    ),
    17106: SanctionedItem(
        sdn_id=17106,
        name="Al- Telecom Services DMCC 107",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17106", "LEI": "54930000017106001"},
        aliases=["Telecom Services DMCC", "Group Al- Telecom Services DMCC 107"]
    ),
    17107: SanctionedItem(
        sdn_id=17107,
        name="Farhad Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17107"},
        aliases=["Il-sung, Farhad", "F. Il-sung"]
    ),
    17108: SanctionedItem(
        sdn_id=17108,
        name="Mahan Flot Holdings Inc 109",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17108", "LEI": "54930000017108001"},
        aliases=["Flot Holdings Inc", "Group Mahan Flot Holdings Inc 109"]
    ),
    17109: SanctionedItem(
        sdn_id=17109,
        name="Mahmoud Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17109"},
        aliases=["Wei, Mahmoud", "M. Wei"]
    ),
    17110: SanctionedItem(
        sdn_id=17110,
        name="Koryo Maritime Group 111",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17110", "LEI": "54930000017110001"},
        aliases=["Maritime Group", "Group Koryo Maritime Group 111"]
    ),
    17111: SanctionedItem(
        sdn_id=17111,
        name="Slobodan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17111"},
        aliases=["Qiang, Slobodan", "S. Qiang"]
    ),
    17112: SanctionedItem(
        sdn_id=17112,
        name="Orion Optics Enterprises 113",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17112", "LEI": "54930000017112001"},
        aliases=["Optics Enterprises", "Group Orion Optics Enterprises 113"]
    ),
    17113: SanctionedItem(
        sdn_id=17113,
        name="Radovan Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17113"},
        aliases=["Cabello, Radovan", "R. Cabello"]
    ),
    17114: SanctionedItem(
        sdn_id=17114,
        name="Volga Tech Consortium 115",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17114", "LEI": "54930000017114001"},
        aliases=["Tech Consortium", "Group Volga Tech Consortium 115"]
    ),
    17115: SanctionedItem(
        sdn_id=17115,
        name="Goran Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17115"},
        aliases=["Lopez, Goran", "G. Lopez"]
    ),
    17116: SanctionedItem(
        sdn_id=17116,
        name="Caspian Resource S.A. 117",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17116", "LEI": "54930000017116001"},
        aliases=["Resource S.A.", "Group Caspian Resource S.A. 117"]
    ),
    17117: SanctionedItem(
        sdn_id=17117,
        name="Milorad Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17117"},
        aliases=["Ivanov, Milorad", "M. Ivanov"]
    ),
    17118: SanctionedItem(
        sdn_id=17118,
        name="Pacific Metals Corporation 119",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17118", "LEI": "54930000017118001"},
        aliases=["Metals Corporation", "Group Pacific Metals Corporation 119"]
    ),
    17119: SanctionedItem(
        sdn_id=17119,
        name="Jean-Pierre Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17119"},
        aliases=["Smirnov, Jean-Pierre", "J. Smirnov"]
    ),
    17120: SanctionedItem(
        sdn_id=17120,
        name="Ros Prom Services DMCC 121",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17120", "LEI": "54930000017120001"},
        aliases=["Prom Services DMCC", "Group Ros Prom Services DMCC 121"]
    ),
    17121: SanctionedItem(
        sdn_id=17121,
        name="Viktor Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17121"},
        aliases=["Sokolov, Viktor", "V. Sokolov"]
    ),
    17122: SanctionedItem(
        sdn_id=17122,
        name="PJSC Finance Holdings Inc 123",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17122", "LEI": "54930000017122001"},
        aliases=["Finance Holdings Inc", "Group PJSC Finance Holdings Inc 123"]
    ),
    17123: SanctionedItem(
        sdn_id=17123,
        name="Dmitry Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17123"},
        aliases=["Soleimani, Dmitry", "D. Soleimani"]
    ),
    17124: SanctionedItem(
        sdn_id=17124,
        name="OJSC Energy Group 125",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17124", "LEI": "54930000017124001"},
        aliases=["Energy Group", "Group OJSC Energy Group 125"]
    ),
    17125: SanctionedItem(
        sdn_id=17125,
        name="Sergei Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17125"},
        aliases=["Najafi, Sergei", "S. Najafi"]
    ),
    17126: SanctionedItem(
        sdn_id=17126,
        name="Al- Telecom Enterprises 127",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17126", "LEI": "54930000017126001"},
        aliases=["Telecom Enterprises", "Group Al- Telecom Enterprises 127"]
    ),
    17127: SanctionedItem(
        sdn_id=17127,
        name="Alexander Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17127"},
        aliases=["Il-sung, Alexander", "A. Il-sung"]
    ),
    17128: SanctionedItem(
        sdn_id=17128,
        name="Mahan Flot Consortium 129",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17128", "LEI": "54930000017128001"},
        aliases=["Flot Consortium", "Group Mahan Flot Consortium 129"]
    ),
    17129: SanctionedItem(
        sdn_id=17129,
        name="Mohammad Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17129"},
        aliases=["Wei, Mohammad", "M. Wei"]
    ),
    17130: SanctionedItem(
        sdn_id=17130,
        name="Koryo Maritime S.A. 131",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17130", "LEI": "54930000017130001"},
        aliases=["Maritime S.A.", "Group Koryo Maritime S.A. 131"]
    ),
    17131: SanctionedItem(
        sdn_id=17131,
        name="Hassan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17131"},
        aliases=["Qiang, Hassan", "H. Qiang"]
    ),
    17132: SanctionedItem(
        sdn_id=17132,
        name="Orion Optics Corporation 133",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17132", "LEI": "54930000017132001"},
        aliases=["Optics Corporation", "Group Orion Optics Corporation 133"]
    ),
    17133: SanctionedItem(
        sdn_id=17133,
        name="Ali Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17133"},
        aliases=["Cabello, Ali", "A. Cabello"]
    ),
    17134: SanctionedItem(
        sdn_id=17134,
        name="Volga Tech Services DMCC 135",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17134", "LEI": "54930000017134001"},
        aliases=["Tech Services DMCC", "Group Volga Tech Services DMCC 135"]
    ),
    17135: SanctionedItem(
        sdn_id=17135,
        name="Ahmad Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17135"},
        aliases=["Lopez, Ahmad", "A. Lopez"]
    ),
    17136: SanctionedItem(
        sdn_id=17136,
        name="Caspian Resource Holdings Inc 137",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17136", "LEI": "54930000017136001"},
        aliases=["Resource Holdings Inc", "Group Caspian Resource Holdings Inc 137"]
    ),
    17137: SanctionedItem(
        sdn_id=17137,
        name="Kim Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17137"},
        aliases=["Ivanov, Kim", "K. Ivanov"]
    ),
    17138: SanctionedItem(
        sdn_id=17138,
        name="Pacific Metals Group 139",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17138", "LEI": "54930000017138001"},
        aliases=["Metals Group", "Group Pacific Metals Group 139"]
    ),
    17139: SanctionedItem(
        sdn_id=17139,
        name="Park Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17139"},
        aliases=["Smirnov, Park", "P. Smirnov"]
    ),
    17140: SanctionedItem(
        sdn_id=17140,
        name="Ros Prom Enterprises 141",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17140", "LEI": "54930000017140001"},
        aliases=["Prom Enterprises", "Group Ros Prom Enterprises 141"]
    ),
    17141: SanctionedItem(
        sdn_id=17141,
        name="Chen Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1976-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17141"},
        aliases=["Sokolov, Chen", "C. Sokolov"]
    ),
    17142: SanctionedItem(
        sdn_id=17142,
        name="PJSC Finance Consortium 143",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17142", "LEI": "54930000017142001"},
        aliases=["Finance Consortium", "Group PJSC Finance Consortium 143"]
    ),
    17143: SanctionedItem(
        sdn_id=17143,
        name="Wang Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1978-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17143"},
        aliases=["Soleimani, Wang", "W. Soleimani"]
    ),
    17144: SanctionedItem(
        sdn_id=17144,
        name="OJSC Energy S.A. 145",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17144", "LEI": "54930000017144001"},
        aliases=["Energy S.A.", "Group OJSC Energy S.A. 145"]
    ),
    17145: SanctionedItem(
        sdn_id=17145,
        name="Zhang Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1980-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17145"},
        aliases=["Najafi, Zhang", "Z. Najafi"]
    ),
    17146: SanctionedItem(
        sdn_id=17146,
        name="Al- Telecom Corporation 147",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17146", "LEI": "54930000017146001"},
        aliases=["Telecom Corporation", "Group Al- Telecom Corporation 147"]
    ),
    17147: SanctionedItem(
        sdn_id=17147,
        name="Carlos Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1982-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17147"},
        aliases=["Il-sung, Carlos", "C. Il-sung"]
    ),
    17148: SanctionedItem(
        sdn_id=17148,
        name="Mahan Flot Services DMCC 149",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17148", "LEI": "54930000017148001"},
        aliases=["Flot Services DMCC", "Group Mahan Flot Services DMCC 149"]
    ),
    17149: SanctionedItem(
        sdn_id=17149,
        name="Raul Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1984-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17149"},
        aliases=["Wei, Raul", "R. Wei"]
    ),
    17150: SanctionedItem(
        sdn_id=17150,
        name="Koryo Maritime Holdings Inc 151",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17150", "LEI": "54930000017150001"},
        aliases=["Maritime Holdings Inc", "Group Koryo Maritime Holdings Inc 151"]
    ),
    17151: SanctionedItem(
        sdn_id=17151,
        name="Ernesto Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1986-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17151"},
        aliases=["Qiang, Ernesto", "E. Qiang"]
    ),
    17152: SanctionedItem(
        sdn_id=17152,
        name="Orion Optics Group 153",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17152", "LEI": "54930000017152001"},
        aliases=["Optics Group", "Group Orion Optics Group 153"]
    ),
    17153: SanctionedItem(
        sdn_id=17153,
        name="Ibrahim Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1988-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17153"},
        aliases=["Cabello, Ibrahim", "I. Cabello"]
    ),
    17154: SanctionedItem(
        sdn_id=17154,
        name="Volga Tech Enterprises 155",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17154", "LEI": "54930000017154001"},
        aliases=["Tech Enterprises", "Group Volga Tech Enterprises 155"]
    ),
    17155: SanctionedItem(
        sdn_id=17155,
        name="Tariq Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1990-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17155"},
        aliases=["Lopez, Tariq", "T. Lopez"]
    ),
    17156: SanctionedItem(
        sdn_id=17156,
        name="Caspian Resource Consortium 157",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17156", "LEI": "54930000017156001"},
        aliases=["Resource Consortium", "Group Caspian Resource Consortium 157"]
    ),
    17157: SanctionedItem(
        sdn_id=17157,
        name="Nikolai Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1992-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17157"},
        aliases=["Ivanov, Nikolai", "N. Ivanov"]
    ),
    17158: SanctionedItem(
        sdn_id=17158,
        name="Pacific Metals S.A. 159",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17158", "LEI": "54930000017158001"},
        aliases=["Metals S.A.", "Group Pacific Metals S.A. 159"]
    ),
    17159: SanctionedItem(
        sdn_id=17159,
        name="Vladimir Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1994-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17159"},
        aliases=["Smirnov, Vladimir", "V. Smirnov"]
    ),
    17160: SanctionedItem(
        sdn_id=17160,
        name="Ros Prom Corporation 161",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17160", "LEI": "54930000017160001"},
        aliases=["Prom Corporation", "Group Ros Prom Corporation 161"]
    ),
    17161: SanctionedItem(
        sdn_id=17161,
        name="Andrei Sokolov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1956-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17161"},
        aliases=["Sokolov, Andrei", "A. Sokolov"]
    ),
    17162: SanctionedItem(
        sdn_id=17162,
        name="PJSC Finance Services DMCC 163",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17162", "LEI": "54930000017162001"},
        aliases=["Finance Services DMCC", "Group PJSC Finance Services DMCC 163"]
    ),
    17163: SanctionedItem(
        sdn_id=17163,
        name="Mikhail Soleimani",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1958-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17163"},
        aliases=["Soleimani, Mikhail", "M. Soleimani"]
    ),
    17164: SanctionedItem(
        sdn_id=17164,
        name="OJSC Energy Holdings Inc 165",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17164", "LEI": "54930000017164001"},
        aliases=["Energy Holdings Inc", "Group OJSC Energy Holdings Inc 165"]
    ),
    17165: SanctionedItem(
        sdn_id=17165,
        name="Reza Najafi",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1960-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17165"},
        aliases=["Najafi, Reza", "R. Najafi"]
    ),
    17166: SanctionedItem(
        sdn_id=17166,
        name="Al- Telecom Group 167",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17166", "LEI": "54930000017166001"},
        aliases=["Telecom Group", "Group Al- Telecom Group 167"]
    ),
    17167: SanctionedItem(
        sdn_id=17167,
        name="Farhad Il-sung",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1962-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17167"},
        aliases=["Il-sung, Farhad", "F. Il-sung"]
    ),
    17168: SanctionedItem(
        sdn_id=17168,
        name="Mahan Flot Enterprises 169",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17168", "LEI": "54930000017168001"},
        aliases=["Flot Enterprises", "Group Mahan Flot Enterprises 169"]
    ),
    17169: SanctionedItem(
        sdn_id=17169,
        name="Mahmoud Wei",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1964-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17169"},
        aliases=["Wei, Mahmoud", "M. Wei"]
    ),
    17170: SanctionedItem(
        sdn_id=17170,
        name="Koryo Maritime Consortium 171",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17170", "LEI": "54930000017170001"},
        aliases=["Maritime Consortium", "Group Koryo Maritime Consortium 171"]
    ),
    17171: SanctionedItem(
        sdn_id=17171,
        name="Slobodan Qiang",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1966-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17171"},
        aliases=["Qiang, Slobodan", "S. Qiang"]
    ),
    17172: SanctionedItem(
        sdn_id=17172,
        name="Orion Optics S.A. 173",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17172", "LEI": "54930000017172001"},
        aliases=["Optics S.A.", "Group Orion Optics S.A. 173"]
    ),
    17173: SanctionedItem(
        sdn_id=17173,
        name="Radovan Cabello",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1968-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17173"},
        aliases=["Cabello, Radovan", "R. Cabello"]
    ),
    17174: SanctionedItem(
        sdn_id=17174,
        name="Volga Tech Corporation 175",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17174", "LEI": "54930000017174001"},
        aliases=["Tech Corporation", "Group Volga Tech Corporation 175"]
    ),
    17175: SanctionedItem(
        sdn_id=17175,
        name="Goran Lopez",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1970-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17175"},
        aliases=["Lopez, Goran", "G. Lopez"]
    ),
    17176: SanctionedItem(
        sdn_id=17176,
        name="Caspian Resource Services DMCC 177",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17176", "LEI": "54930000017176001"},
        aliases=["Resource Services DMCC", "Group Caspian Resource Services DMCC 177"]
    ),
    17177: SanctionedItem(
        sdn_id=17177,
        name="Milorad Ivanov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1972-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17177"},
        aliases=["Ivanov, Milorad", "M. Ivanov"]
    ),
    17178: SanctionedItem(
        sdn_id=17178,
        name="Pacific Metals Holdings Inc 179",
        sdn_type="ENTITY",
        programs=["GLOMAG"],
        remarks="Designated entity under GLOMAG enforcement directive.",
        citizenships=["US", "EU"],
        identifications={"REG_NUM": "REG-17178", "LEI": "54930000017178001"},
        aliases=["Metals Holdings Inc", "Group Pacific Metals Holdings Inc 179"]
    ),
    17179: SanctionedItem(
        sdn_id=17179,
        name="Jean-Pierre Smirnov",
        sdn_type="INDIVIDUAL",
        programs=["GLOMAG"],
        remarks="Designated individual under GLOMAG; subject to secondary sanctions.",
        dob_list=["1974-05-12"],
        citizenships=["US", "GB"],
        identifications={"PASSPORT": "PASS-17179"},
        aliases=["Smirnov, Jean-Pierre", "J. Smirnov"]
    ),
}

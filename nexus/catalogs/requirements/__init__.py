"""
Requirements Master Registry Aggregator.
"""

from typing import Dict, Any, List, Optional

from nexus.catalogs.requirements.north_america_onboarding import REQ_RECORDS_NORTH_AMERICA_ONBOARDING, DocReqItem
from nexus.catalogs.requirements.uk_channel_islands_onboarding import REQ_RECORDS_UK_CHANNEL_ISLANDS_ONBOARDING, DocReqItem
from nexus.catalogs.requirements.european_union_onboarding import REQ_RECORDS_EUROPEAN_UNION_ONBOARDING, DocReqItem
from nexus.catalogs.requirements.switzerland_liechtenstein_onboarding import REQ_RECORDS_SWITZERLAND_LIECHTENSTEIN_ONBOARDING, DocReqItem
from nexus.catalogs.requirements.asia_pacific_onboarding import REQ_RECORDS_ASIA_PACIFIC_ONBOARDING, DocReqItem
from nexus.catalogs.requirements.offshore_financial_centers_onboarding import REQ_RECORDS_OFFSHORE_FINANCIAL_CENTERS_ONBOARDING, DocReqItem
from nexus.catalogs.requirements.middle_east_onboarding import REQ_RECORDS_MIDDLE_EAST_ONBOARDING, DocReqItem

DOCUMENT_REQUIREMENTS: Dict[str, Any] = {}
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_NORTH_AMERICA_ONBOARDING)
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_UK_CHANNEL_ISLANDS_ONBOARDING)
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_EUROPEAN_UNION_ONBOARDING)
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_SWITZERLAND_LIECHTENSTEIN_ONBOARDING)
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_ASIA_PACIFIC_ONBOARDING)
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_OFFSHORE_FINANCIAL_CENTERS_ONBOARDING)
DOCUMENT_REQUIREMENTS.update(REQ_RECORDS_MIDDLE_EAST_ONBOARDING)

def get_required_documents_for_entity(jurisdiction: str, entity_type: str) -> List[Any]:
    results = []
    juris = jurisdiction.upper()
    etype = entity_type.upper()
    for req in DOCUMENT_REQUIREMENTS.values():
        if (juris in req.applies_to_jurisdictions) and (etype in req.applies_to_entity_types):
            results.append(req)
    if not results:
        for req in DOCUMENT_REQUIREMENTS.values():
            if ("US" in req.applies_to_jurisdictions) and ("CORPORATION" in req.applies_to_entity_types):
                results.append(req)
    return results

"""
NexusCRM UBO & Corporate Structure Service.
Unwraps multi-tier ownership chains, detects circular equity holdings, and calculates beneficial ownership.
"""

from typing import List, Dict, Optional, Any
from nexus.database.connection import get_db_session
from nexus.models.ubo import UBOOwner, OwnershipGraph

class UBOService:
    @staticmethod
    def get_ubo_structure(client_id: str) -> Dict[str, Any]:
        with get_db_session() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM ubo_owners
                WHERE client_id = ?
                ORDER BY ownership_percentage DESC;
            """, (client_id,))
            rows = cursor.fetchall()
            owners = []
            graph = OwnershipGraph(entity_id=client_id)

            for r in rows:
                o_dict = dict(r)
                owner_obj = UBOOwner(
                    id=o_dict["id"],
                    client_id=o_dict["client_id"],
                    entity_id=o_dict["entity_id"],
                    owner_type=o_dict["owner_type"],
                    name=o_dict["name"],
                    ownership_percentage=o_dict["ownership_percentage"],
                    voting_rights_percentage=o_dict["voting_rights_percentage"],
                    is_direct_owner=bool(o_dict["is_direct_owner"]),
                    parent_owner_id=o_dict["parent_owner_id"],
                    country_of_citizenship=o_dict["country_of_citizenship"],
                    country_of_tax_residence=o_dict["country_of_tax_residence"],
                    is_pep=bool(o_dict["is_pep"]),
                    pep_tier=o_dict["pep_tier"],
                    sanctions_check_status=o_dict["sanctions_check_status"],
                    idv_verification_status=o_dict["idv_verification_status"],
                    control_type=o_dict["control_type"]
                )
                graph.add_owner(owner_obj)
                owners.append(owner_obj.to_dict())

            is_circular = graph.detect_circular_ownership()
            qualifying = [q.to_dict() for q in graph.get_qualifying_natural_ubos(threshold_pct=25.0)]

            return {
                "client_id": client_id,
                "total_owners": len(owners),
                "owners": owners,
                "has_circular_ownership": is_circular,
                "qualifying_ubos_fincen_cdd": qualifying,
                "requires_enhanced_due_diligence": is_circular or any(q["is_pep"] for q in qualifying)
            }

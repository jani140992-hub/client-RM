"""
Unit Tests for UBO Graph and Beneficial Ownership Engine.
"""

import unittest
from nexus.models.ubo import UBOOwner, OwnershipGraph

class TestUBOUnwrapping(unittest.TestCase):
    def test_qualifying_ubo_threshold(self):
        graph = OwnershipGraph(entity_id="ENT-TEST-01")
        o1 = UBOOwner(id="U1", client_id="C1", entity_id="ENT-TEST-01", owner_type="INDIVIDUAL", name="Owner One", ownership_percentage=35.0, voting_rights_percentage=35.0)
        o2 = UBOOwner(id="U2", client_id="C1", entity_id="ENT-TEST-01", owner_type="INDIVIDUAL", name="Owner Two", ownership_percentage=15.0, voting_rights_percentage=15.0)
        o3 = UBOOwner(id="U3", client_id="C1", entity_id="ENT-TEST-01", owner_type="INDIVIDUAL", name="Managing Director", ownership_percentage=5.0, voting_rights_percentage=5.0, control_type="SENIOR_MANAGING_OFFICIAL")

        graph.add_owner(o1)
        graph.add_owner(o2)
        graph.add_owner(o3)

        qualifying = graph.get_qualifying_natural_ubos(threshold_pct=25.0)
        # o1 qualifies (>25%), o3 qualifies (senior managing official)
        self.assertEqual(len(qualifying), 2)
        names = [q.name for q in qualifying]
        self.assertIn("Owner One", names)
        self.assertIn("Managing Director", names)

    def test_circular_ownership_cycle_detection(self):
        graph = OwnershipGraph(entity_id="ENT-CYCLE-01")
        # Parent A -> Parent B -> Parent A (Cycle)
        o_a = UBOOwner(id="ENT-A", client_id="C1", entity_id="ENT-CYCLE-01", owner_type="INTERMEDIARY_ENTITY", name="Holding A", ownership_percentage=50.0, voting_rights_percentage=50.0, parent_owner_id="ENT-B")
        o_b = UBOOwner(id="ENT-B", client_id="C1", entity_id="ENT-CYCLE-01", owner_type="INTERMEDIARY_ENTITY", name="Holding B", ownership_percentage=50.0, voting_rights_percentage=50.0, parent_owner_id="ENT-A")

        graph.add_owner(o_a)
        graph.add_owner(o_b)

        self.assertTrue(graph.detect_circular_ownership())

    def test_acyclic_ownership_tree(self):
        graph = OwnershipGraph(entity_id="ENT-ACYCLIC-01")
        o_p = UBOOwner(id="ENT-P", client_id="C1", entity_id="ENT-ACYCLIC-01", owner_type="INTERMEDIARY_ENTITY", name="Parent Co", ownership_percentage=100.0, voting_rights_percentage=100.0, parent_owner_id=None)
        o_c = UBOOwner(id="IND-C", client_id="C1", entity_id="ENT-ACYCLIC-01", owner_type="INDIVIDUAL", name="Ultimate Founder", ownership_percentage=100.0, voting_rights_percentage=100.0, parent_owner_id="ENT-P")

        graph.add_owner(o_p)
        graph.add_owner(o_c)

        self.assertFalse(graph.detect_circular_ownership())

if __name__ == "__main__":
    unittest.main()

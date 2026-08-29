"""
Unit Tests for Workflow Engine and Stage Progression.
"""

import unittest
from nexus.services.client_service import ClientService
from nexus.services.onboarding_service import OnboardingService
from nexus.models.onboarding import STAGE_ORDER

class TestWorkflowEngine(unittest.TestCase):
    def test_onboarding_lifecycle_advance(self):
        client = ClientService.create_client(
            name="Apex Workflow Test Corp",
            client_segment="WEALTH_MANAGEMENT",
            rm_id="RM-102",
            jurisdiction="GB",
            entity_type="LLC"
        )
        case = OnboardingService.initialize_case(client["id"], rm_id="RM-102")
        self.assertEqual(case["current_stage"], STAGE_ORDER[0].value)
        self.assertEqual(case["stage_index"], 0)

        # Advance stage
        advanced = OnboardingService.advance_stage(
            case["id"],
            actor_id="RM-102",
            actor_role="RELATIONSHIP_MANAGER",
            notes="Completed stage 1 pre-qualification"
        )
        self.assertEqual(advanced["current_stage"], STAGE_ORDER[1].value)
        self.assertEqual(advanced["stage_index"], 1)
        self.assertGreater(advanced["completion_percentage"], 0.0)

if __name__ == "__main__":
    unittest.main()

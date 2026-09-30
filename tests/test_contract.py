from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills" / "skill-create" / "SKILL.md").read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_modes_separate_publication_authority(self):
        self.assertIn("**Explore**", SKILL)
        self.assertIn("**Build**", SKILL)
        self.assertIn("**Launch**", SKILL)
        self.assertIn("publish only when the user explicitly asks", SKILL)

    def test_release_layers_are_not_collapsed(self):
        for state in ("local", "committed", "pushed", "released", "publicly reachable", "listed", "clean-install verified"):
            self.assertIn(state, SKILL)

    def test_external_promotion_needs_separate_approval(self):
        self.assertIn("Do not contact third parties", SKILL)
        self.assertIn("without separate explicit approval", SKILL)

    def test_high_risk_domains_have_boundary(self):
        for domain in ("financial", "medical", "legal", "identity", "security"):
            self.assertIn(domain, SKILL)


if __name__ == "__main__":
    unittest.main()

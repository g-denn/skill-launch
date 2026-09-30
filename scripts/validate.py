from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "skill-create" / "SKILL.md"
OPENAI = ROOT / "skills" / "skill-create" / "agents" / "openai.yaml"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    skill_text = SKILL.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not match:
        fail("SKILL.md requires YAML frontmatter")
    frontmatter = match.group(1)
    if "name: skill-create" not in frontmatter:
        fail("frontmatter name must be skill-create")
    if "description:" not in frontmatter:
        fail("frontmatter description is required")
    if "[TODO" in skill_text:
        fail("SKILL.md contains an unfinished TODO placeholder")

    openai_text = OPENAI.read_text(encoding="utf-8")
    for required in ('display_name: "Skill Create"', 'default_prompt: "Use $skill-create'):
        if required not in openai_text:
            fail(f"openai.yaml missing {required}")

    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugin = data["plugins"][0]
    if plugin["name"] != "skill-create" or "./skills/skill-create" not in plugin["skills"]:
        fail("marketplace metadata does not expose skill-create")

    for path in (
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "SECURITY.md",
        ROOT / "PRODUCT_VISION.md",
        ROOT / "TODO.md",
    ):
        if not path.is_file():
            fail(f"missing {path.relative_to(ROOT)}")

    print("skill-create repository validation passed")


if __name__ == "__main__":
    main()

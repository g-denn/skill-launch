from pathlib import Path
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "skill-launch" / "SKILL.md"
OPENAI = ROOT / "skills" / "skill-launch" / "agents" / "openai.yaml"
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
    if "name: skill-launch" not in frontmatter:
        fail("frontmatter name must be skill-launch")
    if "description:" not in frontmatter:
        fail("frontmatter description is required")
    if "[TODO" in skill_text:
        fail("SKILL.md contains an unfinished TODO placeholder")

    openai_text = OPENAI.read_text(encoding="utf-8")
    for required in ('display_name: "Skill Launch"', 'default_prompt: "Use $skill-launch'):
        if required not in openai_text:
            fail(f"openai.yaml missing {required}")

    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugin = data["plugins"][0]
    if plugin["name"] != "skill-launch" or "./skills/skill-launch" not in plugin["skills"]:
        fail("marketplace metadata does not expose skill-launch")

    for path in (
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "SECURITY.md",
        ROOT / "PRODUCT_VISION.md",
        ROOT / "TODO.md",
    ):
        if not path.is_file():
            fail(f"missing {path.relative_to(ROOT)}")

    print("skill-launch repository validation passed")


if __name__ == "__main__":
    main()

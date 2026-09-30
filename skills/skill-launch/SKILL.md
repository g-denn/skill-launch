---
name: skill-launch
description: "Research, design, build, publish, and verify a differentiated Agent Skill as a public GitHub repository. Use when the user explicitly asks to create and launch a new skill end to end for usefulness, discoverability, distribution, or GitHub adoption. Do not use for brainstorming-only requests, local-only prototypes, or installing an existing skill."
---

# Skill Launch

Turn a useful, narrow idea into a public, installable Agent Skill. Optimize for repeated usefulness and trust. Stars are an outcome, not an acceptance test.

## Determine the authorized mode

- **Explore**: research and recommend ideas. Do not create repositories or publish.
- **Build**: create and validate local files. Do not publish.
- **Launch**: publish only when the user explicitly asks to publish, ship, launch, create a public repository, or complete the work end to end.

Publication authorization covers the repository, release, metadata, and skills directory registration needed for the requested launch. It does not authorize social posts, messages to maintainers, paid services, account changes, or other promotion.

## Run the launch loop

1. Inspect the user's strengths, existing work, and constraints. Avoid duplicating their current skills.
2. Research current alternatives and demand using fresh primary sources. Check GitHub and skill directories for name and concept collisions.
3. Score three to five candidates using [idea selection](references/idea-selection.md). Choose one narrow promise with a demonstrable result.
4. Define the trigger, non-trigger, inputs, output contract, safety boundary, and acceptance checks before writing files.
5. Create the smallest complete repository. Include `SKILL.md`, `agents/openai.yaml`, a clear README, license, security guidance, contribution guidance, tests, and only the references or scripts the skill genuinely needs.
6. Use original text and synthetic examples. Confirm licenses and data rights for every borrowed asset or dependency.
7. Validate the skill locally with the official validator when available, then run repository tests. Exercise one realistic happy path and one important refusal or stop path.
8. In Launch mode, create the public GitHub repository, push the exact tested commit, add useful topics, publish a semantic version release, and enable available security settings.
9. Verify each release layer separately using [the release contract](references/release-contract.md). Fix failures before claiming completion.
10. Apply [distribution guidance](references/distribution.md) to the repository itself. Do not manufacture engagement or promise stars.

## Keep the launch safe

- Treat financial, medical, legal, identity, and security domains as high-risk. Prefer evidence organization, education, and analysis over decisions or personalized advice.
- Never upload secrets, cookies, private datasets, personal messages, or proprietary source material.
- Stop if authentication is missing, the proposed name is misleading or collides materially, rights are unclear, tests fail, installation fails, or publication was not authorized.
- Preserve the difference between local, committed, pushed, released, publicly reachable, listed, and clean-install verified.
- Do not contact third parties or publish promotional content without separate explicit approval.

## Report the outcome

Return the chosen problem and why it won, the public repository and release links, the exact install command, verification evidence, and any remaining distribution work. If blocked, name the exact failed layer and the smallest action that would unblock it.

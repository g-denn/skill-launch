# Release contract

Do not collapse these states into “published.” Record evidence for each one.

1. **Validated locally**: the skill validator and repository tests pass.
2. **Committed**: the tested files exist in a named Git commit.
3. **Pushed**: the remote default branch resolves to that commit.
4. **Public**: an unauthenticated request can read the repository and `SKILL.md`.
5. **Released**: a semantic version tag and GitHub release point to the tested commit.
6. **CI verified**: the public workflow for that commit passes.
7. **Installable**: a clean temporary directory can install the named skill from `OWNER/REPO`.
8. **Discoverable**: the skills directory page resolves, when the directory supports the repository.

Use a clean installation command such as:

```text
npx skills add OWNER/REPO --skill SKILL_NAME
```

Never treat an authenticated local checkout, a successful push, or a directory page alone as proof of all eight layers.

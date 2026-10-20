# Contributing

Thank you for improving Legal Academic Skills. Contributions should make workflows more accurate, transparent, testable, and useful to researchers and legal professionals.

## Before submitting

- Explain the use case, intended user, and limitations.
- Keep each skill focused; use references for detailed material that need not load on every invocation.
- Do not include confidential, privileged, personal, or unpublished material without permission.
- Never add fabricated citations, sample authorities presented as real, or unverifiable claims of legal accuracy.
- Identify jurisdictions and dates where legal rules are jurisdiction-specific or time-sensitive.
- Preserve source attribution and check the licence for contributed material. Contributions are accepted under the repository's licence (`GPL-3.0-only`).
- Add or update evaluation cases in `evals/` for material behaviour changes.
- Run all checks from the repository root:

  ```bash
  claude plugin validate ./
  python3 scripts/validate_skills.py
  python3 -m unittest discover -s tests -v
  ```

## Skill conventions

- Edit skills only under `skills/`. `.agents/skills` is a symbolic link to `../skills`; do not replace it with copies.
- Use a folder name and frontmatter `name` in lowercase kebab-case, matching one another.
- Include a useful `description` that explains what the skill does and when to use it.
- Keep the main `SKILL.md` concise enough to act as an entry point.
- Use relative links for files shipped with the skill and verify those links.
- State required inputs, expected outputs, uncertainty handling, and review gates.
- Do not claim support for tools or platforms that have not been tested.

## When you add or change a skill

- Add or update its entry in `SKILL_INDEX.md` and in the workflow list in `README.md`.
- Update `project-import/PROJECT_UPLOAD_BUNDLE.md` if the skill should appear in the upload bundle.
- Add a line to `CHANGELOG.md` under "Unreleased".

## Releases and versioning

- Keep `version` identical in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (both the plugin entry and, if present, the top level).
- Bump the version when skills, agents, or manifests change, so installed users can update.
- Move the changelog's "Unreleased" entries under the new version heading and tag the release (for example `v0.1.2`).

## Review expectations

Reviewers should check scope, factual and source accuracy, citation integrity, counterarguments, privacy, safety, licensing, portability, and regression cases. Approval does not guarantee that generated legal or academic work is correct for every matter.

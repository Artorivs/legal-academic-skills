# Supplemental files for Legal Academic Agent Skills

This archive contains **additional** repository files; it intentionally does not duplicate the integration files drafted earlier (`.claude-plugin/plugin.json`, `.plugin`, `.agents/`, `agents/`, or `scripts/install-agent-skills.sh`).

## Merge into your repository

Extract this archive at the root of `legal-academic-skills`, preserving directory structure. Review each file before committing.

## Contents

- `docs/compatibility.md` — platform and packaging notes.
- `references/legal-research-standards.md` — source, authority, citation, and uncertainty controls.
- `evals/README.md` and `evals/cases/` — initial human-review evaluation cases.
- `tests/test_skill_structure.py` — basic structural checks for `skills/**/SKILL.md`.
- `scripts/validate_skills.py` — standard-library-only metadata and reference validator.
- `.github/workflows/validate-skills.yml` — CI for the validator and tests.
- `CONTRIBUTING.md`, `CHANGELOG.md`, `SECURITY.md` — project governance templates.
- `examples/` — illustrative claim-evidence matrix and research log.

## Before publishing

1. Confirm the canonical skill directory (`skills/`) and adjust scripts if your repository uses a different path.
2. Reconcile the repository's actual `LICENSE` with all licensing statements. This archive intentionally does not create or replace a license because the existing repository's licensing status must be checked by its maintainer.
3. Run `python3 scripts/validate_skills.py` and `python3 -m unittest discover -s tests -v` from the repository root after merging.
4. Inspect the generated diff and test from a clean checkout before releasing.

These materials are starter templates, not a certification of legal, scholarly, security, or platform compliance.

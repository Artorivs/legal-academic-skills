# Platform compatibility

What is checked, and what is not. Platforms change their skill and plugin formats, so check a platform's current documentation before relying on a route marked "not tested".

| Platform | How to install | What is checked |
|---|---|---|
| Claude Code | Plugin, from the marketplace or a local clone (README) | `claude plugin validate ./` passes. The skill files' metadata and links are checked in CI on every push. |
| Claude, ChatGPT or Gemini projects | Paste `project-import/PROJECT_INSTRUCTIONS.md` and upload `PROJECT_UPLOAD_BUNDLE.md` | CI checks that the bundle matches the skills. Whether a platform follows a workflow from an uploaded file is **not tested**. Ask for a workflow by name if it is not used. |
| Other agents that read Agent Skills | `bash scripts/install-agent-skills.sh TARGET_DIR` | The installer is tested to copy whole skill folders and to refuse the canonical `skills/` directory. Discovery in any particular agent is **not tested**. |

## Layout rules

- `skills/<name>/SKILL.md` is the one canonical copy of each skill. Its `references/` folder travels with it.
- `.agents/skills` is a symbolic link to `skills/` for agents that look there. On Windows, Git may check it out as a plain file unless symlinks are enabled. In that case, copy the skills from `skills/`.
- `.claude-plugin/plugin.json` is the plugin manifest. `.claude-plugin/marketplace.json` is the marketplace catalogue. Keep the two `version` fields identical.

Add a row to the table above only after testing the route, and say what was tested.

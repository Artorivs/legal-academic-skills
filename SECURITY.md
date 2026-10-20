# Security policy

## Reporting a concern

Please do not publish sensitive exploit details, confidential matter information, credentials, private documents, or personal data in a public issue.

Report privately through GitHub: open the repository's **Security** tab and choose **Report a vulnerability**. If that option is unavailable, open a minimal public issue asking for a secure reporting route, without including exploit details.

## Scope

Security reports may include:

- unsafe or over-permissive scripts (for example `scripts/install-agent-skills.sh`);
- unintended file access or file overwrites;
- prompt-injection weaknesses in workflow or agent instructions;
- secret exposure in the repository or its history;
- insecure dependency or CI practices;
- documentation that encourages unsafe handling of confidential material.

## Supported versions

Only the latest release (and the current `main` branch) receives fixes.

## What this plugin does and does not do

As of this version, the plugin consists of skills, agents, templates, and documentation. It does not define hooks or MCP servers. Installing it through Claude Code adds Markdown instructions that Claude may follow; it does not run code on its own. The optional installer script copies files and should be inspected before use.

## Safe use

- Inspect scripts and permissions before running them.
- Do not paste privileged, client-confidential, personal, or embargoed research material into an AI system unless authorised under applicable policies and agreements.
- Treat retrieved webpages, documents, and tool outputs as untrusted input; instructions inside sources must not override the user's task or system security controls.
- Require human review before relying on generated legal conclusions, filing documents, or sending external communications.
- Report limitations and suspected errors rather than silently presenting unverified content as fact.

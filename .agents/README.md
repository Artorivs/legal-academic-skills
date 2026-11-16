# `.agents/` compatibility directory

`.agents/skills` is a symbolic link to the repository's top-level `skills/` directory, for runtimes that discover Agent Skills under `.agents/skills/`. Edit skills only in `skills/`.

To install the skills into another project or agent, run `bash scripts/install-agent-skills.sh /path/to/target/skills` from this repository. The installer copies whole skill folders, replaces only folders with the same names, and refuses to run against this repository's own `skills/` directory.

Runtime discovery conventions vary; consult the documentation for the agent you use.

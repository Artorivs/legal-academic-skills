#!/usr/bin/env bash
# Copy the canonical skills into an agent's skill directory.
#
# Usage: bash scripts/install-agent-skills.sh [TARGET_DIR]
#   TARGET_DIR defaults to ./.agents/skills in the current working directory
#   (run it from the project you want the skills in).
# Matching skill folders in TARGET_DIR are replaced; other folders are left alone.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/skills"
TARGET="${1:-$PWD/.agents/skills}"

if [[ ! -d "$SOURCE" ]]; then
  echo "ERROR: canonical skills directory not found: $SOURCE" >&2
  exit 1
fi
mkdir -p "$TARGET"

# Refuse to install into the canonical source itself. In this repository
# .agents/skills is a symlink to ../skills, so replacing a "target" folder
# there would delete the canonical skill.
if [[ "$(cd "$TARGET" && pwd -P)" == "$(cd "$SOURCE" && pwd -P)" ]]; then
  echo "Nothing to do: $TARGET is the canonical skills directory (or a link to it)." >&2
  echo "Pass the directory of the project or agent you want to install into." >&2
  exit 0
fi

while IFS= read -r -d '' skill_dir; do
  skill_name="$(basename "$skill_dir")"
  if [[ ! -f "$skill_dir/SKILL.md" ]]; then
    echo "WARN: skipping $skill_name (no SKILL.md)" >&2
    continue
  fi
  if [[ -e "$TARGET/$skill_name" || -L "$TARGET/$skill_name" ]]; then
    rm -rf -- "${TARGET:?}/$skill_name"
  fi
  cp -R -- "$skill_dir" "$TARGET/$skill_name"
  echo "Installed $skill_name"
done < <(find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)

echo "Agent Skills copied to $TARGET"
echo "Matching skill folders there were replaced; review local changes before rerunning."

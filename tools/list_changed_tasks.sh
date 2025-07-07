#!/usr/bin/env bash
BASE="$1"
HEAD="$2"

# Always run git commands inside the student repo
git -C student diff --name-only "$BASE" "$HEAD" \
  | awk -F/ '/^task-[0-9]+/ {print $1}' \
  | sort -u


#!/bin/bash

# scripts/rollback-release.sh
# Rollback local changes after a failed semantic-release (e.g., push error)

# 1. Deleting the last semver tag
LATEST_TAG=$(git tag --sort=-v:refname | head -n 1)

if [[ $LATEST_TAG =~ ^v[0-9]+\.[0-9]+\.[0-9]+ ]]; then
    echo "Found semver tag: $LATEST_TAG"
    git tag -d "$LATEST_TAG"
    echo "Local tag $LATEST_TAG deleted."
else
    echo "No semver tag starting with 'v' found to delete."
fi

# 2. Resetting the HEAD if the last commit is a version update
LATEST_COMMIT_MSG=$(git log -1 --pretty=%B)

if [[ $LATEST_COMMIT_MSG == "chore: update version to"* ]]; then
    echo "Detected semantic-release commit: $LATEST_COMMIT_MSG"
    git reset --hard HEAD~1
    echo "HEAD reset to previous commit."
else
    echo "Latest commit does not appear to be a 'chore: update version to' commit."
    echo "No git reset performed to avoid data loss. Manual check recommended."
    git log -n 1 --oneline
fi

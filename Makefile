ifneq ("$(wildcard .env)","")
	include .env
	export $(shell sed 's/=.*//' .env)
endif

## Semver

version:
	semantic-release version

patch:
	semantic-release version --patch

minor:
	semantic-release version --minor

major:
	semantic-release version --major

## Tag-only (no release)

patch-tag:
	semantic-release version --patch --no-vcs-release

minor-tag:
	semantic-release version --minor --no-vcs-release

major-tag:
	semantic-release version --major --no-vcs-release

## Content management

toc:
	./scripts/toc.sh src/main.md

## Files management

format:
	mdformat src
	./scripts/fix-backslashes.sh src/main.md

release:
	./scripts/release.sh src/main.md

template:
	./scripts/to-odt.sh src/templates/project.md data-economie-gabarit-projet

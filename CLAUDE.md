# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a knowledge repository about **Anki** — a spaced repetition memory tool. The repository contains:

- **Documentation** (root level): Markdown files explaining Anki concepts, installation, card types, and usage guides
- **Flashcard content** (`english/`): Pre-made flashcard decks organized by subject/grade
- **Manual** (`manual/`): Additional reference documentation

## Repository Structure

```
/
├── 01-anki-introduction.md    # What is Anki, spaced repetition science
├── 02-anki-install-guide.md  # Installation instructions
├── 03-anki-core-concepts.md # Decks, cards, notes, reviews
├── 04-anki-basic-cards.md    # Basic card creation
├── 05-anki-cloze.md          # Cloze deletion cards
├── 06-anki-image-occlusion.md
├── 07-anki-card-principles.md
├── 08-anki-connect.md        # AnkiConnect API for VSCode
├── 09-anki-vscode.md        # Anki extension for VSCode
├── 10-anki-basic-usage.md   # Complete beginner guide
├── english/                  # Flashcard content (Markdown format)
│   └── Unit1_Hello.md        # Example: Grade 3 English Unit 1
└── manual/                   # Reference documentation
    ├── 01.background.md
    ├── 01-getting-started.md
    └── 02-studying.md
```

## Flashcard Content Format

Flashcard content in `english/` uses this Markdown structure:

```markdown
# Category::SubCategory::Topic

## word /phonetic/
meaning
usage example

## another_word /phonetic/
meaning
usage example
```

Example from `english/Unit1_Hello.md`:
```markdown
# 03三年级::01上学期::01英语::01_Unit1 Hello

## hello /həˈləʊ/
你好
Hello! I'm Amy.
```

## Content Organization

- Files are named by subject and unit (e.g., `Unit1_Hello.md`)
- Category hierarchy is encoded in the first heading: `年级::学期::学科::单元`
- Each card entry starts with `##` and contains: word, phonetic pronunciation, meaning, and example

## No Build System

This repository contains only Markdown documentation and flashcard content. There are no build commands, tests, or code to run. All content is consumed by Anki or used as reference documentation.

## Git Conventions

- Commit messages should be written in **Chinese**
- See `.trae/rules/git-commit-message.md` for formatting rules
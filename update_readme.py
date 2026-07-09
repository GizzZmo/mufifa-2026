with open('README.md', 'r') as f:
    readme = f.read()

# Add Markdown Formatting to the table
readme = readme.replace('| MUID consistency | Filename and embed MUID must match |', '| MUID consistency | Filename and embed MUID must match |\n| Markdown Formatting | Strict conformance to standard Markdown rules via `markdownlint` |')

# Update pre-commit text
readme = readme.replace('the validator runs automatically', 'the validator and `markdownlint` run automatically')

# Add the Gamification section before the Roadmap
new_section = """
---

## 🚀 Live Gamification & Automated Assets (Phases 1 & 2 Complete)

The tournament has now integrated the following automated features from our Roadmap:
* **Strict Markdown Conformance**: Uses `markdownlint` in our CI and pre-commit hooks to keep all profiles perfectly formatted.
* **Dynamic SVG Badges**: Our CI automatically reads `docs/LEADERBOARD.md` and generates custom high-quality SVG badges for performers, deployed directly to GitHub Pages.
* **Leaderboard Data Feed**: A `leaderboard.json` feed is periodically generated, allowing community developers to build their own live dashboards.
* **Multi-Language Testing Sandbox**: GitHub workflows now support running and grading unit tests in Python, Node.js, Go, and Rust.
"""

readme = readme.replace('\n---\n\n## 🗺️ Multi-Paradigm', new_section + '\n---\n\n## 🗺️ Multi-Paradigm')

with open('README.md', 'w') as f:
    f.write(readme)

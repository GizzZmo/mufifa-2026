with open('README.md', 'r') as f:
    readme = f.read()

old_text = "We are scaling μFIFA 2026 into a full-featured, automated tournament engine. Check out our **[Multi-Paradigm Multi-Language System Roadmap](./docs/ROADMAP.md)** to see how we plan to integrate:"
new_text = "We are scaling μFIFA 2026 into a full-featured, automated tournament engine. Phase 1 & 2 are complete! Check out our **[Multi-Paradigm Multi-Language System Roadmap](./docs/ROADMAP.md)** to see our progress and what's next in Phase 3:"

readme = readme.replace(old_text, new_text)

with open('README.md', 'w') as f:
    f.write(readme)

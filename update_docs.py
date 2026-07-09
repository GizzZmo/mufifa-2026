import re

with open('docs/ROADMAP.md', 'r') as f:
    roadmap = f.read()

roadmap = roadmap.replace('* [ ] **Pre-commit', '* [x] **Pre-commit')
roadmap = roadmap.replace('* [ ] **Strict Markdown', '* [x] **Strict Markdown')
roadmap = roadmap.replace('* [ ] **Automated Lint', '* [x] **Automated Lint')
roadmap = roadmap.replace('* [ ] **Dynamic SVG', '* [x] **Dynamic SVG')
roadmap = roadmap.replace('* [ ] **Multi-Language', '* [x] **Multi-Language')
roadmap = roadmap.replace('* [ ] **JSON Data', '* [x] **JSON Data')

with open('docs/ROADMAP.md', 'w') as f:
    f.write(roadmap)

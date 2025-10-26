#!/usr/bin/env python3
import re
from pathlib import Path

# Get all markdown files in content
md_files = list(Path('content').glob('**/*.md'))

for md_file in md_files:
    with open(md_file, 'r') as f:
        content = f.read()

    # Split frontmatter from body
    parts = content.split('---', 2)
    if len(parts) < 3:
        continue

    frontmatter = parts[1]
    body = parts[2]

    # Remove leading whitespace from HTML lines while preserving structure
    lines = body.split('\n')
    fixed_lines = []
    for line in lines:
        # Remove leading whitespace but preserve indentation within HTML
        stripped = line.lstrip()
        if stripped:  # Only process non-empty lines
            fixed_lines.append(stripped)
        else:
            fixed_lines.append('')  # Keep empty lines

    fixed_body = '\n'.join(fixed_lines)

    # Rebuild file
    new_content = f'---\n{frontmatter}---\n{fixed_body}'

    with open(md_file, 'w') as f:
        f.write(new_content)

    print(f'Fixed indentation: {md_file}')

print('Done!')

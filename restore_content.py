#!/usr/bin/env python3
import re
from pathlib import Path

# Map of markdown files to their backup HTML files and gradients
file_mappings = {
    'content/tips/balanced-seat.md': ('_backup/balanced-seat.html', 'gradient-sunset'),
    'content/tips/natural-horsemanship.md': ('_backup/natural-horsemanship.html', 'gradient-meadow'),
    'content/tips/speed-agility.md': ('_backup/speed-agility.html', 'gradient-sky'),
    'content/categories/dressage.md': ('_backup/dressage.html', 'gradient-sunset'),
    'content/categories/trail-riding.md': ('_backup/trail-riding.html', 'gradient-meadow'),
    'content/categories/show-jumping.md': ('_backup/show-jumping.html', 'gradient-sky'),
    'content/categories/western-riding.md': ('_backup/western-riding.html', 'gradient-sunset'),
    'content/categories/horse-health.md': ('_backup/horse-health.html', 'gradient-sunset'),
    'content/categories/beginner-basics.md': ('_backup/beginner-basics.html', 'gradient-sunset'),
    'content/insights/perfect-gait.md': ('_backup/perfect-gait.html', 'gradient-sunset'),
    'content/insights/building-strength.md': ('_backup/building-strength.html', 'gradient-meadow'),
    'content/insights/mental-focus.md': ('_backup/mental-focus.html', 'gradient-sky'),
    'content/insights/bond-building.md': ('_backup/bond-building.html', 'gradient-sunset'),
    'content/insights/quick-reflexes.md': ('_backup/quick-reflexes.html', 'gradient-sunset'),
    'content/insights/relaxation-tech.md': ('_backup/relaxation-tech.html', 'gradient-meadow'),
    'content/insights/competition-ready.md': ('_backup/competition-ready.html', 'gradient-sky'),
    'content/insights/advanced-techniques.md': ('_backup/advanced-techniques.html', 'gradient-sunset'),
}

def extract_content_from_html(html_file):
    """Extract content from the Content Section"""
    with open(html_file, 'r') as f:
        content = f.read()

    # Find content between "<!-- Content Section -->" and "<!-- Related Articles -->" or "<!-- Footer -->"
    match = re.search(r'<!-- Content Section -->.*?<section class="py-16 bg-white">(.*?)(?:<!-- Related Articles -->|<!-- Footer -->)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

for md_file, (html_file, gradient) in file_mappings.items():
    html_path = Path(html_file)
    md_path = Path(md_file)

    if not html_path.exists() or not md_path.exists():
        print(f"Skipping {md_file}: files not found")
        continue

    # Read current markdown file
    with open(md_path, 'r') as f:
        md_content = f.read()

    # Extract frontmatter
    parts = md_content.split('---', 2)
    frontmatter_text = parts[1]

    # Extract HTML content
    html_content = extract_content_from_html(str(html_path))
    if not html_content:
        print(f"Warning: No content extracted from {html_file}")
        continue

    # Clean up the extracted HTML (remove extra divs, clean whitespace)
    html_content = html_content.replace('<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">', '')
    html_content = html_content.replace('</div>', '', 1)  # Remove closing div
    html_content = re.sub(r'\n\s*\n', '\n', html_content)  # Clean multiple newlines

    # Add heroGradient to frontmatter if not present
    if 'heroGradient:' not in frontmatter_text:
        # Find where to insert it (after title)
        frontmatter_text = re.sub(
            r'(title: "[^"]*"\n)',
            f'\\1heroGradient: "{gradient}"\n',
            frontmatter_text
        )

    # Rebuild the file
    new_content = f'---\n{frontmatter_text}---\n\n{html_content}\n'

    with open(md_path, 'w') as f:
        f.write(new_content)

    print(f'Updated: {md_file}')

print('Done!')

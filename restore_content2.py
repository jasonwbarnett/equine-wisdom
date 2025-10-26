#!/usr/bin/env python3
import re
from pathlib import Path

# Map of markdown files to their backup HTML files and gradients
file_mappings = {
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
    """Extract content section from HTML file"""
    with open(html_file, 'r') as f:
        content = f.read()

    # Find the main content section - everything after the hero section until footer
    # Look for content between </section> (end of hero) and final sections
    match = re.search(
        r'</section>\s*<!-- Content Section -->.*?<section class="py-16 bg-white">(.*?)(?=<section|</body>)',
        content,
        re.DOTALL
    )

    if match:
        return match.group(1).strip()

    # Try alternate pattern without comments
    match = re.search(
        r'<section class="py-16 bg-white">(.*?)(?=<section class="py-16 bg-gray-50"|<footer|</body>)',
        content,
        re.DOTALL
    )

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
    frontmatter_text = parts[1] if len(parts) > 1 else ""

    # Extract HTML content
    html_content = extract_content_from_html(str(html_path))

    if not html_content:
        print(f"Warning: No content extracted from {html_file}")
        continue

    # Clean up the extracted HTML
    html_content = html_content.replace('<div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">', '')
    # Remove matching closing divs
    html_content = re.sub(r'^\s*</div>\s*$', '', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'\n\s*\n', '\n', html_content)  # Clean multiple newlines

    # Add heroGradient to frontmatter if not present
    if 'heroGradient:' not in frontmatter_text:
        # Add after title
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

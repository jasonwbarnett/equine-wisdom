#!/usr/bin/env python3
import os
from pathlib import Path

# Define all the correct titles and information
content_data = {
    'content/tips/balanced-seat.md': {
        'title': 'Balanced Seat Mastery',
        'description': 'Learn how to develop a perfectly balanced seat that gives you control and comfort in every discipline. Proper posture is the foundation of great horsemanship.',
        'emoji': '🏇',
        'border': 'border-amber-100',
    },
    'content/tips/natural-horsemanship.md': {
        'title': 'Natural Horsemanship',
        'description': 'Build trust with your horse using gentle, nature-based techniques. Understand equine psychology and create a harmonious partnership based on respect and communication.',
        'emoji': '🌿',
        'border': 'border-green-100',
    },
    'content/tips/speed-agility.md': {
        'title': 'Speed & Agility Training',
        'description': 'Unlock your horse\'s potential with targeted exercises that build speed and athletic performance. Perfect for jumping, barrel racing, and endurance events.',
        'emoji': '💨',
        'border': 'border-blue-100',
    },
    'content/categories/dressage.md': {
        'title': 'Dressage',
        'description': 'Master the classical discipline of dressage with techniques focusing on collection, balance, and precision movements.',
        'emoji': '🎪',
        'highlights': ['Walk, Trot, Canter Basics', 'Advanced Movements', 'Competition Prep'],
    },
    'content/categories/trail-riding.md': {
        'title': 'Trail Riding',
        'description': 'Explore outdoor adventures safely with comprehensive trail riding guidance and horse conditioning techniques.',
        'emoji': '🏔️',
        'highlights': ['Terrain Navigation', 'Endurance Building', 'Safety Essentials'],
    },
    'content/categories/show-jumping.md': {
        'title': 'Show Jumping',
        'description': 'Learn the art of jumping with expert tips on approach, takeoff, and landing techniques for various obstacle heights.',
        'emoji': '🚀',
        'highlights': ['Fence Approach', 'Perfect Take-off', 'Landing & Recovery'],
    },
    'content/categories/western-riding.md': {
        'title': 'Western Riding',
        'description': 'Perfect your western style with techniques for barrel racing, cutting, and western pleasure disciplines.',
        'emoji': '🤠',
        'highlights': ['Barrel Racing Tips', 'Cutting Techniques', 'Reining Skills'],
    },
    'content/categories/horse-health.md': {
        'title': 'Horse Health',
        'description': 'Essential information on nutrition, injury prevention, and maintaining optimal health for your equine partner.',
        'emoji': '🏥',
        'highlights': ['Nutrition Guide', 'Injury Prevention', 'Wellness Tips'],
    },
    'content/categories/beginner-basics.md': {
        'title': 'Beginner Basics',
        'description': 'Start your equestrian journey with foundational skills and horse handling fundamentals for new riders.',
        'emoji': '👶',
        'highlights': ['Safety First', 'Grooming & Care', 'Basic Commands'],
    },
    'content/insights/perfect-gait.md': {
        'title': 'Perfect Your Gait',
        'description': 'Develop smooth, controlled gaits through targeted exercises and consistent practice routines.',
        'emoji': '🎯',
        'gradient': 'from-amber-50 to-orange-50',
        'border': 'border-amber-200',
    },
    'content/insights/building-strength.md': {
        'title': 'Building Strength',
        'description': 'Strengthen your horse\'s muscles with specific conditioning exercises that improve performance.',
        'emoji': '💪',
        'gradient': 'from-green-50 to-emerald-50',
        'border': 'border-green-200',
    },
    'content/insights/mental-focus.md': {
        'title': 'Mental Focus',
        'description': 'Train your horse\'s mind for concentration and responsiveness in any riding situation.',
        'emoji': '🧠',
        'gradient': 'from-blue-50 to-cyan-50',
        'border': 'border-blue-200',
    },
    'content/insights/bond-building.md': {
        'title': 'Bond Building',
        'description': 'Create deeper connections with your horse through trust-building exercises and quality time.',
        'emoji': '🤝',
        'gradient': 'from-purple-50 to-pink-50',
        'border': 'border-purple-200',
    },
    'content/insights/quick-reflexes.md': {
        'title': 'Quick Reflexes',
        'description': 'Improve your horse\'s response time with agility drills and reactive training techniques.',
        'emoji': '⚡',
        'gradient': 'from-yellow-50 to-orange-50',
        'border': 'border-yellow-200',
    },
    'content/insights/relaxation-tech.md': {
        'title': 'Relaxation Tech',
        'description': 'Help your horse maintain calm composure during competitions and challenging situations.',
        'emoji': '😌',
        'gradient': 'from-red-50 to-pink-50',
        'border': 'border-red-200',
    },
    'content/insights/competition-ready.md': {
        'title': 'Competition Ready',
        'description': 'Prepare yourself and your horse for show day success with expert competition strategies.',
        'emoji': '🏆',
        'gradient': 'from-indigo-50 to-blue-50',
        'border': 'border-indigo-200',
    },
    'content/insights/advanced-techniques.md': {
        'title': 'Advanced Techniques',
        'description': 'Master complex movements and high-level training methods for professional-level riding.',
        'emoji': '🌟',
        'gradient': 'from-teal-50 to-cyan-50',
        'border': 'border-teal-200',
    },
}

for filepath, data in content_data.items():
    path = Path(filepath)
    if path.exists():
        # Read current file
        with open(path, 'r') as f:
            content = f.read()

        # Extract everything after ---
        parts = content.split('---', 2)
        body = parts[2] if len(parts) > 2 else ''

        # Build new frontmatter
        frontmatter = '---\n'
        frontmatter += f'title: "{data["title"]}"\n'

        if 'description' in data:
            frontmatter += f'description: "{data["description"]}"\n'

        if 'emoji' in data:
            frontmatter += f'emoji: "{data["emoji"]}"\n'

        if 'gradient' in data:
            frontmatter += f'gradient: "{data["gradient"]}"\n'

        if 'border' in data:
            frontmatter += f'border: "{data["border"]}"\n'

        if 'highlights' in data:
            highlights = '["' + '", "'.join(data['highlights']) + '"]'
            frontmatter += f'highlights: {highlights}\n'

        frontmatter += '---\n'

        # Write back
        with open(path, 'w') as f:
            f.write(frontmatter + body)

        print(f'Fixed: {filepath}')

print('Done!')

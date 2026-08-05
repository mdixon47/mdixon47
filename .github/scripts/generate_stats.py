#!/usr/bin/env python3

"""
GitHub Stats Generator
Generates SVG badges and metrics from GitHub API
Stores results in stats/ directory
"""

import json
import os
import requests
from datetime import datetime
from pathlib import Path

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USER = 'mdixon47'
API_URL = 'https://api.github.com'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

stats_dir = Path('stats')
stats_dir.mkdir(exist_ok=True)


def get_user_stats():
    """Fetch user profile statistics"""
    print(f"Fetching user stats for {GITHUB_USER}...")
    response = requests.get(
        f'{API_URL}/users/{GITHUB_USER}',
        headers=headers
    )
    response.raise_for_status()
    return response.json()


def get_repo_stats():
    """Fetch all repositories"""
    print(f"Fetching repositories for {GITHUB_USER}...")
    repos = []
    page = 1
    while True:
        response = requests.get(
            f'{API_URL}/users/{GITHUB_USER}/repos',
            headers=headers,
            params={
                'type': 'owner',
                'sort': 'updated',
                'per_page': 100,
                'page': page
            }
        )
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos


def get_contributions_this_year():
    """Get contribution count for the current year using GraphQL"""
    print("Fetching contributions for current year...")
    query = """
    query {
      viewer {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
      }
    }
    """
    response = requests.post(
        f'{API_URL}/graphql',
        json={'query': query},
        headers=headers
    )
    response.raise_for_status()
    data = response.json()
    if 'data' in data and data['data']:
        return data['data']['viewer']['contributionsCollection']['contributionCalendar']['totalContributions']
    return 0


def generate_svg_badge(label, value, color='#0366d6'):
    """Generate a simple SVG badge"""
    label_width = len(label) * 7 + 10
    value_width = len(str(value)) * 7 + 10
    total_width = label_width + value_width
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="20">
  <rect width="{label_width}" height="20" fill="#555"/>
  <rect x="{label_width}" width="{value_width}" height="20" fill="{color}"/>
  <text x="{label_width/2}" y="15" font-size="12" font-weight="bold" fill="white" text-anchor="middle">{label}</text>
  <text x="{label_width + value_width/2}" y="15" font-size="12" font-weight="bold" fill="white" text-anchor="middle">{value}</text>
</svg>'''
    return svg


def save_badge(name, svg_content):
    """Save SVG badge to file"""
    filepath = stats_dir / f'{name}.svg'
    with open(filepath, 'w') as f:
        f.write(svg_content)
    print(f"Created {filepath}")


def generate_all_stats():
    """Generate all stats and badges"""
    user_stats = get_user_stats()
    repos = get_repo_stats()
    contributions = get_contributions_this_year()
    
    # Calculate stats
    followers = user_stats.get('followers', 0)
    public_repos = user_stats.get('public_repos', 0)
    total_stars = sum(repo.get('stargazers_count', 0) for repo in repos)
    total_forks = sum(repo.get('forks_count', 0) for repo in repos)
    
    # Generate SVG badges
    print("\nGenerating SVG badges...")
    save_badge('followers', generate_svg_badge('Followers', followers, '#0366d6'))
    save_badge('repos', generate_svg_badge('Repositories', public_repos, '#28a745'))
    save_badge('stars', generate_svg_badge('Total Stars', total_stars, '#ffd700'))
    save_badge('forks', generate_svg_badge('Total Forks', total_forks, '#6f42c1'))
    save_badge('contributions', generate_svg_badge('Contributions', contributions, '#ff6b6b'))
    
    # Generate JSON stats file
    print("\nGenerating JSON stats file...")
    stats_json = {
        'generated_at': datetime.now().isoformat(),
        'user': GITHUB_USER,
        'followers': followers,
        'repositories': public_repos,
        'total_stars': total_stars,
        'total_forks': total_forks,
        'contributions_this_year': contributions,
        'top_repositories': [
            {
                'name': repo['name'],
                'url': repo['html_url'],
                'description': repo['description'],
                'stars': repo['stargazers_count'],
                'forks': repo['forks_count'],
                'language': repo['language']
            }
            for repo in sorted(repos, key=lambda x: x['stargazers_count'], reverse=True)[:5]
        ]
    }
    
    stats_file = stats_dir / 'stats.json'
    with open(stats_file, 'w') as f:
        json.dump(stats_json, f, indent=2)
    print(f"Created {stats_file}")
    
    print("\n✅ Stats generation complete!")
    print(f"  Followers: {followers}")
    print(f"  Repositories: {public_repos}")
    print(f"  Total Stars: {total_stars}")
    print(f"  Total Forks: {total_forks}")
    print(f"  Contributions (this year): {contributions}")


if __name__ == '__main__':
    try:
        generate_all_stats()
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

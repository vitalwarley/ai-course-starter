"""Starter stub for Task 01 – Technology Extraction.

Complete `extract_tech` so that it returns a **set** of lower‑case technology
strings found in the input text.
You may import spaCy or regex as needed.

Example:
    >>> extract_tech("Backend role: Python/Django with PostgreSQL")
    {'python', 'django', 'postgresql'}
"""
from typing import Set
import re

TECH_KEYWORDS = {
    # Programming languages
    'python', 'java', 'javascript', 'typescript', 'c', 'c++', 'c#', 'go', 'ruby', 'php', 'scala', 'swift', 'kotlin', 'rust', 'perl', 'r', 'objective-c', 'matlab', 'lua', 'haskell', 'clojure', 'elixir', 'dart', 'julia',
    # Frameworks & libraries
    'django', 'flask', 'fastapi', 'spring', 'rails', 'react', 'angular', 'vue', 'svelte', 'ember', 'backbone', 'express', 'next.js', 'nuxt', 'redux', 'graphql', 'pytorch', 'tensorflow', 'keras', 'jupyter', 'node.js', 'electron', 'nestjs', 'symfony', 'laravel', 'cakephp', 'phoenix', 'dotnet', '.net', 'asp.net', 'blazor', 'gatsby', 'webpack', 'babel', 'tailwind', 'bootstrap', 'jquery', 'd3', 'three.js', 'selenium', 'openai', 'opencv', 'grpc', 'protobuf',
    # Databases
    'postgresql', 'postgres', 'mysql', 'sqlite', 'mongodb', 'redis', 'cassandra', 'dynamodb', 'aurora', 'cockroachdb', 'elasticsearch', 'bigquery', 'snowflake', 'oracle', 'mariadb', 'neo4j', 'influxdb', 'timescaledb', 'clickhouse', 'firestore', 'supabase', 'solr', 'memcached', 'hbase', 'db2',
    # Cloud & platforms
    'aws', 'gcp', 'azure', 'heroku', 'firebase', 'cloudflare', 'openstack', 'digitalocean', 'lambda', 'fargate', 'kubernetes', 'docker', 'vagrant', 'terraform', 'ansible', 'puppet', 'chef', 'jenkins', 'github', 'gitlab', 'bitbucket', 's3', 'ec2', 'rds', 'sns', 'sqs', 'cloudformation', 'cloudfront', 'datadog', 'prometheus', 'grafana', 'airflow', 'kafka', 'rabbitmq', 'sidekiq', 'celery', 'metabase', 'spinnaker', 'nomad', 'openai', 'gcp', 'gae', 'bigquery', 'cloud',
}

# Add aliases and normalize
ALIASES = {
    'node': 'node.js', 'js': 'javascript', 'py': 'python', 'postgres': 'postgresql', 'postgre': 'postgresql', 'tf': 'tensorflow', 'ts': 'typescript', 'vuejs': 'vue', 'reactjs': 'react', 'aws': 'aws', 'gcp': 'gcp', 'google cloud': 'gcp', 'ms sql': 'sql', 'sql server': 'sql', 'mongo': 'mongodb', 'pgsql': 'postgresql', 'docker-compose': 'docker', 'dotnet': '.net', 'aspnet': 'asp.net', 's3': 's3', 'ec2': 'ec2', 'rds': 'rds', 'sns': 'sns', 'sqs': 'sqs', 'gae': 'gae', 'cloud': 'cloud',
}

# Create comprehensive regex pattern
ALL_TERMS = list(TECH_KEYWORDS) + list(ALIASES.keys())
ALL_TERMS.sort(key=lambda x: -len(x))  # Longer first to avoid partial matches
pattern = re.compile(r'\b(' + '|'.join(re.escape(term) for term in ALL_TERMS) + r')\b', re.IGNORECASE)

def extract_tech(text: str) -> Set[str]:
    """Return a set of technology tokens mentioned in `text`. Uses regex pattern matching."""
    found = set()
    
    # Use regex to find all technology terms
    for match in pattern.findall(text):
        norm = match.lower()
        if norm in ALIASES:
            norm = ALIASES[norm]
        if norm in TECH_KEYWORDS:
            found.add(norm)

    return found

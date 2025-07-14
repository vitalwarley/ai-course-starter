"""Starter stub for Task 01 – Technology Extraction.

Complete `extract_tech` so that it returns a **set** of lower‑case technology
strings found in the input text.
You may import spaCy or regex as needed.

Example:
    >>> extract_tech("Backend role: Python/Django with PostgreSQL")
    {'python', 'django', 'postgresql'}
"""
from typing import Set
import spacy

# Load spaCy model (using small English model)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback if model is not installed
    nlp = None

def extract_tech(text: str) -> Set[str]:
    """Return a set of technology tokens mentioned in `text`."""
    
    # Comprehensive list of technology terms
    tech_terms = {
        # Programming Languages
        'python', 'java', 'javascript', 'typescript', 'c', 'c++', 'csharp', 'c#',
        'php', 'ruby', 'go', 'rust', 'swift', 'kotlin', 'scala', 'r', 'matlab',
        'perl', 'lua', 'haskell', 'clojure', 'erlang', 'elixir', 'dart', 'julia',
        'cobol', 'fortran', 'assembly', 'bash', 'powershell', 'sql', 'html', 'css',
        
        # Web Frameworks & Libraries
        'react', 'angular', 'vue', 'vuejs', 'django', 'flask', 'fastapi', 'express',
        'expressjs', 'nodejs', 'node', 'spring', 'springboot', 'laravel', 'symfony',
        'rails', 'rubyonrails', 'asp.net', 'aspnet', 'blazor', 'nextjs', 'nuxtjs',
        'gatsby', 'svelte', 'backbone', 'ember', 'jquery', 'bootstrap', 'tailwind',
        'materialize', 'bulma', 'foundation', 'semantic', 'redux', 'mobx', 'rxjs',
        
        # Backend & API
        'graphql', 'rest', 'restful', 'grpc', 'soap', 'websocket', 'socketio',
        'fastify', 'koa', 'hapi', 'nestjs', 'strapi', 'sanity', 'contentful',
        
        # Databases
        'mysql', 'postgresql', 'postgres', 'sqlite', 'mongodb', 'redis', 'cassandra',
        'dynamodb', 'elasticsearch', 'solr', 'neo4j', 'couchdb', 'influxdb',
        'mariadb', 'oracle', 'sqlserver', 'firestore', 'supabase', 'planetscale',
        
        # Cloud Platforms
        'aws', 'azure', 'gcp', 'googlecloud', 'heroku', 'vercel', 'netlify',
        'digitalocean', 'linode', 'vultr', 'cloudflare', 'firebase', 'amplify',
        
        # DevOps & Infrastructure
        'docker', 'kubernetes', 'k8s', 'terraform', 'ansible', 'puppet', 'chef',
        'jenkins', 'circleci', 'travis', 'gitlab', 'github', 'bitbucket', 'vagrant',
        'helm', 'istio', 'prometheus', 'grafana', 'elk', 'logstash', 'kibana',
        'nagios', 'zabbix', 'datadog', 'newrelic', 'sentry',
        
        # Machine Learning & AI
        'tensorflow', 'pytorch', 'keras', 'scikit-learn', 'sklearn', 'pandas',
        'numpy', 'matplotlib', 'seaborn', 'jupyter', 'anaconda', 'opencv',
        'nltk', 'spacy', 'huggingface', 'transformers', 'bert', 'gpt',
        
        # Mobile Development
        'android', 'ios', 'reactnative', 'flutter', 'xamarin', 'ionic', 'cordova',
        'phonegap', 'nativescript', 'expo',
        
        # Testing
        'jest', 'mocha', 'chai', 'cypress', 'selenium', 'pytest', 'unittest',
        'junit', 'testng', 'rspec', 'jasmine', 'karma', 'protractor',
        
        # Build Tools & Package Managers
        'webpack', 'vite', 'parcel', 'rollup', 'gulp', 'grunt', 'npm', 'yarn',
        'pnpm', 'pip', 'conda', 'maven', 'gradle', 'sbt', 'leiningen',
        
        # Version Control
        'git', 'svn', 'mercurial',
        
        # Other Tools & Technologies
        'elasticsearch', 'apache', 'nginx', 'tomcat', 'iis', 'rabbitmq', 'kafka',
        'spark', 'hadoop', 'airflow', 'celery', 'sidekiq', 'resque', 'bull',
        'socket.io', 'webrtc', 'graphql', 'openapi', 'swagger', 'postman',
        'insomnia', 'figma', 'sketch', 'adobe', 'photoshop', 'illustrator',
        'xd', 'invision', 'zeplin', 'slack', 'discord', 'teams', 'zoom',
    }
    
    # Convert text to lowercase for case-insensitive matching
    text_lower = text.lower()
    
    # Find all technology terms mentioned in the text
    found_techs = set()
    
    # Use spaCy NER to identify potential technology entities
    if nlp:
        doc = nlp(text)
        for ent in doc.ents:
            ent_text = ent.text.lower()
            
            # Check if the entity is in our tech terms list
            if ent_text in tech_terms:
                found_techs.add(ent_text)
            
            # Also check for entities that might be technologies (ORG, PRODUCT, etc.)
            # and see if they match our tech terms
            if ent.label_ in ['ORG', 'PRODUCT', 'WORK_OF_ART', 'EVENT']:
                # Clean the entity text and check against tech terms
                cleaned_ent = ent_text.replace('.', '').replace('-', '').replace('_', '').strip()
                if cleaned_ent in tech_terms:
                    found_techs.add(cleaned_ent)
                
                # Also check individual words in multi-word entities
                for word in cleaned_ent.split():
                    if word in tech_terms:
                        found_techs.add(word)
    
    # Also check for technology terms directly in the text using simple string matching
    # This provides a fallback when spaCy is not available
    for tech in tech_terms:
        if tech in text_lower:
            # Simple word boundary check to avoid partial matches
            if (text_lower.find(tech) == 0 or not text_lower[text_lower.find(tech) - 1].isalnum()) and \
               (text_lower.find(tech) + len(tech) == len(text_lower) or not text_lower[text_lower.find(tech) + len(tech)].isalnum()):
                found_techs.add(tech)
    
    # Handle some special cases and variations
    special_cases = {
        'node.js': 'nodejs',
        'node js': 'nodejs',
        'react.js': 'react',
        'vue.js': 'vue',
        'angular.js': 'angular',
        'express.js': 'express',
        'next.js': 'nextjs',
        'nuxt.js': 'nuxtjs',
        'ruby on rails': 'rails',
        'asp.net': 'aspnet',
        'c#': 'csharp',
        'c++': 'c++',
        'google cloud': 'gcp',
        'google cloud platform': 'gcp',
        'amazon web services': 'aws',
        'microsoft azure': 'azure',
        'sql server': 'sqlserver',
        'scikit-learn': 'sklearn',
        'scikit learn': 'sklearn',
        'socket.io': 'socketio',
    }
    
    for phrase, tech in special_cases.items():
        if phrase in text_lower:
            if tech in tech_terms:
                found_techs.add(tech)
    
    return found_techs

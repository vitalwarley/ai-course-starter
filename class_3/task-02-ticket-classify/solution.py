"""Starter stub for Task 02 – Ticket classification."""

from typing import Literal, TypedDict, Tuple
import re
import spacy

Priority = Literal["low", "medium", "high"]
Category = Literal["bug", "question", "feature"]

class Entities(TypedDict):
    user: str
    os: str
    version: str

# Load spaCy model (use small model for efficiency)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # If model not found, use blank model
    nlp = spacy.blank("en")

def extract_entities(text: str) -> Entities:
    """Return extracted entities from ticket body."""
    
    # Initialize default values
    entities: Entities = {
        "user": "",
        "os": "",
        "version": ""
    }
    
    # Convert to lowercase for pattern matching
    text_lower = text.lower()
    
    # Extract user (look for patterns like "User: bob", "user bob", etc.)
    user_patterns = [
        r'user[:\s]+(\w+)',
        r'reported by[:\s]+(\w+)',
        r'from[:\s]+(\w+)',
        r'by[:\s]+(\w+)',
        r'-[:\s]*user[:\s]+(\w+)',
        r'user[:\s]*:[:\s]*(\w+)',
    ]
    
    for pattern in user_patterns:
        match = re.search(pattern, text_lower)
        if match:
            entities["user"] = match.group(1)
            break
    
    # If no user found in structured format, try to extract from common patterns
    if not entities["user"]:
        # Look for common names in the text
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                entities["user"] = ent.text.lower()
                break
    
    # Extract OS (look for operating system patterns)
    os_patterns = [
        r'os[:\s]+([^\s,]+(?:\s+[^\s,]+)*)',
        r'operating system[:\s]+([^\s,]+(?:\s+[^\s,]+)*)',
        r'platform[:\s]+([^\s,]+(?:\s+[^\s,]+)*)',
        r'-[:\s]*os[:\s]+([^\s,]+(?:\s+[^\s,]+)*)',
        r'os[:\s]*:[:\s]*([^\s,]+(?:\s+[^\s,]+)*)',
    ]
    
    for pattern in os_patterns:
        match = re.search(pattern, text_lower)
        if match:
            os_text = match.group(1).strip()
            # Clean up common OS name variations
            if 'ubuntu' in os_text:
                entities["os"] = os_text
            elif 'windows' in os_text:
                entities["os"] = os_text
            elif 'macos' in os_text or 'mac os' in os_text:
                entities["os"] = os_text
            elif 'linux' in os_text:
                entities["os"] = os_text
            else:
                entities["os"] = os_text
            break
    
    # Extract version (look for version patterns)
    version_patterns = [
        r'version[:\s]+([v]?[\d\.]+[^\s,]*)',
        r'ver[:\s]+([v]?[\d\.]+[^\s,]*)',
        r'v[:\s]*([v]?[\d\.]+[^\s,]*)',
        r'-[:\s]*version[:\s]+([v]?[\d\.]+[^\s,]*)',
        r'version[:\s]*:[:\s]*([v]?[\d\.]+[^\s,]*)',
    ]
    
    for pattern in version_patterns:
        match = re.search(pattern, text_lower)
        if match:
            version_text = match.group(1).strip()
            # Ensure version starts with 'v' if it's just numbers
            if not version_text.startswith('v') and re.match(r'^\d', version_text):
                version_text = 'v' + version_text
            entities["version"] = version_text
            break
    
    return entities

def classify(text: str) -> Tuple[Priority, Category]:
    """Return (priority, category) for the ticket body."""
    
    text_lower = text.lower()
    
    # Priority classification based on urgency indicators
    priority = "medium"  # default
    
    # High priority indicators
    high_priority_words = [
        'critical', 'urgent', 'emergency', 'blocking', 'crash', 'down', 'broken',
        'not working', 'failed', 'error', 'exception', 'bug', 'issue', 'problem',
        'serious', 'major', 'severe', 'important', 'asap', 'immediately', 'now',
        'production', 'live', 'outage', 'unavailable', 'cannot', 'can\'t', 'unable',
        'stuck', 'freeze', 'hang', 'stop', 'fail'
    ]
    
    # Low priority indicators
    low_priority_words = [
        'question', 'how', 'what', 'when', 'where', 'why', 'can i', 'is there',
        'would like', 'could you', 'please', 'help', 'suggestion', 'idea',
        'enhancement', 'improvement', 'feature', 'nice to have', 'eventually',
        'minor', 'small', 'trivial', 'cosmetic', 'aesthetic'
    ]
    
    # Check for high priority
    for word in high_priority_words:
        if word in text_lower:
            priority = "high"
            break
    
    # Check for low priority (only if not already high)
    if priority != "high":
        for word in low_priority_words:
            if word in text_lower:
                priority = "low"
                break
    
    # Category classification
    category = "question"  # default
    
    # Bug indicators
    bug_words = [
        'crash', 'error', 'exception', 'bug', 'broken', 'not working', 'fail',
        'problem', 'issue', 'wrong', 'incorrect', 'unexpected', 'freeze',
        'hang', 'stop', 'stuck', 'glitch', 'malfunction', 'defect'
    ]
    
    # Question indicators
    question_words = [
        'how', 'what', 'when', 'where', 'why', 'can i', 'is there', 'does',
        'will', 'would', 'could', 'should', 'help', 'explain', 'understand',
        'know', 'learn', 'question', 'ask', 'tell me', 'show me'
    ]
    
    # Feature indicators
    feature_words = [
        'feature', 'add', 'new', 'request', 'enhancement', 'improvement',
        'suggest', 'idea', 'would like', 'can you', 'please implement',
        'support', 'include', 'integrate', 'develop', 'create', 'build',
        'make', 'allow', 'enable', 'provide'
    ]
    
    # Check for bug
    for word in bug_words:
        if word in text_lower:
            category = "bug"
            break
    
    # Check for feature (only if not already bug)
    if category != "bug":
        for word in feature_words:
            if word in text_lower:
                category = "feature"
                break
    
    # Questions often start with question words or contain question marks
    if category == "question" or '?' in text or any(text_lower.startswith(word) for word in ['how', 'what', 'when', 'where', 'why', 'can', 'is', 'does', 'will', 'would', 'could', 'should']):
        category = "question"
    
    return (priority, category)

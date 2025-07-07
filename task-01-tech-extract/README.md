# Task 01 – Technology Extraction from Job Postings

Implement `extract_tech(text)` in **`solution.py`** so that it returns a Python `set`
containing every unique *technology term* (programming language, framework,
database, or cloud) mentioned in `text`.

You may use **spaCy**, **regex**, or any pure‑Python logic.  
The grader will evaluate **macro‑averaged F1** against a hidden gold set.
Your score must be ≥ 0.70 to pass.

*Run locally*

```bash
pip install -r ../../requirements.txt
python - << 'PY'
from solution import extract_tech
print(extract_tech("We need a React & TypeScript engineer familiar with AWS."))
PY
```

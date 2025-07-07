# Task 02 – Support Ticket Entity Extraction & Classification

1. **Entity extraction**  
   Implement `extract_entities(text)` so that it returns a dictionary
   `{'user': ..., 'os': ..., 'version': ...}`.

2. **Priority & category**  
   Implement `classify(text)` so that it returns a pair  
   `(<priority>, <category>)` where:

   * `priority` ∈ {`low`, `medium`, `high`}
   * `category` ∈ {`bug`, `question`, `feature`}

The grader will check:
* entity macro‑F1 ≥ 0.85
* joint accuracy (priority + category) ≥ 0.80

Feel free to use rules, spaCy, or an external LLM (expensive for you but allowed).

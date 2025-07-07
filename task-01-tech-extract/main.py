import json
from solution import extract_tech

if __name__ == "__main__":
    with open("jobposts_sample.jsonl", "r", encoding="utf-8") as f:
        for line in f:
            obj = json.loads(line)
            text = obj.get("text", "")
            techs = extract_tech(text)
            print(f"Text: {text}\nExtracted tech: {techs}\n") 
"""Starter stub for Task 02 – Ticket classification."""

from typing import Literal, TypedDict, Tuple

Priority = Literal["low", "medium", "high"]
Category = Literal["bug", "question", "feature"]

class Entities(TypedDict):
    user: str
    os: str
    version: str

def extract_entities(text: str) -> Entities:
    """Return extracted entities from ticket body."""
    # TODO: implement
    return Entities(user="", os="", version="")

def classify(text: str) -> Tuple[Priority, Category]:
    """Return (priority, category) for the ticket body."""
    # TODO: implement
    return ("low", "bug")
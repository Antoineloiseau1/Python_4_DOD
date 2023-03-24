import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate an id made of 15 random ascii letters in lower case"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """class student"""
    name: str = field(metadata={"required": True})
    surname: str = field(metadata={"required": True})
    active: bool = True
    login: str = "Eagle"
    id: str = generate_id()

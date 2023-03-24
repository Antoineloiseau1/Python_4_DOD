import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate an id made of 15 random ascii letters in lower case"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """class student"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = True
    login: str = field(init=False)
    id: str = field(default=generate_id(), init=False)

    def __post_init__(self):
        self.login = self.surname.capitalize()

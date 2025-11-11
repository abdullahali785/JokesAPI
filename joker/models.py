#!/usr/bin/env python3

"""
Jokes API Model

@author: Abdullah
@version: 2025.11
""" 
from dataclasses import dataclass

@dataclass
class Joke:
    language: str
    category: str
    text: str

    def to_dict(self):
        return {"language": self.language, "category": self.category, "text": self.text}
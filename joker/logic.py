#!/usr/bin/env python3

"""
Jokes API Logic

@author: Abdullah
@version: 2025.11
""" 
import random, pyjokes, pathlib, tomllib
from functools import cache
from flask import current_app
from .models import Joke

class Joker:
    dataset = []
    languages = []
    categories = ["any", "neutral", "chuck"]

    @classmethod
    def init_dataset(cls):
        base_dir = pathlib.Path(__file__).parent.parent
        config_path = base_dir / "config.toml"

        with open(config_path, "rb") as f:
            config = tomllib.load(f)

        cls.languages = sorted(config["LANGUAGES"].keys())
        cls.dataset = []

        for lang in cls.languages:
            try:
                neutral = pyjokes.get_jokes(lang, "neutral")
                for text in neutral:
                    cls.dataset.append(Joke(lang, "neutral", text))
            except:
                #print(f"{lang} has no neutral jokes")
                pass

            try:
                chuck = pyjokes.get_jokes(lang, "chuck")
                for text in chuck:
                    cls.dataset.append(Joke(lang, "chuck", text))
            except:
                #print(f"{lang} has no chuck jokes")
                pass

    @classmethod
    @cache
    def get_jokes(cls, language="any", category="any", number=0):
        if language != "any" and language not in cls.languages:
            raise ValueError(f"Language {language} does not exist")

        if category not in cls.categories:
            raise ValueError(f"Category {category} does not exist")

        filtered = []
        for joke in cls.dataset:
            if (language == "any" or joke.language == language) and \
               (category == "any" or joke.category == category):
                filtered.append(joke)

        if not filtered:
            return []
        
        if number == 0 or number >= len(filtered):
            return filtered

        return random.sample(filtered, number)

    @classmethod
    def get_the_joke(cls, id):
        if id < 0 or id >= len(cls.dataset):
            raise ValueError(f"Joke {id} not found, try an id between 0 and 952")

        return cls.dataset[id]
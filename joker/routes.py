#!/usr/bin/env python3

"""
Jokes API Routes

@author: Abdullah
@version: 2025.11
""" 
from flask import Blueprint, jsonify
jokes_bp = Blueprint("jokes", __name__)
from .logic import Joker

main = Blueprint("main", __name__, url_prefix="/api/v1")
joker = Joker()

# GET /api/v1/jokes/<id>
@main.get("/jokes/<int:id>")
def getJokeByID(id: int):
    try:
        joke = joker.get_the_joke(id)
        return jsonify({
            "joke": {"text": joke.text}
        })
    except:
        return jsonify({"error": "Invalid ID"}), 404

# GET /api/v1/jokes/<language>/<category>/<number>
@main.get("/jokes/<language>/<category>/<number>")
def getJokes(language, category, number):
    if number == "all":
        num = 0
    else:
        num = int(number)

    try:
        jokes = joker.get_jokes(language, category, num)
        return jsonify({"jokes": [j.text for j in jokes]})
    except:
        return jsonify({"error": "Invalid inputs"}), 404
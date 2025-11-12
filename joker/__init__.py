#!/usr/bin/env python3

"""
Jokes API Initialization

@author: Abdullah
@version: 2025.11
""" 
import tomllib, pathlib
from flask import Flask
from flask_cors import CORS
from pathlib import Path

def create_app() -> Flask:
    from .logic import Joker
    from .routes import main

    this_app = Flask(__name__)
    CORS(this_app, resources={r"/*": {"origins": "*"}})

    BASE_DIR = pathlib.Path(__file__).parent.parent
    CONFIG_PATH = BASE_DIR / pathlib.Path("config.toml")
    
    try:
        with open(CONFIG_PATH, "rb") as f:
            config = tomllib.load(f)
    except:
        print("config.toml not found!")
        return

    this_app.config["LANGUAGES"] = config["LANGUAGES"]

    with this_app.app_context():
        Joker.init_dataset()
    
    this_app.register_blueprint(main, url_prefix="/api/v1")

    return this_app 
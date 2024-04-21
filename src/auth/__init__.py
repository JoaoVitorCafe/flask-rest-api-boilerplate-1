from flask import Blueprint

bp = Blueprint("/", __name__)

from auth import routes
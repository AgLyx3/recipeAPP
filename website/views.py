"""
Filename:
    views.py
"""
import os
import requests
from flask import Blueprint, render_template, request

# Create a blueprint
main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the index page.
    """
   
    return render_template('index.html')

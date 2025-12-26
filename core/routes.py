from flask import Blueprint, render_template, request, redirect, url_for
import os
# We create a Blueprint (a modular slice of the app)
dashboard_bp = Blueprint('dashboard', __name__)

# We will inject dependencies later, or initialize them here if strict singleton
# For now, we will import the config to access paths
from .config import Config
config = Config()

@dashboard_bp.route('/')
def index():
    """Lists current files in the content directory."""
    files = []
    if os.path.exists(config.CONTENT_DIR):
        files = [f for f in os.listdir(config.CONTENT_DIR) if f.endswith('.md')]
    return render_template('dashboard.html', files=files)

@dashboard_bp.route('/editor')
def editor():
    return render_template('editor.html')
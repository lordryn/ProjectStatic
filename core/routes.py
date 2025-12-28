from flask import Blueprint, render_template, request, redirect, url_for, send_from_directory # <--- Add send_from_directoryimport os
from .config import Config
import os

config = Config()
# We create a Blueprint (a modular slice of the app)
dashboard_bp = Blueprint('dashboard', __name__)

# We will inject dependencies later, or initialize them here if strict singleton
# For now, we will import the config to access paths
from .config import Config
config = Config()

@dashboard_bp.route('/delete/<filename>', methods=['POST'])
def delete_post(filename):
    file_path = os.path.join(config.CONTENT_DIR, filename)
    # Security check to prevent deleting files outside the directory
    if os.path.exists(file_path) and filename.endswith('.md') and '..' not in filename:
        os.remove(file_path)
        # We will add flash messaging here in Phase 3
    return redirect(url_for('dashboard.index'))
@dashboard_bp.route('/')
def index():
    """Lists current files in the content directory."""
    files = []
    if os.path.exists(config.CONTENT_DIR):
        files = [f for f in os.listdir(config.CONTENT_DIR) if f.endswith('.md')]
    return render_template('dashboard.html', files=files, config=config)

@dashboard_bp.route('/editor')
def editor():
    return render_template('editor.html')

# --- NEW ROUTE: Serve the Built Site ---
@dashboard_bp.route('/public/<path:filename>')
def serve_output(filename):
    """
    Serves the static site files from the configured OUTPUT_DIR.
    This allows 'Preview' links to work without a separate web server.
    """
    return send_from_directory(config.OUTPUT_DIR, filename)
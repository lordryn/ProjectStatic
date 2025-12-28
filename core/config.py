import os
from dotenv import load_dotenv  # <--- CRITICAL: Loads your .env file

load_dotenv()


class Config:
    def __init__(self):
        # 1. Get the path of THIS file (.../Project/core/config.py)
        current_file_path = os.path.abspath(__file__)

        # 2. Get the directory containing this file (.../Project/core)
        core_dir = os.path.dirname(current_file_path)

        # 3. Go up ONE level to get the actual Project Root (.../Project)
        self.BASE_DIR = os.path.dirname(core_dir)

        # 4. Now all paths will correctly point to the root folders
        self.CONTENT_DIR = os.path.join(self.BASE_DIR, 'content', 'posts')
        self.STATIC_DIR = os.path.join(self.BASE_DIR, 'content', 'static')
        self.TEMPLATE_DIR = os.path.join(self.BASE_DIR, 'templates')

        # Safety Check: Ensure input dirs exist
        self._ensure_dir(self.CONTENT_DIR)
        self._ensure_dir(self.TEMPLATE_DIR)

        # --- OUTPUT CONFIGURATION ---

        # Force absolute path for default public folder to avoid confusion
        default_output = os.path.join(self.BASE_DIR, 'public')

        # Load from Environment or use default
        self.OUTPUT_DIR = os.environ.get('PROJECT_OUTPUT_DIR', default_output)

        # CRITICAL FIX: Create the output directory immediately so the server doesn't 404
        self._ensure_dir(self.OUTPUT_DIR)

        # URL Base (for the dashboard buttons)
        self.LIVE_URL = os.environ.get('PROJECT_LIVE_URL', '/public')

        # Secret Key
        self.SECRET_KEY = os.environ.get('FLASK_SECRET_KEY', 'dev-key-123')

    def _ensure_dir(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError:
                pass  # Directory likely exists
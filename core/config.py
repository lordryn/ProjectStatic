import os


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
        self.OUTPUT_DIR = os.path.join(self.BASE_DIR, 'public')

        # Safety Check: Ensure dirs exist so we don't crash
        self._ensure_dir(self.CONTENT_DIR)
        self._ensure_dir(self.TEMPLATE_DIR)

    def _ensure_dir(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError:
                pass  # Directory likely exists
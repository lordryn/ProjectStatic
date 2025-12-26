import os


class MarkdownGenerator:
    def __init__(self, config):
        self.content_dir = config.CONTENT_DIR

    def create_file(self, filename, title, summary, content):
        """Creates a formatted markdown file."""
        if not filename.endswith('.md'):
            filename += '.md'

        filepath = os.path.join(self.content_dir, filename)

        # Enforce the strict Line 1/Line 3 format
        raw_text = f"# {title}\n\n{summary}\n\n{content}"

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(raw_text)

        return filepath
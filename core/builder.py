import os
import shutil
import markdown
import datetime


class SiteBuilder:
    def __init__(self, config):
        """Initialize with a Config object."""
        self.config = config
        self.posts = []

    def clean_output(self):
        """Wipes the public directory."""
        if os.path.exists(self.config.OUTPUT_DIR):
            shutil.rmtree(self.config.OUTPUT_DIR)
        os.makedirs(self.config.OUTPUT_DIR)
        os.makedirs(os.path.join(self.config.OUTPUT_DIR, 'posts'))
        print("[BUILDER] Cleaned public directory.")

    def copy_assets(self):
        """Copies static assets."""
        if os.path.exists(self.config.STATIC_DIR):
            dest = os.path.join(self.config.OUTPUT_DIR, 'static')
            shutil.copytree(self.config.STATIC_DIR, dest)
            print("[BUILDER] Assets copied.")

    def scan_posts(self):
        """Scans content dir and parses metadata."""
        self.posts = []  # Reset
        files = [f for f in os.listdir(self.config.CONTENT_DIR) if f.endswith('.md')]

        for filename in files:
            filepath = os.path.join(self.config.CONTENT_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            # Simple Metadata Extraction
            lines = text.split('\n')
            title = lines[0].replace('#', '').strip()
            summary = lines[2] if len(lines) > 2 else "Read more..."

            # Strip the first H1 for HTML rendering to avoid redundancy
            html_content = markdown.markdown(text)

            self.posts.append({
                'title': title,
                'summary': summary,
                'slug': filename.replace('.md', '.html'),
                'content': html_content,
                'date': datetime.datetime.now().strftime('%Y-%m-%d')
            })
        print(f"[BUILDER] Scanned {len(self.posts)} posts.")

    def build_all(self):
        """Orchestrates the full build process."""
        self.clean_output()
        self.copy_assets()
        self.scan_posts()

        # Load Templates (FIX: Added encoding='utf-8')
        with open(os.path.join(self.config.TEMPLATE_DIR, 'post_template.html'), 'r', encoding='utf-8') as f:
            post_template = f.read()

        with open(os.path.join(self.config.TEMPLATE_DIR, 'index_template.html'), 'r', encoding='utf-8') as f:
            index_template = f.read()

        # Generate Individual Pages
        for post in self.posts:
            final_html = post_template.replace('{{ TITLE }}', post['title']) \
                .replace('{{ CONTENT }}', post['content']) \
                .replace('PUBLISHED_DATE', post['date'])

            out_path = os.path.join(self.config.OUTPUT_DIR, 'posts', post['slug'])
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(final_html)

        # Generate Index
        cards_html = ""
        for post in self.posts:
            cards_html += f"""
            <div class="card">
                <h3>{post['title']}</h3>
                <p>{post['summary']}</p>
                <a href="posts/{post['slug']}" class="button">Read Log</a>
            </div>
            """

        final_index = index_template.replace('{{ POSTS_GRID }}', cards_html)
        with open(os.path.join(self.config.OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(final_index)

        return True
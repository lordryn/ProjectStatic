import os
import datetime
import markdown
import shutil

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, 'content', 'posts')
STATIC_DIR = os.path.join(BASE_DIR, 'content', 'static')  # New source for images/css
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, 'public')


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def clean_build():
    """Wipes the public directory to prevent ghost files."""
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
        print("[CLEAN] Wiped public directory.")
    ensure_dir(OUTPUT_DIR)


def copy_static_assets():
    """Copies images/css from content/static to public/static"""
    if os.path.exists(STATIC_DIR):
        output_static = os.path.join(OUTPUT_DIR, 'static')
        shutil.copytree(STATIC_DIR, output_static)
        print(f"[ASSETS] Copied static files to {output_static}")


def build_site():
    print("--- STARTING BUILD ---")

    # 1. CLEAN EVERYTHING
    clean_build()

    # 2. COPY STATIC ASSETS (Images, CSS)
    copy_static_assets()

    ensure_dir(os.path.join(OUTPUT_DIR, 'posts'))

    posts = []

    # 3. SCAN POSTS
    if not os.path.exists(CONTENT_DIR):
        print(f"Error: Content directory not found at {CONTENT_DIR}")
        return

    for filename in os.listdir(CONTENT_DIR):
        if filename.endswith(".md"):
            filepath = os.path.join(CONTENT_DIR, filename)

            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            html_content = markdown.markdown(text)

            lines = text.split('\n')
            title = lines[0].replace('#', '').strip()
            summary = lines[2] if len(lines) > 2 else "Read more..."
            slug = filename.replace('.md', '.html')

            posts.append({
                'title': title,
                'summary': summary,
                'link': f"posts/{slug}",
                'date': datetime.datetime.now().strftime('%Y-%m-%d')
            })

            with open(os.path.join(TEMPLATE_DIR, 'post_template.html'), 'r', encoding='utf-8') as t:
                template = t.read()

            final_html = template.replace('{{ TITLE }}', title) \
                .replace('{{ CONTENT }}', html_content) \
                .replace('PUBLISHED_DATE', posts[-1]['date'])

            with open(os.path.join(OUTPUT_DIR, 'posts', slug), 'w', encoding='utf-8') as out:
                out.write(final_html)
                print(f"[OK] Generated Post: {slug}")

    # 4. GENERATE INDEX HTML
    cards_html = ""
    for post in posts:
        cards_html += f"""
        <div class="card">
            <h3>{post['title']}</h3>
            <p>{post['summary']}</p>
            <a href="{post['link']}" class="button">Read Log</a>
        </div>
        """

    with open(os.path.join(TEMPLATE_DIR, 'index_template.html'), 'r', encoding='utf-8') as t:
        index_html = t.read()

    final_index = index_html.replace('{{ POSTS_GRID }}', cards_html)

    with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w', encoding='utf-8') as out:
        out.write(final_index)

    print("--- BUILD COMPLETE ---")


if __name__ == "__main__":
    build_site()
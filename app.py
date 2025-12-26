from flask import Flask, redirect, url_for, request
from core import Config, SiteBuilder, MarkdownGenerator, dashboard_bp

# Initialize Flask with the new template folder for the UI
app = Flask(__name__, template_folder='app_templates')

# --- INITIALIZATION ---
# We instantiate our classes once when the app starts
app_config = Config()
builder = SiteBuilder(app_config)
md_gen = MarkdownGenerator(app_config)

# Register the View Routes (The Dashboard & Editor Pages)
app.register_blueprint(dashboard_bp)


# --- ACTION ROUTES (The Buttons) ---

@app.route('/trigger_build')
def trigger_build():
    """Triggers the SiteBuilder Engine."""
    print("[APP] Build Triggered via Web")
    builder.build_all()
    # Reload the dashboard so we see the status
    return redirect(url_for('dashboard.index'))


@app.route('/save_post', methods=['POST'])
def save_post():
    """Takes data from the Editor and passes it to the Generator."""
    title = request.form.get('title')
    summary = request.form.get('summary')
    content = request.form.get('content')

    # Simple slugify for filename
    filename = title.lower().replace(' ', '_')

    md_gen.create_file(filename, title, summary, content)

    print(f"[APP] New Post Saved: {filename}")
    return redirect(url_for('dashboard.index'))


if __name__ == '__main__':
    print("--- PROJECT STATIC v2.0 ONLINE ---")
    print("Open http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
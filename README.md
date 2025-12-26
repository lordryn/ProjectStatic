# ProjectStatic: Static Site Control Node

**Date:** 2025-12-26
**Current Version:** 2.0 (Local WebApp)
**Status:** Operational / Active Development

---

## 1. System Overview (v2.0)

ProjectStatic has evolved from a simple CLI script into a modular Python Web Application. It runs locally as a control node, providing a Graphical User Interface (GUI) to manage content, trigger builds, and administrate the static site generation process.

### Key Capabilities

* **Web Interface**
  A Flask-based dashboard (`localhost:5000`) to view status and trigger actions.

* **Input Terminal**
  A dedicated GUI for writing and saving new Markdown logs without touching the file system manually.

* **Modular Engine**
  The core logic is decoupled into a robust core package, separating configuration, content generation, and building logic.

* **Atomic Builds**
  The `SiteBuilder` class completely wipes and regenerates the `public/` directory on every build to ensure zero redundancy.

---

## 2. Architecture & Modules

The project is structured as an Object-Oriented application managed by `app.py`.

### Directory Structure

```text
Project/
├── app.py              # CONTROLLER: Flask Web Server entry point
├── core/               # MODEL: Logic Package
│   ├── __init__.py     # Exposes modules to app.py
│   ├── config.py       # Centralized pathing & settings
│   ├── builder.py      # Static Site Generation Engine
│   ├── generator.py    # Markdown file creation logic
│   └── routes.py       # Flask Blueprints (Dashboard logic)
├── app_templates/      # UI: Admin Panel HTML
├── templates/          # SITE: Public site HTML templates
├── content/            # DATA: Source Markdown & static assets
└── public/             # OUTPUT: Generated live site
```

---

## 3. Workflow & Usage

### Starting the Control Node

Instead of running a script, launch the application server:

```bash
python app.py
```

Access the dashboard at:

```
http://127.0.0.1:5000
```

---

### Creating Content

1. Navigate to **+ NEW LOG ENTRY** in the dashboard.
2. Fill in the **Entry Title** and **Summary**.
3. Write the post in the **Markdown Payload** area.
4. Click **COMMIT TO STORAGE** to save the `.md` file to `content/posts/`.

---

### Building the Site

Click **EXECUTE BUILD_SEQUENCE** on the dashboard.

The `SiteBuilder` engine will:

1. Clean the `public/` directory.
2. Copy assets from `content/static/`.
3. Convert all Markdown files to HTML.
4. Inject rendered content into `templates/`.

The live site is now available in `public/`.

---

## 4. Roadmap

* **v2.1** – Live Preview (render Markdown in-browser before saving)
* **v2.5** – Drag-and-Drop Asset Management
* **v3.0** – Server Deployment Pipelines (one-click push to live)

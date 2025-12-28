# ProjectStatic: Static Site Control Node

**Current Version:** 2.1 (LAN / Staging Support)
**Status:** Operational / Active Development

---

## 1. System Overview

ProjectStatic is a modular Python Web Application designed to manage static site generation. It runs as a **Control Node**, providing a Web GUI to manage content, trigger builds, and preview the site before going live.

**v2.1 Update:** Now supports remote access via LAN and includes a built-in staging server to preview the generated HTML without an external web server.

### Key Capabilities

* **Web Dashboard** (`:5000`)
  Manage files, trigger builds, and view system status from any device on your network.

* **Staging Server**
  Instantly preview the full generated site via the **VIEW STAGED SITE** button.

* **Atomic Builds**
  The `SiteBuilder` engine wipes and regenerates the output directory on every build to ensure zero redundancy.

* **Environment Config**
  Paths and secrets are managed via `.env` files, making it safe to deploy on different servers.

---

## 2. Installation & Setup

### Prerequisites

* Python 3.x
* `pip`

### 2.1 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2.2 Configuration (.env)

Create a `.env` file in the project root:

```ini
# Path to where the HTML files should be generated
PROJECT_OUTPUT_DIR=C:/Path/To/Your/Public/Folder

# Secret key for session security (Flash messages)
FLASK_SECRET_KEY=change-this-to-something-random

# Base URL for the Staging Preview (usually /public)
PROJECT_LIVE_URL=/public
```

### 2.3 Run the Control Node

```bash
python app.py
```

Access the dashboard at:
`http://localhost:5000` (or your machine's IP address).

---

## 3. Workflow

* **Create**
  Use the **+ NEW LOG ENTRY** button to write content in Markdown.

* **Manage**
  View or delete existing logs from the Dashboard list.

* **Build**
  Click **EXECUTE BUILD_SEQUENCE** to compile Markdown into HTML.

* **Preview**
  Click **VIEW STAGED SITE** to browse the generated site in a safe staging environment.

* **Deploy**
  *(External)* Sync the `PROJECT_OUTPUT_DIR` to your live web server.

---

## 4. Directory Structure

```text
Project/
├── app.py              # CONTROLLER: Flask Web Server entry point
├── .env                # CONFIG: Local environment settings (Ignored by Git)
├── requirements.txt    # DEPS: Python package list
├── core/               # MODEL: Logic Package
│   ├── builder.py      # Static Site Generation Engine
│   ├── config.py       # Configuration Loader
│   ├── generator.py    # File creation logic
│   └── routes.py       # Flask Routing & Logic
├── content/            # DATA: Source Markdown & static assets
│   ├── posts/          # .md files
│   └── static/         # Images/CSS to be copied to public
└── public/             # OUTPUT: The generated website (Target of Build)
```

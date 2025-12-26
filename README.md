# ProjectStatic Site Generator: Project Status & Roadmap

**Date:** 2025-12-26
**Current Version:** 1.0 (CLI Builder)
**Status:** Production Ready / Pre-Deployment

---

## 1. Current Architecture (v1.0)
The current system is a lightweight, Python-based Static Site Generator (SSG). It is designed to run locally, generating a complete HTML structure that is ready to be pushed to a live web server.

### Core Features
* **Markdown to HTML:** Converts `.md` files from `content/posts/` into clean HTML.
* **Templating Engine:** Uses string replacement to inject content into `index_template.html` and `post_template.html`.
* **Dynamic Indexing:** Automatically scans all posts and generates a card-based grid on the homepage.
* **Clean Build Logic:** Wipes the `public/` directory on every run to prevent "ghost files" and redundancy.
* **Asset Management:** Automatically copies `content/static/` (images/css) to the public build folder.

### Directory Structure
```text
Project/
├── build.py                  # The logic core (Script)
├── content/
│   ├── posts/                # Markdown source files
│   └── static/               # Images/CSS (Copied verbatim)
├── templates/
│   ├── index_template.html   # Homepage layout with {{ POSTS_GRID }}
│   └── post_template.html    # Single post layout with {{ CONTENT }}
└── public/                   # FINAL OUTPUT (Do not edit manually)

# Real-Time Supply Chain & Analytics Dashboard

A high-performance full-stack inventory and supply chain tracking system designed to manage multi-location store inventory, process transactional event logs, and stream real-time stock alerts.

##  Features
* **Relational Database Architecture:** Built on a normalized PostgreSQL schema tracking multi-location store inventory, stock thresholds, and automated reorder triggers.
* **RESTful Backend:** Developed using Python and Flask with robust database connectivity (`psycopg2`) to serve dynamic JSON payloads and handle inventory operations.
* **Real-Time Event Streaming:** Integrated WebSockets to push live stock updates, transactional logs, and low-inventory alerts directly to the frontend without page reloads.
* **Modern UI:** Styled with a responsive Tailwind CSS dashboard interface for instantaneous visual monitoring of supply chain metrics.

##  Tech Stack
* **Backend:** Python, Flask, WebSockets, REST APIs
* **Database:** PostgreSQL
* **Frontend:** JavaScript, Tailwind CSS, HTML5
* **Version Control:** Git, GitHub

##  Project Structure
```text
├── backend/
│   ├── app.py              # Main Flask application & WebSocket routes
│   ├── database.py         # PostgreSQL connection & query handlers
│   └── requirements.py     # Python dependencies
├── database/
│   └── schema.sql          # Relational schema & seed data
├── frontend/
│   ├── index.html          # Dashboard UI
│   └── script.js           # WebSocket client & DOM rendering
└── README.md

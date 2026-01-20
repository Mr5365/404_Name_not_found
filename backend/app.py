from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

# Import local modules (same folder)
from identify import identify_object_local
from openai_helper import get_object_info

app = Flask(__name__)
CORS(app)

# =========================
# PATHS
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "industrial_objects.json")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =========================
# LOAD DATABASE
# =========================

with open(DB_PATH, "r") as f:
    OBJECT_DB = json.load(f)

# =========================
# SERVICE 1: OBJECT IDENTIFICATION
# =========================

@app.route("/identify/<label>", methods=["GET"])
def identify_object(label):
    # 1️⃣ Try local database
    data = OBJECT_DB.get(label)

    if data:
        return jsonify({
            "name": data["name"],
            "description": data["description"],
            "source": "local_db",
            "confidence": 0.92
        })

    # 2️⃣ Fallback to OpenAI
    object_name = label.replace("_", " ").title()
    ai_description = get_object_info(object_name)

    return jsonify({
        "name": object_name,
        "description": ai_description,
        "source": "openai",
        "confidence": 0.75
    })

# =========================
# SERVICE 2: AR INSPECTION (FRAME UPLOAD)
# =========================

@app.route("/upload", methods=["POST"])
def upload_frames():
    files = request.files.getlist("images")

    if not files:
        return jsonify({"error": "No files received"}), 400

    for f in files:
        save_path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(save_path)

    return jsonify({
        "status": "frames uploaded",
        "count": len(files)
    })

# =========================
# HEALTH CHECK (VERY USEFUL)
# =========================

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ARWork Assist backend running"})

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

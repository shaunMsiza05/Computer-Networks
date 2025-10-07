from flask import Flask, request, jsonify
import hashlib
import os
from auth import verify_signature

app = Flask(__name__)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_file(recipient_id, filename, file_data):
    recipient_folder = os.path.join(UPLOAD_DIR, recipient_id)
    os.makedirs(recipient_folder, exist_ok=True)
    file_path = os.path.join(recipient_folder, filename)
    with open(file_path, "wb") as f:
        f.write(file_data)
    return file_path

@app.route("/upload", methods=["POST"])
def upload():
    try:
        sender_id = request.form.get("sender_id")
        public_key = request.form.get("public_key")
        signature = request.form.get("signature")
        recipient_id = request.form.get("recipient_id")
        filename = request.form.get("filename")
        metadata = request.form.get("metadata", "")
        file = request.files.get("file")

        if not all([sender_id, public_key, signature, recipient_id, filename, file]):
            return jsonify({"error": "Missing required fields"}), 400

        file_data = file.read()

        hasher = hashlib.sha256()
        hasher.update(file_data)
        hasher.update(metadata.encode())
        message = hasher.digest()

        valid, reason = verify_signature(sender_id, public_key, message, signature)
        if not valid:
            return jsonify({"error": f"Signature verification failed: {reason}"}), 403

        saved_path = save_file(recipient_id, filename, file_data)

        return jsonify({"message": "Upload successful", "path": saved_path})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000)

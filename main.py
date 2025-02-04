from flask import Flask, request, jsonify
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_video():
    if "video" not in request.files:
        return jsonify({"error": "No video file provided"}), 400
    
    video = request.files["video"]
    file_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(file_path)
    
    return jsonify({"message": "Upload successful", "file_path": file_path}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


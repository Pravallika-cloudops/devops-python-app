from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello DevOps CI/CD Working 🚀"


@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# CICD TEST Sun Feb 15 17:55:52 GMTST 2026

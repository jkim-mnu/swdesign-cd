import os
from flask import Flask

app = Flask(__name__)
VERSION = "v0.1.0"
NEW_UI = os.getenv("FEATURE_NEW_UI", "off") == "on"

@app.get("/")
def home():
    page = "new page" if NEW_UI else "old page"
    return f"{VERSION} {page}\n"

@app.get("/health")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

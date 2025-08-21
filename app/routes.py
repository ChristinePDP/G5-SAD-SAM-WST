from flask import render_template
from flask import current_app as app   # ✅ FIX

@app.route("/")
def home():
    return "Hello, Flask is working!"

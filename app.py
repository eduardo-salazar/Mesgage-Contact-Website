import os
from flask import Flask, redirect, render_template, url_for, request, session, flash
from flask_assets import Environment, Bundle
from os import environ
from datetime import datetime

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')
assets = Environment(app)
bundles = {
        'home_css': Bundle(
            'styles/main.scss',
            filters='libsass', output='gen/main.css', depends='/**/*.scss'
        )
    }
assets.register(bundles)

@app.route('/')
def home():
    return render_template('home.html',now=datetime.utcnow())

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
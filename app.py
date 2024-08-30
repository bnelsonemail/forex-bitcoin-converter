from flask import Flask, render_template, redirect, request, session, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension
from config import logger, DevelopmentConfig # or ProductionConfig, TestingConfig
from dotenv import load_dotenv, find_dotenv
import os


# load environment variables from the .env file
load_dotenv(find_dotenv())

app = Flask(__name__)

# Call config files
app.config.from_object(DevelopmentConfig)

debug = DebugToolbarExtension(app)

@app.route('/') # Home Page
def home():
    return render_template ('home.html')

@app.route('/tables')
def currency_code_table():
    """Renders an HTML page to locate currency codes"""
    return render_template('tables.html')

@app.route('/convert')
def currency_convert():
    """Renders the webpage that converts the currency to the latest Bitcoin value"""
    return render_template('convert.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
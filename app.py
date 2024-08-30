from flask import Flask, render_template, redirect, request, session, make_response, flash
from flask_debugtoolbar import DebugToolbarExtension
from config import logger, DevelopmentConfig # or ProductionConfig, TestingConfig
from dotenv import load_dotenv, find_dotenv
from forex import forex_BTC
import os



# load environment variables from the .env file
load_dotenv(find_dotenv())

app = Flask(__name__)

# Call config files
app.config.from_object(DevelopmentConfig)
app.config['DEBUG'] = 'DEBUG_TB_INTERCEPT_REDIRECTS = True'
debug = DebugToolbarExtension(app)

@app.route('/') # Home Page
def home():
    return render_template ('home.html')

@app.route('/tables')
def currency_code_table():
    """Renders an HTML page to locate currency codes"""
    return render_template('tables.html')

@app.route('/convert', methods=['POST'])
def currency_convert_post():
    """Renders the webpage that converts the currency to the latest Bitcoin value"""
    if request.method == 'POST':
        # Retrieve the value of the desired currency
        currency = request.form.get('currency')
        logger.debug(f'Form data received for the desired currency: {currency}')
        
        # Perform calculation from script
        result = forex_BTC(currency)
        
        return render_template('convert.html', result = result)
    


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
from flask import Flask, render_template
import json 

app = Flask(__name__)

home_message = ("Did you know sharks only attack you when your wet?")

@app.route("/")
def home():
    return render_template('home.html', message=home_message)

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
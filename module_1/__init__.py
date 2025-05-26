from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates')

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contacts")
def contacts():
    return render_template('contacts.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

if __name__=="__init__":
    app.run(host="0.0.0.0", port=8000, debug=True)
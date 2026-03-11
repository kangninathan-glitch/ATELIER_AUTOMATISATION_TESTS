from flask import Flask, jsonify, render_template
from tester.runner import run_tests

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Atelier automatisation des tests d'API</h1>
    <p><a href="/run">Lancer un run</a></p>
    <p><a href="/dashboard">Voir le dashboard</a></p>
    """

@app.route("/run")
def run():
    results = run_tests()
    return jsonify(results)

@app.route("/dashboard")
def dashboard():
    results = run_tests()
    return render_template("dashboard.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)

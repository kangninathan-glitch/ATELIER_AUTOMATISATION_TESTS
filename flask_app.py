from flask import Flask, jsonify, render_template
from tester.runner import run_tests
from storage import init_db, save_run, list_runs

app = Flask(__name__)

# Initialiser la base SQLite au démarrage
init_db()

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

    # Sauvegarder le run dans SQLite
    save_run(results)

    return jsonify(results)

@app.route("/dashboard")
def dashboard():

    runs = list_runs()

    return render_template(
        "dashboard.html",
        runs=runs
    )

if __name__ == "__main__":
    app.run()

from flask import Flask, jsonify, render_template
from tester.runner import run_tests
from storage import init_db, save_run, list_runs

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Atelier API Monitoring</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, Helvetica, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .box {
                max-width: 800px;
                width: 100%;
                background: rgba(15, 23, 42, 0.78);
                border: 1px solid rgba(148, 163, 184, 0.15);
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.25);
            }
            h1 {
                margin-top: 0;
                font-size: 2.2rem;
            }
            p {
                color: #cbd5e1;
                line-height: 1.6;
            }
            .buttons {
                margin-top: 30px;
                display: flex;
                gap: 15px;
                flex-wrap: wrap;
            }
            a {
                text-decoration: none;
                color: white;
                background: linear-gradient(135deg, #2563eb, #3b82f6);
                padding: 12px 18px;
                border-radius: 12px;
                font-weight: bold;
                box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35);
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Atelier automatisation des tests d’API</h1>
            <p>Application Flask de monitoring d’API publique avec exécution de tests, calcul d’indicateurs QoS et historique des runs enregistrés en SQLite.</p>
            <div class="buttons">
                <a href="/run">Lancer un run</a>
                <a href="/dashboard">Voir le dashboard</a>
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/run")
def run():
    results = run_tests()
    save_run(results)
    return jsonify(results)

@app.route("/dashboard")
def dashboard():
    runs = list_runs()
    return render_template("dashboard.html", runs=runs)

if __name__ == "__main__":
    app.run()

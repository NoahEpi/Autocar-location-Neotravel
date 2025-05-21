import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Dossier de stockage des messages
MESSAGE_DIR = "messages_data"
os.makedirs(MESSAGE_DIR, exist_ok=True)


def charger_messages(groupe):
    chemin = os.path.join(MESSAGE_DIR, f"groupe_{groupe}.json")
    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder_message(groupe, auteur, message):
    chemin = os.path.join(MESSAGE_DIR, f"groupe_{groupe}.json")
    messages = charger_messages(groupe)
    messages.append({"auteur": auteur, "message": message})
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


@app.route('/')
def client():
    data = {
        "role": "client",
        "kpi": {"devis": 2, "voyages": 1},
        "trajets": [
            {"date": "23/05/25", "heure": "09:00", "depart": "Mérignac", "arrivee": "Lyon", "statut": "Confirmée"},
            {"date": "01/06/26", "heure": "09:00", "depart": "Lyon", "arrivee": "Bordeaux", "statut": "En attente"},
            {"date": "05/06/25", "heure": "09:00", "depart": "Bordeaux", "arrivee": "Futuroscope", "statut": "Annulée"},
        ],
        "messages": [
            {"auteur": "John Doe", "texte": "merci pour votre réponse, nous po"},
            {"auteur": "Alain Tairieur", "texte": "Le paiement a été reçu"},
        ],
        "documents": ["Devis-0425.pdf", "Facture-0224.pdf"]
    }
    return render_template('dashboard.html', data=data)

@app.route('/autocariste')
def autocariste():
    data = {
        "role": "autocariste",
        "kpi": {"missions": 5, "acceptation": "87%", "realisees": 32, "revenus": "3,2k€"},
        "trajets": [
            {"date": "23/05/25", "heure": "09:00", "depart": "Mérignac", "arrivee": "Lyon", "statut": "Confirmée"},
            {"date": "01/06/26", "heure": "09:00", "depart": "Lyon", "arrivee": "Bordeaux", "statut": "En attente"},
            {"date": "05/06/25", "heure": "09:00", "depart": "Bordeaux", "arrivee": "Futuroscope", "statut": "Annulée"},
        ],
        "documents": ["FeuilleRoute-0525.pdf", "Facture-Mission-0224.pdf"],
        "messages": [
            {"auteur": "Dispatch", "texte": "Merci d’avoir confirmé votre mission"},
            {"auteur": "Admin", "texte": "Votre feuille de route est disponible"}
        ]
    }
    return render_template('dashboard.html', data=data)
@app.route('/messagerie')
def messagerie():
    index = int(request.args.get("groupe", 0))
    messages = charger_messages(index)
    groupes = [
        {"nom": "🚍 Groupe Futuroscope"},
        {"nom": "🎓 Lycée Voltaire"}
    ]
    data = {
        "role": "client",
        "nom_utilisateur": "Client",
        "groupes": groupes,
        "groupe_actif": index,
        "conversation": messages
    }
    return render_template("messagerie.html", data=data)
@app.route('/messagerie-autocariste')
def messagerie_autocariste():
    index = int(request.args.get("groupe", 0))
    messages = charger_messages(index)
    groupes = [
        {"nom": "🚍 Groupe Futuroscope"},
        {"nom": "🎓 Lycée Voltaire"}
    ]
    data = {
        "role": "autocariste",
        "nom_utilisateur": "Autocariste",
        "groupes": groupes,
        "groupe_actif": index,
        "conversation": messages
    }
    return render_template("messagerie.html", data=data)
@app.route("/envoyer-message", methods=["POST"])
def envoyer_message():
    role = request.form["role"]
    auteur = request.form["auteur"]
    groupe = request.form["groupe"]
    message = request.form["message"]

    sauvegarder_message(groupe, auteur, message)

    return redirect(url_for("messagerie_autocariste" if role == "autocariste" else "messagerie", groupe=groupe))
@app.route('/trajets')
def trajets():
    trajets = [
        {"date": "23/05/25", "heure": "09:00", "depart": "Mérignac", "arrivee": "Lyon","duree": "6h45", "statut": "Confirmée","prix": 580,"autocariste": "Autocar Sud"},
        {"date": "01/06/26", "heure": "09:00", "depart": "Lyon", "arrivee": "Bordeaux","duree": "6h", "statut": "En attente","prix": 620,"autocariste": ""},
        {"date": "05/06/25", "heure": "09:00", "depart": "Bordeaux", "arrivee": "Futuroscope","duree": "2h", "statut": "Annulée","prix": 180,"autocariste": ""},
        {"date": "14/06/25", "heure": "07:45", "depart": "Toulouse", "arrivee": "Carcassonne", "duree": "1h45", "statut": "Confirmée","prix": 120,"autocariste": ""},
        {"date": "15/07/25", "heure": "08:30", "depart": "Montpellier", "arrivee": "Avignon", "duree": "2h10", "statut": "En attente","prix": 140,"autocariste": ""}
    ]
    return render_template('trajets.html', trajets=trajets )
@app.route('/statistiques')
def statistiques():
    role = 'autocariste' 
    return render_template('statistiques.html',role=role)
@app.route('/parametres')
def parametres():
    role = request.args.get("role", "client")

    utilisateur = {
        "nom": "Jean Dupont",
        "email": "jean.dupont@email.com"
    }

    if role == "autocariste":
        entreprise = {
            "nom": "Autocar Sud",
            "siret": "123 456 789 00017",
            "tel": "05 55 55 55 55",
            "iban": "FR76 3000 6000 0112 3456 7890 189",
            "horaires": "Lun–Ven : 08h00–18h00"
        }
        return render_template(
            "parametres.html",
            role=role,
            utilisateur=utilisateur,
            entreprise=entreprise
        )
    else:
        paiement = {
            "type": "cb",
            "numero": "•••• •••• •••• 1234",
            "expiration": "2026-08"
        }
        return render_template(
            "parametres.html",
            role=role,
            utilisateur=utilisateur,
            paiement=paiement
        )
@app.route('/documents')
def documents():
    role = request.args.get("role", "client")
    folder = f"static/documents/{role}"

    categories = {
        "devis": [],
        "factures": [],
        "feuilles_de_route": [],
        "conditions": []
    }

    try:
        fichiers = [
            f for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))
        ]
    except FileNotFoundError:
        fichiers = []

    for fichier in fichiers:
        nom = fichier.lower()
        if "devis" in nom:
            categories["devis"].append(fichier)
        elif "facture" in nom:
            categories["factures"].append(fichier)
        elif "feuille" in nom or "route" in nom:
            categories["feuilles_de_route"].append(fichier)
        elif "condition" in nom or "mission" in nom:
            categories["conditions"].append(fichier)
    return render_template("documents.html", role=role, fichiers=categories)
@app.route('/upload', methods=['POST'])
def upload_file():
    role = request.form.get("role", "client")
    file = request.files.get("file")
    type_doc = request.form.get("type", "autres")

    # Dossier de destination
    path = f"static/documents/{role}"
    os.makedirs(path, exist_ok=True)

    # Enregistrement du fichier
    if file:
        filepath = os.path.join(path, file.filename)
        file.save(filepath)
        return "Upload réussi", 200
    return "Aucun fichier reçu", 400

if __name__ == '__main__':
    app.run(debug=True)

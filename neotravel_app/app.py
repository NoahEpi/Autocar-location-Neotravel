from flask import Flask, render_template

app = Flask(__name__)

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
    data = {
        "role": "client",  # ou "autocariste" selon le contexte utilisateur
        "conversation": [
            {"auteur": "Client", "message": "Bonjour, pouvez-vous confirmer l'heure de départ du 5 juin ?"},
            {"auteur": "Autocariste", "message": "Oui, départ prévu à 9h00 depuis Bordeaux comme indiqué dans la feuille de route."},
            {"auteur": "Client", "message": "Merci ! On prévoit une arrivée vers midi ?"},
            {"auteur": "Autocariste", "message": "Exactement, arrivée estimée à 11h50 au Futuroscope."},
            {"auteur": "System", "message": "📎 Feuille de route.pdf ajoutée"}
        ]
    }
    return render_template('messagerie.html', data=data)
@app.route('/messagerie-autocariste')
def messagerie_autocariste():
    data = {
        "role": "autocariste",
        "conversation": [
            {"auteur": "Client", "message": "Bonjour, pouvez-vous nous envoyer la feuille de route ?"},
            {"auteur": "Autocariste", "message": "Oui, elle est disponible dans votre espace documents."},
            {"auteur": "Client", "message": "Parfait, merci pour la réactivité."},
            {"auteur": "Autocariste", "message": "Avec plaisir, départ confirmé pour 9h."},
            {"auteur": "System", "message": "📎 Feuille de route.pdf ajoutée"}
        ]
    }
    return render_template('messagerie.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)

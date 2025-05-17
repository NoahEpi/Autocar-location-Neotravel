from flask import Flask, render_template, request

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
    groupes = [
        {
            "nom": "🚍 Groupe Futuroscope",
            "messages": [
                {"auteur": "Client", "message": "Bonjour, pouvez-vous confirmer l’heure de départ ?"},
                {"auteur": "Autocariste", "message": "Oui, 9h00 au collège. Retour prévu vers 18h."},
                {"auteur": "Client", "message": "Parfait, merci pour votre efficacité !"},
                {"auteur": "System", "message": "📎 Feuille de route ajoutée."}
            ]
        },
        {
            "nom": "🎓 Lycée Voltaire",
            "messages": [
                {"auteur": "Client", "message": "Bonjour"},
                {"auteur": "Autocariste", "message": "Bonjour, je vous écoute."}
            ]
        }
    ]
    index = int(request.args.get("groupe", 0))
    data = {
        "role": "client",  
        "nom_utilisateur": "Client",  # pour comparaison fiable
        "groupes": groupes,
        "groupe_actif": index,
        "conversation": groupes[index]["messages"]
    }
    return render_template("messagerie.html", data=data)
@app.route('/messagerie-autocariste')
def messagerie_autocariste():
    groupes = [
        {
            "nom": "🚍 Groupe Futuroscope",
            "messages": [
                {"auteur": "Client", "message": "Bonjour, pouvez-vous confirmer l’heure de départ ?"},
                {"auteur": "Autocariste", "message": "Oui, 9h00 au collège. Retour prévu vers 18h."},
                {"auteur": "Client", "message": "Parfait, merci pour votre efficacité !"},
                {"auteur": "System", "message": "📎 Feuille de route ajoutée."}
            ]
        },
        {
            "nom": "🎓 Lycée Voltaire",
            "messages": [
                {"auteur": "Client", "message": "Bonjour"},
                {"auteur": "Autocariste", "message": "Bonjour, je vous écoute."}
            ]
        }
    ]
    index = int(request.args.get("groupe", 0))
    data = {
        "role": "autocariste",
        "nom_utilisateur": "Autocariste",
        "groupes": groupes,
        "groupe_actif": index,
        "conversation": groupes[index]["messages"]
    }
    return render_template("messagerie.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)

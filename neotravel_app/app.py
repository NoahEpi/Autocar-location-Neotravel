from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def accueil():
    data = {
        "devis": [
            {"date": "22/04/2024", "ref": "Q-9876", "statut": "à valider", "montant": "4.200 €"},
            {"date": "5/02/2025", "ref": "Q-9876", "statut": "accepté", "montant": "750 €"},
            {"date": "12/03/2024", "ref": "M-8962", "statut": "refusé", "montant": "-"},
        ],
        "voyages": [
            {"date": "5/02/2024", "depart": "Ecole primaire -", "arrivee": "Futuroscope", "duree": "2h37m", "ref": "Q-9876"},
            {"date": "12/02/2024", "depart": "Poitiers", "arrivee": "Ecole primaire", "duree": "34m", "ref": "Q-9876"},
        ],
        "messages": [
            {"auteur": "John Doe", "texte": "merci pour votre réponse"},
            {"auteur": "Alain Tairieur", "texte": "Le paiement a été reçu"},
            {"auteur": "Gilles Jeaune", "texte": "Bonjour, désolé mais je ne pou"},
            {"auteur": "Nordine Hateur", "texte": "Bonjour, besoin pour le 14 mai"},
        ],
        "documents": ["Devis-0425.pdf", "Facture-0224.pdf"]
    }
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
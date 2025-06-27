import csv
from reservation import Reservation

class Hotel:
    def __init__(self):
        self.chambres = []
        self.clients = []
        self.reservations = []

    def ajouter_client(self, client):
        self.clients.append(client)

    def ajouter_chambre(self, chambre):
        self.chambres.append(chambre)

    def reserver(self, client, chambre, nb_nuits, saison):
        reservation = Reservation(client, chambre, nb_nuits, saison)
        reservation.confirmer()
        self.reservations.append(reservation)
        reservation.sauvegarder()
        return reservation

    def charger_reservations(self, filename="reservations.csv"):
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                client_id, chambre_num, nb_nuits, saison = row
                client = next((c for c in self.clients if str(c.id) == client_id), None)
                chambre = next((ch for ch in self.chambres if str(ch._numero) == chambre_num), None)
                if not client:
                    print(f"Client avec id {client_id} non trouvé.")
                if not chambre:
                    print(f"Chambre avec numéro {chambre_num} non trouvée.") 
                if client and chambre:
                    # Vérifie si la réservation existe déjà
                    existe = any(
                        r.client == client and r.chambre == chambre and r.nb_nuits == int(nb_nuits) and r.saison == saison
                        for r in self.reservations
                    )
                    if not existe:
                        reservation = Reservation(client, chambre, int(nb_nuits), saison)
                        self.reservations.append(reservation)
                        chambre.marquer_indisponible()
                        print(f"Réservation chargée pour {client.nom} dans la chambre {chambre._numero}")
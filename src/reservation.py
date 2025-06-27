from exceptions import ChambreNonDisponibleException
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os


from abc import ABC, abstractmethod
import csv

class Facturable(ABC):
    @abstractmethod
    def generer_facture(self):
        pass

class Reservation(Facturable):
    def __init__(self, client, chambre, nb_nuits, saison):
        self.client = client
        self.chambre = chambre
        self.nb_nuits = nb_nuits
        self.saison = saison

    def confirmer(self):
        if not self.chambre.est_disponible():
            raise ChambreNonDisponibleException("Chambre déjà réservée")
        self.chambre.marquer_indisponible()

    def generer_facture(self):
        montant = self.chambre.calculer_prix(self.nb_nuits, self.saison)
        return f"Facture pour {self.client.nom}: {montant}€"

    def sauvegarder(self, filename="reservations.csv"):
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.client.id, self.chambre._numero, self.nb_nuits, self.saison])
        print(f"Réservation sauvegardée pour {self.client.nom} dans la chambre {self.chambre._numero}")

    
    def generer_facture_pdf(self, dossier="factures"):
        if not os.path.exists(dossier):
            os.makedirs(dossier)
        filename = f"{dossier}/facture_{self.client.id}_{self.chambre._numero}.pdf"
        montant = self.chambre.calculer_prix(self.nb_nuits, self.saison)
        c = canvas.Canvas(filename, pagesize=A4)
    
        # Titre centré et en gras
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(300, 800, "FACTURE HÔTEL")
    
        # Ligne de séparation
        c.setLineWidth(1)
        c.line(50, 790, 550, 790)
    
        # Date
        c.setFont("Helvetica", 10)
        c.drawString(400, 780, f"Date : {datetime.now().strftime('%d/%m/%Y')}")
    
        # Infos client et réservation
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, f"Client : {self.client.nom}")
        c.drawString(100, 730, f"Chambre : {self.chambre._numero} ({self.chambre._type})")
        c.drawString(100, 710, f"Nombre de nuits : {self.nb_nuits}")
        c.drawString(100, 690, f"Saison : {self.saison}")
    
        # Montant total en plus grand
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 650, f"Montant total : {montant} €")
    
        c.save()
        return filename
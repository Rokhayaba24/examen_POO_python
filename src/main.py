from client import Client
from chambre import ChambreStandard, ChambreLuxueuse
from hotel import Hotel
from exceptions import ChambreNonDisponibleException

def main():
    # Création de l'hôtel
    hotel = Hotel()

    # Création de clients
    client1 = Client(1, "rokhaya", "rokhaya@gmail.com")
    client2 = Client(2, "maman", "maman@gmail.com")
    client3 = Client(3, "doudou", "doudou@gmail.com")
    client4 = Client(4, "youyou", "youyou@gmail.com")
    hotel.ajouter_client(client1)
    hotel.ajouter_client(client2)
    hotel.ajouter_client(client3)
    hotel.ajouter_client(client4)

    # Création de chambres
    chambre1 = ChambreStandard(101, 300)
    chambre3 = ChambreStandard(102, 350)
    chambre2 = ChambreLuxueuse(201, 500)
    chambre4 = ChambreLuxueuse(202, 600)
    hotel.ajouter_chambre(chambre1)
    hotel.ajouter_chambre(chambre2)
    hotel.ajouter_chambre(chambre3)
    hotel.ajouter_chambre(chambre4)

    # Présentation des clients
    client1.presentation()
    client2.presentation()
    client3.presentation()
    client4.presentation()

    # Réservation normale
    try:
        reservation1 = hotel.reserver(client1, chambre1, 2, "haute")
        print(reservation1.generer_facture())
        pdf_path = reservation1.generer_facture_pdf()
        print(f"Facture PDF générée : {pdf_path}")
    except ChambreNonDisponibleException as e:
        print("Erreur :", e)

    try:
        reservation4 = hotel.reserver(client3, chambre4, 5, "haute")
        print(reservation4.generer_facture())
        pdf_path = reservation4.generer_facture_pdf()
        print(f"Facture PDF générée : {pdf_path}")
    except ChambreNonDisponibleException as e:
        print("Erreur :", e)
   
    

    # Tentative de double réservation sur la même chambre
    try:
        reservation2 = hotel.reserver(client2, chambre1, 1, "basse")
        print(reservation2.generer_facture())
        pdf_path = reservation2.generer_facture_pdf()
        print(f"Facture PDF générée : {pdf_path}")
    except ChambreNonDisponibleException as e:
        print("Erreur :", e)

    # Réservation sur une autre chambre
    try:
        reservation3 = hotel.reserver(client2, chambre2, 3, "basse")
        print(reservation3.generer_facture())
        pdf_path = reservation3.generer_facture_pdf()
        print(f"Facture PDF générée : {pdf_path}")
    except ChambreNonDisponibleException as e:
        print("Erreur :", e)

    # Lecture des réservations depuis le CSV
    print("\nChargement des réservations depuis le fichier CSV :")
    hotel.charger_reservations()

if __name__ == "__main__":
    main()
import unittest
from client import Client
from chambre import ChambreStandard, ChambreLuxueuse
from hotel import Hotel
from exceptions import ChambreNonDisponibleException

class TestHotelBookingPro(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()
        self.client = Client(1, "Test", "test@mail.com")
        self.hotel.ajouter_client(self.client)
        self.chambre_std = ChambreStandard(101, 100)
        self.chambre_lux = ChambreLuxueuse(201, 200)
        self.hotel.ajouter_chambre(self.chambre_std)
        self.hotel.ajouter_chambre(self.chambre_lux)

    def test_reservation_normale(self):
        reservation = self.hotel.reserver(self.client, self.chambre_std, 2, "haute")
        self.assertFalse(self.chambre_std.est_disponible())
        self.assertIn(reservation, self.hotel.reservations)

    def test_double_reservation(self):
        self.hotel.reserver(self.client, self.chambre_std, 2, "haute")
        with self.assertRaises(ChambreNonDisponibleException):
            self.hotel.reserver(self.client, self.chambre_std, 1, "basse")

    def test_reservation_luxueuse(self):
        reservation = self.hotel.reserver(self.client, self.chambre_lux, 1, "basse")
        montant = self.chambre_lux.calculer_prix(1, "basse")
        self.assertEqual(montant, 250)

if __name__ == '__main__':
    unittest.main()
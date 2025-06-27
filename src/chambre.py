from abc import ABC, abstractmethod

class Chambre(ABC):
    def __init__(self, numero, type_chambre, prix_base):
        self._numero = numero
        self._type = type_chambre
        self._prix_base = prix_base
        self._est_disponible = True

    def est_disponible(self):
        return self._est_disponible

    def marquer_indisponible(self):
        self._est_disponible = False

    def marquer_disponible(self):
        self._est_disponible = True

    @abstractmethod
    def calculer_prix(self, nb_nuits, saison):
        pass

class ChambreStandard(Chambre):
    def __init__(self, numero, prix_base):
        super().__init__(numero, "standard", prix_base)

    def calculer_prix(self, nb_nuits, saison):
        prix = self._prix_base
        if saison == "haute":
            prix *= 1.2
        return prix * nb_nuits

class ServiceSpa:
    def spa(self):
        return "Accès spa inclus"

class ChambreLuxueuse(Chambre, ServiceSpa):
    def __init__(self, numero, prix_base):
        super().__init__(numero, "luxueuse", prix_base)

    def calculer_prix(self, nb_nuits, saison):
        prix = self._prix_base + 50
        if saison == "haute":
            prix *= 1.2
        return prix * nb_nuits
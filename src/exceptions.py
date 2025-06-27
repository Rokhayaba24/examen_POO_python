class ChambreNonDisponibleException(Exception):
    def __init__(self, message="La chambre n'est pas disponible."):
        super().__init__(message)
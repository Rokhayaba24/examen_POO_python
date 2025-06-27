class Client:
    def __init__(self, id, nom, email):
        self.id = id
        self.nom = nom
        self.email = email

    def presentation(self):
        print(f"Client {self.id} : {self.nom} ({self.email})")
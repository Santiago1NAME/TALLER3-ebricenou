from boa import BoaConstrictor
from huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [BoaConstrictor(), BoaConstrictor()]
        self.hurones = [Huron(), Huron()]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.alimentar()
            return "Éxito"
        except ValueError:
            return "La boa está llena"

if __name__ == "__main__":
    guarderia = Guarderia()

    # Alimentamos la primera boa varias veces
    print(guarderia.alimentar_boa(guarderia.boas[0]))
    for _ in range(9):
        print(guarderia.alimentar_boa(guarderia.boas[0]))

    print(guarderia.alimentar_boa(guarderia.boas[0]))
    print(guarderia.alimentar_boa(None))
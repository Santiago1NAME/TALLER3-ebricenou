class BoaConstrictor:
    def __init__(self):
        self.ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def calcular_flete(self, impuestos, peso):
        return round(impuestos * peso, 2)

    def alimentar(self):
        if self.ratones_comidos >= 20:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1
        return "Boa alimentada"
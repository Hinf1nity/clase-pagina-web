class animal():
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def hablar(self):
        print("El animal hace ruido")

    def tipo(self):
        print(f'El tipo de animal es {self.tipo}')


class perro(animal):
    def __init__(self):
        pass

    def hablar(self):
        print("El perro ladra")


perro = perro('Firulais', 'perro')
perro.hablar()

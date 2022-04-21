class Pilha:
    def __init__(self):
        self._vet = []

    def peek5(self):
        print(self)
        contador = -1
        while contador != -6:
            try:
                paciente = self._vet[contador]
                print(paciente[2].nome)
                contador = contador -1
            except IndexError:
                break
        pass
       
    def push(self, item):
        return self._vet.append(item)
    
if __name__ == '__main__':


    class Inmueble():
        __altura = 0
        __anchura = 0
        __profundidad = 0
        __peso = 0

        def __init__(self, altura, anchura, profundidad, peso):
            self.__altura = altura
            self.__anchura = anchura
            self.__profundidad = profundidad
            self.__peso = peso

        @property
        def altura(self):
            return self.__altura

        @altura.setter
        def altura(self, altura):
            self.__altura = altura

        @property
        def anchura(self):
            return self.__anchura

        @anchura.setter
        def anchura(self, anchura):
            self.__anchura = anchura

        @property
        def profundidad(self):
            return self.__profundidad

        @profundidad.setter
        def profundidad(self, profundidad):
            self.__profundidad = profundidad

        @property
        def peso(self):
            return self.__peso

        @peso.setter
        def peso(self, peso):
            self.__peso = peso

        def __str__(self):
            return "Altura: {} \nAnchura: {} \nProfundidad: {} \nPeso: {}".format(
                self.__altura, self.__anchura, self.__profundidad, self.__peso)


    class Silla(Inmueble):
        __patas = 0
        __respaldo = False

        def __init__(self, altura, anchura, profundidad, peso, patas, respaldo):
            Inmueble.__init__(self, altura, anchura, profundidad, peso)
            self.__patas = patas
            self.__respaldo = respaldo

        @property
        def patas(self):
            return self.__patas

        @patas.setter
        def patas(self, patas):
            self.__patas = patas

        @property
        def respaldo(self):
            return self.__respaldo

        @respaldo.setter
        def respaldo(self, respaldo):
            self.__respaldo = respaldo

        def __str__(self):
            return Inmueble.__str__(self) + "\nPatas: {} \nRespaldo: {}".format(self.__patas, self.__respaldo)


    sofa1 = Inmueble(50, 40, 20, 100)
    print(sofa1)
    silla1 = Silla(50, 30, 20, 10, 4, True)
    print(silla1)








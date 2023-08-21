class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor (self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "blanco" or color == "negro":
            self.color = color

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro 
    
    def cambiarRegistro (self, registro):
        self.registro = registro

    def asignarTipo (self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self. registro = registro


    def cantidadAsientos (self, asientos):
        cantidadAsientos = 0
        for i in range (len(asientos)):
            if asientos[i] != None:
                cantidadAsientos +=1
        return cantidadAsientos

        


    
    def verificarIntegridad (self, registro, asientos):
        if registro == self.motor.registro:
            for e in range (len(asientos)):
                if self.asientos[e].registro != registro:
                    return "Las piezas no son originales"
                
            return "Auto original"
            
        else:
            "Las piezas no son originales"

        

                    
         

            

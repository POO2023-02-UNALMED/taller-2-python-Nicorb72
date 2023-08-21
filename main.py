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
    def __init__(self, motor, asientos, registro, modelo, precio):
        self.motor = motor
        self.asientos = asientos
        self. registro = registro
        self.modelo = modelo
        self.precio = precio



    def cantidadAsientos (self, asientos):
        for asientos in asientos:
            cantidadAsientos = cantidadAsientos+1

    
    def verificarIntegridad (self, registro):
        if self.motor.registro == registro:
            for asientos in asientos:
                if self.asientos.registro != registro:
                    return "Las piezas no son originales"
                
            return "Auto original"
            
        else:
            "Las piezas no son originales"

        

                    
         

            

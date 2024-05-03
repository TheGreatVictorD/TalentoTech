"""
Supongamos que tenemos una clase Motor y una clase Coche. El coche depende del
motor para funcionar, pero el motor puede ser reemplazado o actualizado sin
afectar directamente al coche. La dependencia en este caso radica en el hecho
de que el coche usa el motor para su funcionamiento, pero no tiene una relación
de "tener" o "contener" como en las asociaciones.
"""


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

    def arrancar(self):
        print("Motor arrancado")


class Coche:
    def __init__(self, marca, motor):
        self.marca = marca
        self.motor = motor  # Dependencia del motor

    def encender(self):
        self.motor.arrancar()
        print(f"{self.marca} encendido")


# Crear un motor inicial
motor_coche = Motor("Gasolina")

# Crear un coche que depende del motor inicial
mi_coche = Coche("Toyota", motor_coche)

# Encender el coche inicial
mi_coche.encender()

# Crear un nuevo motor
nuevo_motor = Motor("Eléctrico")

# Cambiar el motor del coche por el nuevo motor
mi_coche.motor = nuevo_motor

# Encender el coche con el nuevo motor
mi_coche.encender()


"""
En este ejemplo, la clase Coche tiene una dependencia de la clase Motor. El coche utiliza el 
motor para arrancar y funcionar (self.motor.arrancar() en el método encender). Sin embargo, 
el coche no posee el motor ni tiene una relación de composición o agregación con él; simplemente 
depende de él para su funcionamiento.

Puedes notar que el motor se pasa como un argumento al inicializar un objeto Coche. Esto muestra la 
dependencia del coche en el motor. Si el motor cambia o se actualiza, el coche seguirá funcionando 
siempre y cuando el nuevo motor también tenga un método arrancar.

# El motor del coche se puede actualizar o cambiar simplemente asignando un nuevo objeto Motor al 
atributo motor del coche. Esto demuestra la flexibilidad y la independencia de la dependencia del 
coche en relación con el motor.
"""
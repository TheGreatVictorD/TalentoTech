"""
En este ejemplo, la clase Conductor tiene una dependencia con la clase Coche. Esto se debe a que
Conductor utiliza a Coche en su método conducir(). Esto significa que Conductor no puede funcionar
sin Coche, y si Coche cambia (por ejemplo, si cambias el atributo marca), entonces Conductor también
podría verse afectado.

En términos más simples, puedes pensar en la dependencia como una “relación de usa”. En este caso, un
Conductor usa un Coche.
"""


class Coche:
    def __init__(self, marca):
        self.marca = marca


class Conductor:
    def conducir(self, coche):
        print(f"Conduciendo un coche de marca {coche.marca}")


coche = Coche("Toyota")
conductor = Conductor()
conductor.conducir(coche)  # Imprime: Conduciendo un coche de marca Toyota


"""
Diferencia entre dependencia y composición:

    -Composición: Imagina que estás construyendo un coche. El coche se compone de varias partes como el motor, 
    las ruedas, los asientos, etc. Si el coche se destruye, todas sus partes (motor, ruedas, asientos) también 
    se destruyen. No puedes simplemente tomar el motor y decir que es un coche. Eso es la composición. En  
    términos de programación, un objeto de una clase (el coche) se compone de objetos de otras clases (motor, 
    ruedas, asientos).

    -Dependencia: Ahora, imagina que tienes un conductor. El conductor usa el coche para ir a algún lugar, 
    pero el conductor y el coche son entidades separadas y pueden existir independientemente. Si el coche se 
    destruye, el conductor todavía existe. El conductor depende del coche para conducir, pero no es parte del 
    coche. Eso es la dependencia. En términos de programación, un objeto de una clase (el conductor) utiliza 
    un objeto de otra clase (el coche), pero no son parte del mismo objeto.
"""
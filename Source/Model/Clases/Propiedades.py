class Propiedades:

    def __init__(self, tipo_propiedad, ubicacion, superficie, cant_ambientes, limite_ocupantes, permite_mascotas, apto_credito, tasación, precio_alquiler):
        self.tipo_propiedad = tipo_propiedad
        self.ubicacion = ubicacion
        self.superficie = superficie
        self.cant_ambientes = cant_ambientes
        self.limite_ocupantes = limite_ocupantes
        self.permite_mascotas = permite_mascotas
        self.apto_credito = apto_credito
        self.tasación = tasación
        self.precio_alquiler = precio_alquiler

    def comprarPrecio(self):
        print('Si quieres comprar esta propiedad el precio es de: ' + str(self.tasación))

    def alquilarPrecio(self):
        print('Si quieres alquilar esta propiedad el precio por mes es de: ' + str(self.precio_alquiler))


pruebaPropiedad = Propiedades('Departamento', 'Cordoba, Vila Carlos Paz', 1200, 5, 10, True, False, 60000000, 50000)


pruebaPropiedad.comprarPrecio()
pruebaPropiedad.alquilarPrecio()
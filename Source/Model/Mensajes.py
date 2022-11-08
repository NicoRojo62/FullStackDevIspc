class Mensajes:

    def __init__(self, nro_mensaje, asunto, fecha, descripcion_msj):
        self.nro_mensaje = nro_mensaje
        self.asunto = asunto
        self.fecha = fecha
        self.descripcion_msj = descripcion_msj

    def nuevoMsj(self):
        print('fecha ' + self.fecha +
         ' Asunto: ' + self.asunto + 
         ' Mensaje: ' + self.descripcion_msj)


pruebaMsj = Mensajes(1, 'Cañeria rota', '08/11/2022', 'Necesito una solución')

pruebaMsj.nuevoMsj()
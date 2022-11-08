class Cliente:

    def __init__(self, tipoCliente, fechaAlta, nYA, dni, email, telefono, domicilio):
        self.tipoCliente = tipoCliente
        self.fechaAlta = fechaAlta
        self.nYA = nYA
        self.dni = dni
        self.email = email
        self.telefono = telefono
        self.domicilio = domicilio

    def cargaComprobante(self):
        print('Usuario: ' + self.nYA +
              ' DNI: ' + str(self.dni) +
              ' pagó el monto pactado y este es su comprobante')

    def esInquilino(self):
        if self.tipoCliente == 'inquilino':
            return print('Si, es Inquilino')


miCliente1 = Cliente('comprador', '31-10-2022', 'Nico lopez', 45666888, 'dumbish@hotmail.com', 154888666, 'esquina 0')

miCliente2 = Cliente('inquilino', '1-11-2022', 'jose rojo', 42222665, 'bichssnka@hotmail.com', 154888996, 'los andes 123')


miCliente1.cargaComprobante()

miCliente2.esInquilino()

# El ultimo método solo es de prueba



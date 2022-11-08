class Admin:
    
    def __init__(self, alias, cbu, permisos):
        self.alias = alias
        self.cbu = cbu
        self.permisos = permisos

    def agregarPropiedad(self):
        print('El admin: ' + self.alias + ' puede agregar propiedades')

pruebaAdmin = Admin('lobo.oeste', 154666512488784, True)

pruebaAdmin.agregarPropiedad()
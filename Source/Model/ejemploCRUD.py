import mysql.connector

class Conectar():

    def __init__(self) -> None:    
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'contraseñabd',
                db = 'bd_administración_bienes_raices'
            )

        except mysql.connector.Error as descipcionError:
            print('¡No se conectó!', descipcionError)

# Primera operación del CRUD: INSERT

    def insertarValor(self, ID_Cliente, E_mail, Tipo_Cliente, Fecha_alta, NyA, DNI, Telefono, Domicilio):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'INSERT INTO Cliente (ID_Cliente, E_mail, Tipo_Cliente, Fecha_alta, NyA, DNI, Telefono, Domicilio) VALUES (1, "prueba@hotmail.com", "Inquilino", DATE("2022-11-03"), "Locomotora Castro", 45586752, 485962355, "los sauces");'
                data = (ID_Cliente, E_mail, Tipo_Cliente, Fecha_alta, NyA, DNI, Telefono, Domicilio)

                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print('No se pudo conectar a la base de datos')

# Segunda Operación CRUD: READ

    def traerTablaCliente(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'SELECT * FROM db_admin_bienes_raices.cliente;'

                cursor.execute(sentenciaSQL)
                resultadoTablaCliente = cursor.fetchall()
                self.conexion.close()

                return resultadoTablaCliente

            except:
                print('No se pudo conectar a la base de datos')

# Tercera operación CRUD: UPDATE


    def actualizarRegistro(self, ID_Cliente):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'UPDATE Cliente SET NyA = "Jorge Pintos" WHERE ID_Cliente = 1;'
                data = (ID_Cliente)

                cursor.execute(sentenciaSQL, data)
                self.conexion.commit()
                self.conexion.close()

            except:
                print('No se pudo conectar a la base de datos')



# Cuarta operación CRUD: DELETE

    def EliminarRegistro(self, ID_Cliente):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE FROM Cliente WHERE ID_Cliente = 1;"
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                self.conexion.close()
            
            except:
                print('No se pudo conectar a la base de datos')

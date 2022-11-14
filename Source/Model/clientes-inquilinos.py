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

    def traerInquilinos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = 'SELECT * FROM db_admin_bienes_raices.cliente WHERE Tipo_cliente LIKE "Inquilino";'

                cursor.execute(sentenciaSQL)
                resultadoInquilinos = cursor.fetchall()
                self.conexion.commit()
                self.conexion.close()

                return resultadoInquilinos

            except:
                print('No se pudo conectar a la base de datos')
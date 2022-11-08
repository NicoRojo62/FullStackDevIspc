class Operación:

    def __init__(self, nro_operacion, tipo_operacion, fecha_inicio, fecha_fin, comision, motivo_pago, total_expensas, pago_total):
        self.nro_operacion = nro_operacion
        self.tipo_operacion = tipo_operacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.comision = comision
        self.motivo_pago = motivo_pago
        self.total_expensas = total_expensas
        self.pago_total = pago_total

    def crearComprobante(self):
        print('Comprobante de operación nro: ' + str(self.nro_operacion) +
        ' Se realizó un pago total de: ' + str(self.pago_total) +
        ' con fecha: ' + self.fecha_fin +
        ' la comisión del administrador es de: ' + str(self.comision))


pruebaOperación = Operación(1, 'alquiler', '01-11-2022', '08-11-2022', 12000, 'pago alquiler', 20000, 72000)


pruebaOperación.crearComprobante()
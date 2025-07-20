from datetime import datetime

class Encuesta:
    def __init__(self, codigo=None, nombre_cliente=None, tipo_servicio=None,
                 correo=None, telefono=None, pregunta1=None, pregunta2=None, pregunta3=None,
                 fecha_registro=None):
        self.codigo = codigo
        self.nombre_cliente = nombre_cliente
        self.tipo_servicio = tipo_servicio
        self.correo = correo
        self.telefono = telefono
        self.pregunta1 = pregunta1
        self.pregunta2 = pregunta2
        self.pregunta3 = pregunta3

        if isinstance(fecha_registro, str):
            try:
                self.fecha_registro = datetime.strptime(fecha_registro, '%Y-%m-%d').date()
            except ValueError:
                self.fecha_registro = None
        else:
            self.fecha_registro = fecha_registro  

    def get_codigo(self):
        return self.codigo

    def get_nombre_cliente(self):
        return self.nombre_cliente

    def get_tipo_servicio(self):
        return self.tipo_servicio

    def get_correo(self):
        return self.correo

    def get_telefono(self):
        return self.telefono

    def get_pregunta1(self):
        return self.pregunta1

    def get_pregunta2(self):
        return self.pregunta2

    def get_pregunta3(self):
        return self.pregunta3

    def get_fecha_registro(self):
        return self.fecha_registro

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre_cliente(self, nombre_cliente):
        self.nombre_cliente = nombre_cliente

    def set_tipo_servicio(self, tipo_servicio):
        self.tipo_servicio = tipo_servicio

    def set_correo(self, correo):
        self.correo = correo

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_pregunta1(self, pregunta1):
        self.pregunta1 = pregunta1

    def set_pregunta2(self, pregunta2):
        self.pregunta2 = pregunta2

    def set_pregunta3(self, pregunta3):
        self.pregunta3 = pregunta3

    def set_fecha_registro(self, fecha_registro):
        if isinstance(fecha_registro, str):
            try:
                self.fecha_registro = datetime.strptime(fecha_registro, '%Y-%m-%d').date()
            except ValueError:
                self.fecha_registro = None
        else:
            self.fecha_registro = fecha_registro

    def __str__(self):
        fecha_str = self.fecha_registro.strftime('%Y-%m-%d') if self.fecha_registro else 'None'
        return (f"Encuesta(codigo='{self.codigo}', nombre_cliente='{self.nombre_cliente}', "
                f"tipo_servicio='{self.tipo_servicio}', correo='{self.correo}', telefono='{self.telefono}', "
                f"pregunta1='{self.pregunta1}', pregunta2='{self.pregunta2}', pregunta3='{self.pregunta3}', "
                f"fecha_registro='{fecha_str}')")

import re
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from datetime import datetime
from src.UI.vtnEncuestas import Ui_Encuestas
from src.datos.EncuestasDao import EncuestaDao
from src.dominio.encuestas import Encuesta

class EncuestaServicio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Encuestas()
        self.ui.setupUi(self)

        self.ui.btnguardar.clicked.connect(self.guardar)
        self.ui.btnborrar.clicked.connect(self.borrar)
        self.ui.btnactualizar.clicked.connect(self.actualizar)
        self.ui.btnlimpiar.clicked.connect(self.limpiar)
        self.ui.btnbuscar.clicked.connect(self.buscar)

        self.ui.txttelefono.setValidator(QIntValidator(0, 9999999))
        self.ui.txtcodigo.setMaxLength(10)
        self.ui.txtbuscarencuesta.setMaxLength(10)

    def validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def validar_campos(self, codigo, nombre, tipo, correo, telefono, p1, p2, p3, fecha):
        if not nombre:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el nombre del cliente.')
            print("Falta nombre.")
            return False

        if tipo == 'Seleccionar':
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un tipo de servicio.')
            print("Tipo de servicio no seleccionado.")
            return False

        if not codigo:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el código de la encuesta.')
            print("Falta código.")
            return False

        if not correo or '@' not in correo or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un correo válido.')
            print("Correo inválido.")
            return False

        if len(telefono) != 7 or not telefono.isdigit():
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un teléfono válido (7 dígitos numéricos).')
            print("Teléfono inválido.")
            return False

        if not p1:
            QMessageBox.warning(self, 'Advertencia', 'Complete la pregunta 1.')
            print("Pregunta 1 incompleta.")
            return False

        if not p2:
            QMessageBox.warning(self, 'Advertencia', 'Complete la pregunta 2.')
            print("Pregunta 2 incompleta.")
            return False

        if not p3:
            QMessageBox.warning(self, 'Advertencia', 'Complete la pregunta 3.')
            print("Pregunta 3 incompleta.")
            return False

        if not fecha or not self.validar_fecha(fecha):
            QMessageBox.warning(self, 'Advertencia', 'Ingrese una fecha válida (formato: YYYY-MM-DD).')
            print("Fecha inválida.")
            return False

        return True

    def guardar(self):
        codigo = self.ui.txtcodigo.text().strip()
        nombre = self.ui.txtnombre.text().strip()
        tipo = self.ui.cbtipo.currentText()
        correo = self.ui.txtcorreo.text().strip()
        telefono = self.ui.txttelefono.text().strip()
        pregunta1 = self.ui.txtpregunta_1.text().strip()
        pregunta2 = self.ui.txtpregunta_2.text().strip()
        pregunta3 = self.ui.txtpregunta_3.text().strip()
        fecha_registro = self.ui.txtfecha.text().strip()

        if not self.validar_campos(codigo, nombre, tipo, correo, telefono,
                                  pregunta1, pregunta2, pregunta3, fecha_registro):
            return

        if EncuestaDao.buscar_por_codigo(codigo):
            QMessageBox.warning(self, 'Advertencia', 'Ya existe una encuesta con ese código.')
            print("Código ya existe.")
            return

        encuesta = Encuesta(codigo, nombre, tipo, correo, telefono, pregunta1, pregunta2, pregunta3, fecha_registro)
        resultado = EncuestaDao.guardar(encuesta)

        if resultado == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo guardar la encuesta.')
            print("Error al guardar encuesta.")
        else:
            self.ui.statusbar.showMessage('Encuesta guardada exitosamente', 3000)
            print("Encuesta guardada correctamente.")
            self.limpiar()

    def actualizar(self):
        if QMessageBox.question(self, 'Confirmar', '¿Está seguro de actualizar?') != QMessageBox.Yes:
            print("Actualización cancelada por usuario.")
            return

        codigo = self.ui.txtcodigo.text().strip()

        if not EncuestaDao.buscar_por_codigo(codigo):
            QMessageBox.warning(self, 'Advertencia', 'No se encontró la encuesta para actualizar.')
            print("Encuesta para actualizar no encontrada.")
            return

        nombre = self.ui.txtnombre.text().strip()
        tipo = self.ui.cbtipo.currentText()
        correo = self.ui.txtcorreo.text().strip()
        telefono = self.ui.txttelefono.text().strip()
        pregunta1 = self.ui.txtpregunta_1.text().strip()
        pregunta2 = self.ui.txtpregunta_2.text().strip()
        pregunta3 = self.ui.txtpregunta_3.text().strip()
        fecha_registro = self.ui.txtfecha.text().strip()

        if not self.validar_campos(codigo, nombre, tipo, correo, telefono,
                                  pregunta1, pregunta2, pregunta3, fecha_registro):
            return

        encuesta = Encuesta(codigo, nombre, tipo, correo, telefono, pregunta1, pregunta2, pregunta3, fecha_registro)
        resultado = EncuestaDao.actualizar(encuesta)

        if resultado == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo actualizar la encuesta.')
            print("Error al actualizar encuesta.")
        else:
            self.ui.statusbar.showMessage('Encuesta actualizada exitosamente', 3000)
            print("Encuesta actualizada correctamente.")
            self.limpiar()

    def buscar(self):
        codigo_buscar = self.ui.txtbuscarencuesta.text().strip()
        if not codigo_buscar:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un código para buscar.')
            print("Falta código para buscar.")
            return

        encuesta = EncuestaDao.buscar_por_codigo(codigo_buscar)
        if encuesta:
            self.ui.txtcodigo.setText(encuesta.get_codigo())
            self.ui.txtnombre.setText(encuesta.get_nombre_cliente())
            index = self.ui.cbtipo.findText(encuesta.get_tipo_servicio())
            self.ui.cbtipo.setCurrentIndex(index if index != -1 else 0)
            self.ui.txtcorreo.setText(encuesta.get_correo())
            self.ui.txttelefono.setText(encuesta.get_telefono())
            self.ui.txtpregunta_1.setText(encuesta.get_pregunta1())
            self.ui.txtpregunta_2.setText(encuesta.get_pregunta2())
            self.ui.txtpregunta_3.setText(encuesta.get_pregunta3())

            fecha = encuesta.get_fecha_registro()
            fecha_str = fecha.strftime('%Y-%m-%d') if hasattr(fecha, 'strftime') else fecha if fecha else ''
            self.ui.txtfecha.setText(fecha_str)

            print("Encuesta encontrada y cargada.")
        else:
            QMessageBox.information(self, 'Información', 'Encuesta no encontrada.')
            print("No se encontró encuesta.")

    def borrar(self):
        if QMessageBox.question(self, 'Confirmar', '¿Está seguro de borrar?') != QMessageBox.Yes:
            print("Eliminación cancelada por usuario.")
            return

        codigo = self.ui.txtcodigo.text().strip()
        if not codigo:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un código válido para borrar.')
            print("Falta código para borrar.")
            return

        resultado = EncuestaDao.eliminar(codigo)
        if resultado == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo borrar la encuesta.')
            print("Error al eliminar encuesta.")
        else:
            self.ui.statusbar.showMessage('Encuesta borrada exitosamente', 3000)
            print("Encuesta eliminada correctamente.")
            self.limpiar()

    def limpiar(self):
        self.ui.txtcodigo.clear()
        self.ui.txtnombre.clear()
        self.ui.cbtipo.setCurrentIndex(0)
        self.ui.txtcorreo.clear()
        self.ui.txttelefono.clear()
        self.ui.txtpregunta_1.clear()
        self.ui.txtpregunta_2.clear()
        self.ui.txtpregunta_3.clear()
        self.ui.txtfecha.clear()
        self.ui.txtbuscarencuesta.clear()
        print("Campos limpiados.")


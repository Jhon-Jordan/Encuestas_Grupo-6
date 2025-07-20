from src.dominio.encuestas import Encuesta
from src.datos.conexion import Conexion

class EncuestaDao:

    @classmethod
    def guardar(cls, encuesta: Encuesta):
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()
        sql = '''
            INSERT INTO Encuestas (
                codigo, nombre_cliente, tipo_servicio, correo, telefono,
                pregunta1, pregunta2, pregunta3, fecha_registro
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        valores = (
            encuesta.codigo,
            encuesta.nombre_cliente,
            encuesta.tipo_servicio,
            encuesta.correo,
            encuesta.telefono,
            encuesta.pregunta1,
            encuesta.pregunta2,
            encuesta.pregunta3,
            encuesta.fecha_registro  
        )
        try:
            cursor.execute(sql, valores)
            conexion.commit()
        except Exception as e:
            print(f"Error al guardar encuesta: {e}")
            conexion.rollback()
            cursor.close()
            return -1
        cursor.close()
        return 1

    @classmethod
    def buscar_por_codigo(cls, codigo):
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()
        sql = 'SELECT codigo, nombre_cliente, tipo_servicio, correo, telefono, pregunta1, pregunta2, pregunta3, fecha_registro FROM Encuestas WHERE codigo = ?'
        cursor.execute(sql, (codigo,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Encuesta(*fila)
        return None

    @classmethod
    def actualizar(cls, encuesta: Encuesta):
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()
        sql = '''
            UPDATE Encuestas SET
                nombre_cliente = ?,
                tipo_servicio = ?,
                correo = ?,
                telefono = ?,
                pregunta1 = ?,
                pregunta2 = ?,
                pregunta3 = ?,
                fecha_registro = ?
            WHERE codigo = ?
        '''
        valores = (
            encuesta.nombre_cliente,
            encuesta.tipo_servicio,
            encuesta.correo,
            encuesta.telefono,
            encuesta.pregunta1,
            encuesta.pregunta2,
            encuesta.pregunta3,
            encuesta.fecha_registro,  
            encuesta.codigo
        )
        try:
            cursor.execute(sql, valores)
            conexion.commit()
        except Exception as e:
            print(f"Error al actualizar encuesta: {e}")
            conexion.rollback()
            cursor.close()
            return -1
        cursor.close()
        return 1

    @classmethod
    def eliminar(cls, codigo):
        conexion = Conexion.obtenerConexion()
        cursor = conexion.cursor()
        sql = 'DELETE FROM Encuestas WHERE codigo = ?'
        try:
            cursor.execute(sql, (codigo,))
            conexion.commit()
        except Exception as e:
            print(f"Error al eliminar encuesta: {e}")
            conexion.rollback()
            cursor.close()
            return -1
        cursor.close()
        return 1

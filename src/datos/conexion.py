import sys
import pyodbc as bd

class Conexion:
    _SERVIDOR = '192.168.100.9'
    _BBDD = 'Encuestas'
    _USUARIO = 'grupo6pro'
    _PASSWORD = 'grupo6pro123'
    _conexion = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};'
                    f'UID={cls._USUARIO};'
                    f'PWD={cls._PASSWORD};'
                    'Network=dbmssocn;'
                    'TrustServerCertificate=yes;'
                )
            except Exception as e:
                print(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit(1)
        return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        try:
            return cls.obtenerConexion().cursor()
        except Exception as e:
            print(f'Ocurrió una excepción al obtener el cursor: {e}')
            sys.exit(1)

if __name__ == '__main__':
    conexion = Conexion.obtenerConexion()
    cursor = Conexion.obtenerCursor()
    print('Conexión establecida:', conexion)
    print('Cursor obtenido:', cursor)

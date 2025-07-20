# Sistema de Gestión de Encuestas de Satisfacción del Cliente

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green)
![SQL Server](https://img.shields.io/badge/SQL%20Server-Database-red)

---

## 📚 Carrera  
**Licenciatura en Gestión de la Información Gerencial**

---

## 👥 Equipo de Desarrollo  
Grupo 6
- Murillo Christian  
- Jordan Jhon  
- Manobanda Marcos  
- Tejena Daniel  
- Changuan Asthon  

---

## 📝 Descripción  

Este proyecto consiste en un sistema de escritorio para la gestión de encuestas de satisfacción del cliente. Permite registrar, buscar, actualizar y eliminar encuestas de forma sencilla y segura, con una interfaz amigable desarrollada en PySide6 y una base de datos en SQL Server para el almacenamiento de la información.

---

## ⚙️ Tecnologías usadas  

- **Python 3**  
- **PySide6** para la interfaz gráfica  
- **pyodbc** para conexión con SQL Server  
- **Qt Designer** para diseño visual  
- **SQL Server** como base de datos  

---

## 🗂 Estructura del proyecto
src/ ├── UI/ │    
              ├── vtnEncuestas.ui │    
              └── vtnEncuestas.py 
├── dominio/ │    
              └── encuestas.py 
├── datos/ │    
              ├── conexion.py │    
              └── EncuestaDao.py 
└── servicio/ 
            └── EncuestaServicio.py

---

## 🚀 Funcionalidades principales  

- Registro de encuestas con validación completa  
- Búsqueda de encuestas por código  
- Actualización y eliminación de registros  
- Validación de campos (correo, teléfono, fechas, etc.)  
- Mensajes claros y confirmaciones para el usuario  

---

## 💻 Instalación y configuración  

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/Jhon-Jordan/Encuestas_Grupo-6

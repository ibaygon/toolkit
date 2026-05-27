# Sys Admin Toolkit

Kit de herramientas de administración de sistemas construido en Python.

Conjunto de módulos CLI que automatiza tareas reales de sysadmin: auditoría de
logs SSH, geolocalización de IPs atacantes, gestión de inventarios de red y
generación de reportes Excel ejecutivos.


Repositorio: https://github.com/ibaygon/toolkit

---

## Características

1. Auditor de seguridad SSH que parsea logs, extrae IPs atacantes y las geolocaliza consultando una API externa
2. Generador y analizador de inventarios de red con 1000 servidores ficticios, filtrado por vulnerabilidad y agrupación por departamento
3. Exportador automático de reportes Excel listos para gerencia con datos filtrados y agrupados

---

## Tecnologías

### Módulos principales
Módulo: Uso
sys_toolkit.py: Menú CLI interactivo que orquesta todas las herramientas
log_parser.py: Parseo de auth.log con sets y diccionarios para contar IPs
threat_intel.py: Integración con ipinfo.io para geolocalizar atacantes

### Librerías de datos
Librería: Uso 
Pandas: Carga, filtrado y agrupación del inventario CSV
OpenPyXL: Generación de archivos Excel reales desde DataFrames
Faker: Generación de 1000 servidores ficticios con datos realistas 

### Auxiliares
Herramienta: Uso 
requests: Llamadas HTTP a la API de geolocalización 
pytest: Tests unitarios del parser de logs 
mypy: Verificación estática de type hints 

---

## Estructura del proyecto

La raíz del repositorio contiene todos los módulos Python al mismo nivel para
permitir importaciones directas entre ellos.

**sys_toolkit.py** es el punto de entrada principal con el menú interactivo CLI.
**os_utils.py** contiene las funciones de ping y comprobación de disco usando
subprocess y shutil. **log_parser.py** lee auth.log línea a línea con un gestor
de contexto y extrae IPs fallidas usando sets y diccionarios. **network_models.py**
define la jerarquía de clases NetworkDevice, Router y Server con polimorfismo en
el método audit_device. **threat_intel.py** consulta la API de ipinfo.io y muestra
una tabla con país y organización de cada atacante. **generate_inventory.py** genera
un CSV con 1000 servidores ficticios usando Faker. **inventory_manager.py** carga el
CSV con Pandas, filtra vulnerables y exporta a Excel. **test_toolkit.py** contiene
los tests unitarios del parser ejecutables con pytest.

La carpeta **data** contiene los archivos de entrada y salida: auth.log con los logs
SSH simulados, inventory.csv con el inventario generado y report_YYYY-MM.xlsx con
el reporte ejecutivo. La carpeta **docs** contiene python-sysadmin.md con la
justificación técnica del uso de Python en administración de sistemas.

---

## Descargar y ejecutar

```bash
git clone https://github.com/ibaygon/toolkit.git
cd toolkit
```

Crea el entorno virtual e instala las dependencias:

```bash
python -m venv venv
venv\Scripts\activate      
source venv/bin/activate   
pip install -r requirements.txt
```

Ejecuta el toolkit:

```bash
python generate_inventory.py   
python sys_toolkit.py          
```

Ejecuta los tests:

```bash
pytest test_toolkit.py -v
```

---

## Desarrollado durante las prácticas en Corner Estudios — Pietro Simonato — 2026
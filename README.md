# QA Automation Framework - Proyecto Final

Este repositorio contiene mi trabajo final del curso de Automation Testing. Armé un framework que combina pruebas de interfaz (UI) con Selenium y pruebas de backend (API) con Requests, aplicando el patrón Page Object Model para que sea ordenado y mantenible.

## Estructura del Proyecto

```
QA-AUTOMATION-FRAMEWORK/
├── .github/workflows/        # Pipeline CI/CD con GitHub Actions
├── pages/                    # Page Object Model (BasePage, LoginPage, InventoryPage)
├── tests/                    # Scripts de prueba (UI y API)
├── utils/                    # Configuración del driver y helpers
├── reports/                  # Reportes HTML generados
├── logs/                     # Archivos de log
├── conftest.py               # Configuración global de Pytest (capturas, logger)
├── requirements.txt
└── README.md
```

## Requisitos e instalación

- Python 3.10+
- Instalar dependencias: `pip install -r requirements.txt`

## Ejecución

```bash
# Correr todas las pruebas
pytest tests/ -v -s

# Generar reporte HTML
pytest tests/ -v --html=reports/reporte_final.html --self-contained-html

# Filtrar por tipo
pytest -m ui    # solo UI
pytest -m api   # solo API
```

## Pruebas incluidas

**UI (Selenium):**
- Login con usuario estándar
- Validación del inventario (productos visibles)
- Agregar producto al carrito y verificar contador

**API (Requests):**
- Consultas GET (validación de códigos y datos)
- Operaciones POST (creación de recursos)

## Reportes y logs

- **HTML** (`reports/`): Resumen visual con estado de cada prueba. Si falla una UI, incluye captura de pantalla.
- **Logs** (`logs/suite.log`): Registro detallado de cada interacción y respuesta, útil para depurar.

## Detalles técnicos

- **Page Object Model**: Separa selectores de la lógica de prueba.
- **webdriver-manager**: Maneja automáticamente las versiones del driver.
- **conftest.py**: Hooks para capturas automáticas en fallos y logging.
- **CI/CD**: Pipeline en GitHub Actions que ejecuta pruebas en cada push.

---

**Autor:** Romina Paola Benítez  
**Contexto:** Trabajo Final Integrador - Curso de Automatización de Testing
import pytest
import os
import logging
from utils.driver_setup import get_driver

# Configuración del archivo de Log
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/suite.log"),
        logging.StreamHandler()
    ]
)

@pytest.fixture
def driver(request):
    navegador = get_driver()
    navegador.implicitly_wait(10)
    yield navegador
    
    # Hook para tomar captura de pantalla solo si falla
    if request.node.rep_call.failed:
        if not os.path.exists('reports'):
            os.makedirs('reports')
        # Guardar evidencia con el nombre del test fallido
        navegador.save_screenshot(f"reports/{request.node.name}_fallo.png")
    
    navegador.quit()

# Código interno de Pytest para saber el resultado del test (pasó/falló)
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
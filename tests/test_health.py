from fastapi.testclient import TestClient      # cliente que simula pedidos HTTP sin levantar un servidor real
from conciliador.api.main import app           # importa la aplicación (todavía no existe: por eso va a fallar)

cliente = TestClient(app)                      # crea el "visitante falso" que va a golpear las ventanillas de app


def test_health_responde_ok():                 # pytest ejecuta toda función que empiece con test_
    respuesta = cliente.get("/health")         # envía un pedido GET a /health y guarda la respuesta
    assert respuesta.status_code == 200        # assert = "exijo que esto sea verdad"; si no lo es, la prueba falla
    assert respuesta.json() == {"status": "ok"}  # exige que el contenido sea exactamente este diccionario
"""Punto de entrada de la API web del conciliador."""   # docstring: describe el archivo para quien lo lea

from fastapi import FastAPI                 # la clase que representa una aplicación web

app = FastAPI(title="Conciliador", version="0.1.0")   # crea la aplicación; título y versión aparecen en /docs


@app.get("/health")                         # decorador: "los pedidos GET a /health los atiende la función de abajo"
def health() -> dict[str, str]:             # la función; -> dict[str, str] indica que devuelve un diccionario de textos
    return {"status": "ok"}                 # FastAPI convierte este diccionario a JSON automáticamente
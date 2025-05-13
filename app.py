from flask import Flask
from data.data_productos import productos, categorias  # Importar los datos

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Martín Bernatene</h1> <h2>Estudiante de Desarrollo de Aplicaciones Web</h2>'

@app.route("/productos")
def listar_productos():
    productos_str = "<br>".join(
        [f"ID: {p['id']} - Descripción: {p['descripcion']} - Categoría ID: {p['categoria_id']}" for p in productos]
    )
    return f"<h2>Lista de Productos</h2><p>{productos_str}</p>"

@app.route("/categorias")
def listar_categorias():
    categorias_str = "<br>".join(
        [f"ID: {c['id']} - Descripción: {c['descripcion']}" for c in categorias]
    )
    return f"<h2>Lista de Categorías</h2><p>{categorias_str}</p>"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask


# Instanciamos con la Clase Flask 
app = Flask(__name__)


# Ahora llenaremos info a nuestro server

# Primer Endpoint
@app.route('/', methods=["GET"])
def any():
    return {
        "Status" : "ta MAL"
    }

# Objeto para mi endpoint 2 
todos = [
    {
        "id" : 2,
        "label" : "jordy",
        "done" : False,
    },
    {
        "id" : 3 ,
        "label" : "makina",
        "done" : True,
        "descripcion" : "Mamado y retirado",
    }]
    


# Segundo Endpoint
@app.route('/todos', methods=["GET"])
def any_2 ():
    return todos

makina = {}
# Tercer Endpoint
@app.route('/todos/makina', methods=["GET"])
def any_3 ():
    for index, unit in enumerate(todos):
        if index == 1:
            for key in unit.keys():
                makina[key] = unit[key]
    return makina
        
   

# Si es igual a main ( Desde donde name fue llamado ) ejecuta el server
if __name__ == '__main__':
    # Hostealo manual o lo hace automatico
    app.run(debug=True)


from flask import Flask
from flask import render_template, request, redirect
import requests
app = Flask(__name__, template_folder="templates")


@app.route("/")
def vista():
    response = requests.get("http://127.0.0.1:8000/api/user")
    print(response)
    data = response.json()
    if response.status_code == 200:
        print(data)

    return render_template("index.html", tabla=data)


@app.route("/crear", methods=["post"])
def crear():
    nom = request.form["name"]
    ape = request.form["apellidos"]
    pas = request.form["password"]

    url = 'http://127.0.0.1:8000/api/user'
    myobj = {'id': '0', 'nombres': nom, 'apellidos': ape,
             'password': pas, 'fecha': '12/05/2023'}

    x = requests.post(url, json=myobj)


@app.route("/actualizar", methods=["post"])
def actualizar():
    id = request.form["id2"]
    nom = request.form["name2"]
    ape = request.form["apellidos2"]
    pas = request.form["password2"]

    url = 'http://127.0.0.1:8000/api/user/'+id
    myobj = {'id': '0', 'nombres': nom, 'apellidos': ape,
             'password': pas, 'fecha': '12/05/2023'}

    x = requests.put(url, json=myobj)

    return redirect("/")


@app.route("/eliminar", methods=["post"])
def eliminar():
    id = request.form["id3"]
    url = 'http://127.0.0.1:8000/api/user/'+id

    x = requests.delete(url)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

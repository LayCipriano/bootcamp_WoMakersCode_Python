from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character" #link api rick and morty
    response = urllib.request.urlopen(url) #variavel utilizada para abrir a api
    data = response.read() #variavel para fazer a leitura dos resultados
    dict = json.loads(data)    

    return render_template("characters.html", characters=dict["results"])

@app.route("/character/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id #link api rick and morty
    response = urllib.request.urlopen(url) #variavel utilizada para abrir a api
    data = response.read() #variavel para fazer a leitura dos resultados
    dict = json.loads(data)    

    return render_template("profile.html", profile=dict)

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character" #link api rick and morty
    response = urllib.request.urlopen(url) #variavel utilizada para abrir a api
    characters = response.read() #variavel para fazer a leitura dos resultados
    dict = json.loads(characters) #formatando esses dados para json
    
    # criação de um dicionário de personsagens
    characters = [] 
    
    # loop para percorrer esses dados e trazer para nosso dicionário
    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"],
            "gender": character["gender"]
        }
        
        characters.append(character)
    
    return {"characters": characters} 
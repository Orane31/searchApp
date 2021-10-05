from flask import Flask, app, render_template, request, jsonify

# from flask.wrappers import Response

import requests

from requests.api import request

# from requests.sessions import _Data
from api_insee import ApiInsee


app = Flask(__name__)

api = ApiInsee(
    key="RU7C1BwIijo3actsq4LPkIlbPOQa", secret="UoRk8PdMpIo9JAkhZLVEyGoQu14a"
)


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/search, methods=['GET', 'POST']")
def search():
    # récupérer l'argument numero siret depuis la fonction async dans main.js :
    siret_a_trouver = request.get_json(cache=False)
    print(siret_a_trouver)

    # définition de l'url de l'api à interroger avec le numero siret en dynamique
    url = f"https://api.insee.fr/entreprises/sirene/V3/siret/{siret_a_trouver}?masquerValeursNulles=true"

    headers = {"Authorization": "Bearer e1d7a601-392f-3112-8266-34963d089375"}
    # requete à l'api
    response = requests.get(url, headers=headers)

    print(response.status_code)

    data = response.json()

    if "etablissement" not in data:
        print("aie aie aie")

    return data


if __name__ == "__main__":
    app.run(debug=True)

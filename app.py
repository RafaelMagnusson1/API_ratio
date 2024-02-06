from flask import Flask, request, jsonify
import pickle
import numpy as np

BASE_DIR = Path(_file_).resolve(strict=True).parent

with open(f"{BASE_DIR}/modelo_ratio_version1.sav", "rb") as f:
    rf_reg = pickle.load(f)
        
colunas = ["sulfato","den_5700_val","diluicao","den_5700_sp"]


app = Flask(__name__)

@app.route('/ratio/', methods = ["POST"])

def ratio():
        
    dados=request.get_json()
    dados_input = np.array([dados[col] for col in colunas]).reshape(1, -1)
    ratio = rf_reg.predict(dados_input)
    return jsonify(ratio = ratio[0])

app.run(debug = True)

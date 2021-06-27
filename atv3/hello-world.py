from flask import Flask
import json
from datetime import datetime
# -*- coding: UTF-8 -*-
app = Flask(__name__)


@app.route('/')

def raiz():
    my_date = datetime.now()
    payload = {'objetivo':'Desafio Técnico da SSYS',
    'feito por':'Thiago Vinney Oliveira Almeida',
    'data':my_date.isoformat()}
    
    
    return json.dumps(payload)

app.run(host='0.0.0.0', port=8080)
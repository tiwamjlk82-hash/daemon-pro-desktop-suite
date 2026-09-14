# build 18c7013803
# (auto) 2771f8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'

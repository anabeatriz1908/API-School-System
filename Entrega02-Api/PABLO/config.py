import os
from flask import Flask

app = Flask(__name__)
app.config['PORT']=5036
app.config['DEBUG']=True
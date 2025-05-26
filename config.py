from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 5036
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql://db_school_vgbu_user:BWZqvsho9UlzTjPXFUiA3Z0HoxMsO0Fu@dpg-d0qd9rbuibrs73eh4880-a.oregon-postgres.render.com/db_school_vgbu')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# antigo postgresql://escoladb_kms8_user:GYmK37zARPPGAjheqS4T8EHxFXbLsAyj@dpg-d092nrh5pdvs73a239og-a.oregon-postgres.render.com/escoladb_kms8
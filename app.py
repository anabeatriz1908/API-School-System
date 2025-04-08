from config import app
import os
from professor_controller import professores_blueprint

app.register_blueprint(professores_blueprint)

if __name__ == '__main__':
    app.run(debug=True,port=5036)
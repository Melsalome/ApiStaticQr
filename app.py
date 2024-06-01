
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
# from blueprints.user import users_bp
from blueprints.table import table_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'http://localhost:3306/'
# db = SQLAlchemy(app)
app.url_map.strict_slashes = False
CORS(app)

# app.register_blueprint(users_bp, url_prefix='/user')
app.register_blueprint(table_bp, url_prefix='/api')



@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3306))
    app.run(host='0.0.0.0', port=PORT, debug=True)

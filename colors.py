from flask import Flask, jsonify
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/colors/<palette>/')
@swag_from('check.yml')
def colors(palette):
    all_colors = {
        'dc1': ['goel.sunand@gmail.com', 'magenta', 'yellow', 'black'], 
        # fetch from db
        # create db, pull data

        'dc2': ['red', 'green', 'blue']
    }
    if palette == 'dc3':
        result = all_colors
    else:
        result = {palette: all_colors.get(palette)}

    return jsonify(result)

app.run(debug=True)
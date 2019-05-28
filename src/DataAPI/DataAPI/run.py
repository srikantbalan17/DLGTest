from config import Config
from flask import Flask, make_response, jsonify
from routes import total_route

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(total_route, url_prefix="/total")


# Default page not found handler for application
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run()


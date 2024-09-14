from flask import Flask, request, jsonify
from blueprints.quote import create_quote_blueprint



def create_app():

    app  = Flask(__name__)

    @app.get("/")
    def health_check():
        return "API working"

    quote_bp  = create_quote_blueprint()
    app.register_blueprint(quote_bp)
    
    return app

if __name__ == "__main__":
    
    app = create_app()
    app.run("0.0.0.0",9000, debug=True)
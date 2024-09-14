from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from utils.math_operations import add, subtract
from . import controller as controller
from . import model as model



def create_quote_blueprint():

    quote_blueprint = Blueprint('quote',__name__,url_prefix="/quote")


    @quote_blueprint.get("/")
    def get_quotes():
        return "QUote endpoint"


    @quote_blueprint.post("/")
    def calculate_quote():
        schema = model.QuoteOperationSchema()
        try:
            data = schema.load(request.json)
        except ValidationError as err:
            return jsonify(err.messages),400
        result = controller.calculate_quote(data)
        return result,200


    return quote_blueprint
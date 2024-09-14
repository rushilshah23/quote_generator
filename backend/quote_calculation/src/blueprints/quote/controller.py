from flask import jsonify
from utils.math_operations import add, subtract
from . import model as model

def calculate_quote(quote_operation_data:model.QuoteOperationSchema):
    result = None
    if quote_operation_data["operation"] == "add":
        result = add(quote_operation_data["number_1"],quote_operation_data["number_2"])
    elif quote_operation_data["operation"] == "subtract":
        result = subtract(quote_operation_data["number_1"],quote_operation_data["number_2"])
    print(f"REsult - {result}")
    return jsonify({"Result":result})
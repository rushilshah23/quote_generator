from marshmallow import Schema, validate, fields


class QuoteOperationSchema(Schema):
    operation = fields.Str(required=True, validate=validate.OneOf(["add","subtract"]))
    number_1 = fields.Float(required=True)
    number_2 = fields.Float(required=True)

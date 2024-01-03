from flask import Blueprint, request, jsonify 
from flask_jwt_extended import create_access_token, jwt_required 
from qweeack.models import User, db, StockSchema, get_stock_data



api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/token', methods = ['GET', 'POST'])
def token():

    data = request.json
    if data:
        client_id = data['client_id']
        access_token = create_access_token(identity=client_id) 
        return {
            'status': 200,
            'access_token': access_token
        }
    else:
        return {
            'status' : 400,
            'message' : 'Missing Client Id. Try Again.'
        }
    
@api.route('/stocks')
@jwt_required()
def get_stocks():
    stocks = get_stock_data.query.all()
    schema = StockSchema(many=True)
    response = schema.dump(stocks)
    return jsonify(response)

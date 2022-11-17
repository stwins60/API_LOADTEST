# Import Flask
from flask import Flask,jsonify, request, make_response
import json
import helper

app = Flask(__name__) # Create an instance of Flask
secret_key = helper.secretKey()
headers = {
    "ContentType": "text/html",
    "Cookies": helper.secretKey(),
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With",
    "Access-Control-Allow-Credentials": "true",
    "Bearer": helper.secretKey()
}

with open('transactions.json') as json_file:
        data = json.load(json_file)
@app.route('/')
@app.route('/api/v1/transactions') # Define the root route
def welcome(): # Define the welcome function
    headers["Status"] = 200
    return make_response(jsonify(data), headers) # Return the welcome message

@app.route('/api/v1/transactions_by_id') # Define the transaction route
def transaction(): # Define the transaction function
    id = request.args.get('id') # Get the id from the url
    new_data = data['transactions']
    for i in new_data:
        if i['id'] == int(id):
            headers["Status"] = 200
            return make_response(jsonify(i), headers, 200) # Return the transaction
    headers["Status"] = 404
    return make_response(jsonify({'error': 'Transaction not found'}), 404, headers)


@app.route('/api/v1/transactions/transact_type') # Define the transaction route
def transaction_type(): # Define the transaction function
    transact_type = request.args.get('transact_type') # Get the transact_type from the url
    new_data = data['transactions']
    result = []
    for i in new_data:
        if i['transType'] == str(transact_type):
            result.append(i)
        
        else:
            headers["Status"] = 404
            return make_response(jsonify({'error': 'Transaction not found'}), 404, headers)
    headers["Status"] = 200        
    return make_response(jsonify(result), headers, 200) # Return the transaction


# post new transaction
@app.route('/api/v1/transactions/new', methods=['POST', 'GET'])
def new_transaction():
    if request.method == 'POST' or request.method == 'GET':
        id = request.args.get('id')
        transType = request.args.get('transType')
        transDate = request.args.get('transDate')
        transAmount = request.args.get('transAmount')
        new_transaction = {
            "id": int(id),
            "transType": transType,
            "transDate": transDate,
            "transAmount": float(transAmount),
        }
        data['transactions'].append(new_transaction)
        return make_response(jsonify({'message': 'Transaction added successfully'}), 201, headers)

# Delete transaction
@app.route('/api/v1/transactions/delete', methods=['DELETE'])
def delete_transaction():
    id = request.args.get('id')
    new_data = data['transactions']
    for i in new_data:
        if i['id'] == int(id):
            print(i['id'])
            new_data.remove(i)
            headers["Status"] = 200
            return make_response(jsonify({'message': 'Transaction deleted successfully'}), headers, 200)
        headers["Status"] = 404
    return make_response(jsonify({'error': 'Transaction not found'}), headers, 404)

# Request bearer token
@app.route('/api/v1/transactions/token', methods=['GET'])
def token():
    headers["Status"] = 200
    return make_response(jsonify({'token': secret_key}), headers, 200)

# pass bearer token to access api
@app.route('/api/v1/transactions/secret', methods=['GET'])
def secret():
    if request.headers.get('Authorization') == secret_key:
        headers["Status"] = 200
        return make_response(jsonify({'message': 'You have access to the secret page'}), headers, 200)
    headers["Status"] = 401
    return make_response(jsonify({'error': 'You do not have access to the secret page'}), headers, 401)

# Ensure that the app is being run directly and not imported
if __name__ == '__main__': 
    # Run the app in debug mode.
    app.run(debug=True, port=5000, host='0.0.0.0')
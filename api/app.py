import os
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# Give proper 404 message for bad requests
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# test API
@app.route('/api/v1/test1', methods=['GET'])
def test_api_1():
    if request.method == 'GET':
        return jsonify({'status_code':200, 'message':'teste 1'})

# test API
@app.route('/api/v1/test2', methods=['GET'])
def test_api_2():
    if request.method == 'GET':
        return jsonify({'status_code':200, 'message':'teste 2'})

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=False)
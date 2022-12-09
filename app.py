from flask import Flask, jsonify, request, Response

from name_validation import is_valid_name
app = Flask(__name__)


@app.route('/api', methods=['POST'])
def index(): 
	try:
		req = request.get_json() 
		if len(req['name'].split(' ')) < 3:
			return Response("fullname must contain three names...", status=400)
		is_valid = is_valid_name(req['name'])
		return jsonify({'valid_name': is_valid})
	except:
		return Response(status=400)

# waitress-serve waitress_server:app

# app.run(port=3000)

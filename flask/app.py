from flask import Flask, request, jsonify
from log_util import create_logger

app = Flask(__name__)

@app.route('/')
def hello():
	logger = create_logger()
	logger.info("Entered hello")
	return "Hello World!"

@app.route('/cache-me')
def cache():
	logger = create_logger()
	logger.info("Entered cache")
	return "nginx will cache this response"

@app.route('/info')
def info():
	logger = create_logger()
	logger.info("Entered info")


	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	logger.debug(resp)
	return jsonify(resp)

@app.route('/flask-health-check')
def flask_health_check():
	logger = create_logger()
	logger.info("health-check")
	return "success"

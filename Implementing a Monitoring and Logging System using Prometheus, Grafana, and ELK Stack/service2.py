from flask import Flask, request
import random
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

# Create a Prometheus counter
requests_counter = Counter('requests_total', 'Total requests received')

@app.route('/api/data', methods=['GET'])
def get_data():
    requests_counter.inc()
    data = {'value': random.randint(1, 100)}
    return {'data': data}

if __name__ == '__main__':
    start_http_server(8002)  # Start Prometheus server
    app.run(debug=True, port=5002)
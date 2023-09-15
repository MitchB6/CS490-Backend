from flask import Flask, jsonify
from flask_cors import CORS
# from healthcheck import HealthCheck
app=Flask(__name__)
CORS(app)
# health=HealthCheck()
# def test():
#    return True, "Hello World"
# health.add_check(test)
# app.add_url_rule('/healthcheck', 'healthcheck', view_func=lamda: health.run())

@app.route('/healthcheck')    
def heath_check():
   return jsonify(status=200, print="Hello World")

if __name__ == "__main__":
   app.run(debug=True)
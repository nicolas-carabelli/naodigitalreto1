from flask import Flask, jsonify
from flask_lambda import FlaskLambda

app = FlaskLambda(__name__)

@app.route('/')
def hello_world():
    return 'Hola, RadioNet!'

def lambda_handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)



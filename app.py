from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, RadioNet!'

# Definir el handler de Lambda
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": jsonify(hello_world())
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

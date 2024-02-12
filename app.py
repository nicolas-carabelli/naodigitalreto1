from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola, RadioNet!'

def lambda_handler(event, context):
    # Obtener la respuesta de Flask
    with app.test_request_context(path=event['path'], method=event['httpMethod']):
        # Obtener la respuesta de la ruta de Flask
        response = app.full_dispatch_request()
        
        # Construir la respuesta para Lambda y API Gateway
        return {
            "statusCode": response.status_code,
            "headers": dict(response.headers),
            "body": response.get_data(as_text=True)
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

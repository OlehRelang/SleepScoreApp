from flask import Flask, request
from tensorflow.python.keras.models import Model, Sequential
from keras._tf_keras.keras.saving import load_model

model = load_model(r'fc2.best_model.keras')

app = Flask(__name__)


@app.route('/model', methods=['POST'])
def serve_model():
    request_data = request.get_json(force=True)
    data = request_data['data']
    return model.predict(data)


if __name__ == '__main__':
    app.run()

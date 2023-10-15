from flask import Flask
from flask import request
from flask import jsonify
import pickle

with open('model2.bin', 'rb') as f_in2, open('dv.bin','rb') as f_in1:
    dv,model = pickle.load(f_in1),pickle.load(f_in2)

app = Flask('predict')
@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'credit_probability': float(y_pred),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
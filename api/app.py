from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import joblib

app = Flask(__name__)
CORS(app)

svm_model = joblib.load('svm_model_2.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer_2.pkl')

def classify_comment(comment):
    comment_vectorized = tfidf_vectorizer.transform([comment])
    prediction = svm_model.predict(comment_vectorized)
    return prediction[0]

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    comment = data['comment']
    label = classify_comment(comment)
    return jsonify({'label': label})

@app.route('/process_json', methods=['POST'])
def process_json():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha proporcionado ningún archivo JSON'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se ha seleccionado ningún archivo'}), 400
    
    if file and file.filename.endswith('.json'):
        comments = json.load(file)
        print("Comentarios cargados desde el archivo JSON:", comments)
        classifications = []
        for comment_data in comments:
            comment = comment_data.get('comment', '')
            label = classify_comment(comment)
            print("Comentario:", comment, "| Clasificación:", label)
            comment_data['label'] = label
            classifications.append(comment_data)
        
        print("Clasificaciones:", classifications)
        return jsonify({'classifications': classifications}), 200
    else:
        return jsonify({'error': 'El archivo proporcionado no es un archivo JSON válido'}), 400

@app.route('/')
def index():
    return '¡Hola! Esta es la página de inicio de la aplicación de clasificación de comentarios.'

if __name__ == '__main__':
    app.run(debug=True)
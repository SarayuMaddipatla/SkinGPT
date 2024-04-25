from flask import Flask, render_template, request, jsonify
from detect import initialize_context, generate_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        image_path = "uploads/" + file.filename
        file.save(image_path)
        context = initialize_context(image_path)  # Get the context dynamically
        return render_template('response.html', context=context, image_path=image_path)

@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        query = request.form['query']
        response = generate_response(request.form['context'], query)
        return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)

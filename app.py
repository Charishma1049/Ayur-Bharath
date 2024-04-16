from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_python_attribute', methods=['POST'])
def update_python_attribute():
    selected_city = request.args.get('city')
    # Perform any actions with the selected city in your Python code
    print(f"Selected City: {selected_city}")
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)

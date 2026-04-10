from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    place = request.form['place']
    return render_template('result.html', place=place)

if __name__ == "__main__":
    app.run(debug=True)
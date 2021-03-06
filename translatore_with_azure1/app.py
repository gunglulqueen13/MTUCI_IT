from flask import Flask, render_template, jsonify, request
import translate


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
@app.route('/data', methods=['post'])
def index():
    return render_template("index.html")


@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)


app.run()
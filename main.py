from flask import Flask, request, render_template_string

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# cd telefone, cd flask, python3 main.py
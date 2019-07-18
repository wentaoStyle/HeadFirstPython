
from vsearch import search4letters
from flask import Flask

app = Flask(__name__)

@app.route('/search4')
def search4() -> str:
    return str(search4letters('life, the universe, and everything', 'xyz'))

app.run(debug=True)

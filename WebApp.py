from vovels7 import search4letters
from flask import Flask

app = Flask(__name__)

@app.route('/')
def do_search() -> str:
    return str(search4letters('It is so cool', 'aeiyo'))


app.run()

from flask import Flask
from flask import render_template, request

from src.lexical import MyLex


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/lexical", methods=['GET', 'POST'])
def lexical():
    llex = ()
    lerror = ()
    code = ''

    if request.method == 'POST':
        code = request.form['code']
        l = MyLex()
        llex, lerror = l.tokenize(code)

    return render_template(
        'lexical_analysis.html', llex=llex, lerror=lerror, code=code
    )


if __name__ == "__main__":
    app.run(debug=True)

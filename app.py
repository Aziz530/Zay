from flask import Flask, render_template

app = Flask(__name__, static_folder='templates', static_url_path='')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def help():
    return """
       Go to Hell
       ... or use:   /fib/{fib_index} \n
       """


@app.route('/fib/<int:n>')
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return f"{a}"


if __name__ == "__main__":
    app.run()

from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return "Ура кошка наконец-то ты питонишь"

@app.route('/test')
def test():
    return "привет"

if __name__ == "__main__":
    app.run()
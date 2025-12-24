from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
    {"name": "Худи Python", "price": "4500", "img": "https://picsum.photos/id/1/300/200"},
    {"name": "Футболка Flask", "price": "2000", "img": "https://picsum.photos/id/2/300/200"},
    {"name": "Кепка Minimal", "price": "1200", "img": "https://picsum.photos/id/3/300/200"}
]

@app.route('/')
def home():
    return render_template('index.html', clothes=ITEMS)

if __name__ == "__main__":
    app.run(debug=True)
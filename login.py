from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

if __name__ == '__main__':
    app.run(debug=True)

print('hello world')

print('nihao')

print('哇哈哈～ 冲突修正好了')
